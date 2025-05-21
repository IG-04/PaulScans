# utils.py
import socket
import requests

VULNERS_API_KEY = 0PNMA5P2Q1FPVHYRZGHA87UGWYZJ3JHIDD4L70FST6YJ66MSGEELQ231Y5JZGSU2
VULNERS_API_URL = "https://vulners.com/api/v3/search/lucene/"

def scan_ports(ip, port_range):
    start, end = map(int, port_range.split('-'))
    open_ports = []
    for port in range(start, end + 1):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        finally:
            sock.close()
    return open_ports

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode(errors='ignore').strip()
        sock.close()
        return banner if banner else "Unknown"
    except:
        return "Unknown"

def lookup_cves(banner):
    if banner == "Unknown":
        return []
    headers = {"Content-Type": "application/json"}
    payload = {
        "query": banner,
        "apiKey": VULNERS_API_KEY
    }
    try:
        response = requests.post(VULNERS_API_URL, json=payload, headers=headers)
        data = response.json()
        results = data.get("data", {}).get("search", [])
        cves = [
            {"id": r["id"], "description": r.get("description", "No description available")}
            for r in results if "id" in r
        ]
        return cves[:3]  # Limit output for the sake of clarity
    except Exception as e:
        print(f"[!] CVE lookup failed: {e}")
        return []
