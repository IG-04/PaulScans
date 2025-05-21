import argparse
from utils import scan_ports, grab_banner, lookup_cves
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="PaulScans - A Simple Vulnerability & Port Scanner Tool")
    parser.add_argument('--target', required=True, help='Target IP address')
    parser.add_argument('--ports', default='1-1024', help='Port range to scan (e.g., 20-80)')
    parser.add_argument('--output', default='report.html', help='Output report file')
    args = parser.parse_args()

    print(f"[+] Scanning target: {args.target}")
    open_ports = scan_ports(args.target, args.ports)
    results = []

    for port in open_ports:
        banner = grab_banner(args.target, port)
        cves = lookup_cves(banner)
        results.append({'port': port, 'banner': banner, 'cves': cves})

    generate_report(args.target, results, args.output)
    print(f"[+] Report generated: {args.output}")

if __name__ == "__main__":
    main()
