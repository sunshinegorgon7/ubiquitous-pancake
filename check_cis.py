import argparse
from pyfgtconflib import Parser


def parse_config(path: str):
    """Parse FortiGate configuration using pyfgtconflib."""
    parser = Parser()
    with open(path) as fh:
        return parser.parse_text(fh.readlines())


def check_1_1(cfg) -> bool:
    """Ensure DNS server is configured."""
    dns = cfg.get('config system dns', {})
    return bool(dns.get('set primary') and dns.get('set secondary'))


def main():
    parser = argparse.ArgumentParser(description="Validate CIS 1.1 for a FortiGate config")
    parser.add_argument('config', help='Path to fgt.conf configuration file')
    args = parser.parse_args()

    cfg = parse_config(args.config)
    result = "PASS" if check_1_1(cfg) else "FAIL"
    print(f"1.1 Ensure DNS server is configured\t{result}")


if __name__ == '__main__':
    main()
