import argparse
import json
import yaml
from typing import Any, Dict, Callable, Optional


def load_config(path: str) -> Dict[str, Any]:
    with open(path, 'r') as fh:
        return yaml.safe_load(fh)


def load_benchmark(path: str):
    with open(path, 'r') as fh:
        return json.load(fh)


def find_interface(cfg: Dict[str, Any], name: str) -> Optional[Dict[str, Any]]:
    interfaces = cfg.get("system_interface", [])
    for entry in interfaces:
        if name in entry:
            return entry[name]
    return None


def check_dns(cfg: Dict[str, Any]) -> bool:
    dns = cfg.get("system_dns", {})
    return bool(dns.get("primary") and dns.get("secondary"))


def check_wan_management(cfg: Dict[str, Any]) -> bool:
    iface = find_interface(cfg, "port1")
    if not iface:
        return False
    allowed = set((iface.get("allowaccess") or "").split())
    disallowed = {"https", "http", "ping", "ssh", "snmp", "radius-acct"}
    return not disallowed.intersection(allowed)


def check_timezone(cfg: Dict[str, Any]) -> bool:
    return bool(cfg.get("system_global", {}).get("timezone"))


def check_hostname(cfg: Dict[str, Any]) -> bool:
    hostname = cfg.get("system_global", {}).get("hostname", "")
    return bool(hostname and not hostname.lower().startswith("fortigate"))


CHECKS: Dict[str, Callable[[Dict[str, Any]], bool]] = {
    "1.1": check_dns,
    "1.3": check_wan_management,
    "2.1.3": check_timezone,
    "2.1.5": check_hostname,
}


def main():
    parser = argparse.ArgumentParser(description="Check FortiGate CIS Benchmark compliance")
    parser.add_argument("benchmark", help="Path to benchmark JSON file")
    parser.add_argument("config", help="Path to FortiGate config YAML")
    args = parser.parse_args()

    benchmark = load_benchmark(args.benchmark)
    config = load_config(args.config)

    for item in benchmark:
        title = item.get("title", "")
        check_id = title.split()[0]
        status = "NOT IMPLEMENTED"
        func = CHECKS.get(check_id)
        if func:
            try:
                status = "PASS" if func(config) else "FAIL"
            except Exception:
                status = "ERROR"
        print(f"{check_id}\t{title}\t{status}")


if __name__ == "__main__":
    main()
