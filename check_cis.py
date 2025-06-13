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


def check_1_1(cfg: Dict[str, Any]) -> bool:
    """Ensure DNS server is configured."""
    dns = cfg.get("system_dns", {})
    return bool(dns.get("primary") and dns.get("secondary"))


def check_1_2(cfg: Dict[str, Any]) -> bool:
    """Ensure intra-zone traffic is not always allowed."""
    zones = cfg.get("system_zone", [])
    if not zones:
        return False
    for zone in zones:
        for _name, props in zone.items():
            if props.get("intrazone") != "deny":
                return False
    return True


def check_1_3(cfg: Dict[str, Any]) -> bool:
    """Disable all management related services on WAN port."""
    iface = find_interface(cfg, "port1")
    if not iface:
        return False
    allowed = set((iface.get("allowaccess") or "").split())
    disallowed = {"https", "http", "ping", "ssh", "snmp", "radius-acct"}
    return not disallowed.intersection(allowed)


def check_2_1_3(cfg: Dict[str, Any]) -> bool:
    """Ensure timezone is properly configured."""
    return bool(cfg.get("system_global", {}).get("timezone"))


def check_2_1_5(cfg: Dict[str, Any]) -> bool:
    """Ensure hostname is set."""
    hostname = cfg.get("system_global", {}).get("hostname", "")
    return bool(hostname and not hostname.lower().startswith("fortigate"))


def get_check(check_id: str) -> Optional[Callable[[Dict[str, Any]], bool]]:
    """Return the check function for a given CIS control ID."""
    func_name = f"check_{check_id.replace('.', '_')}"
    return globals().get(func_name)


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
        func = get_check(check_id)
        if func:
            try:
                status = "PASS" if func(config) else "FAIL"
            except Exception:
                status = "ERROR"
        print(f"{check_id}\t{title}\t{status}")


if __name__ == "__main__":
    main()
