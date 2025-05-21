

```
  ____             _ ____                      
 |  _ \ __ _ _   _| / ___|  ___ __ _ _ __  ___ 
 | |_) / _` | | | | \___ \ / __/ _` | '_ \/ __|
 |  __/ (_| | |_| | |___) | (_| (_| | | | \__ \
 |_|   \__,_|\__,_|_|____/ \___\__,_|_| |_|___/
                                                                                           
 ```                                            

## Description
PaulScans is a basic vulnerability scanner written in Python that can:
- Perform port scanning
- Grab banners from open ports
- Search for known vulnerabilities (CVEs) using Vulners
- Generate a simple HTML or PDF report summarizing findings

This project is intended for educational purposes and meant to showcase the skills I've learned in the past few months. 

---

## Features
- TCP port scanning using sockets
- Banner grabbing to identify services
- CVE lookups using Vulners API
- Command-line interface
- Report generation (HTML or PDF)

---

## Technologies Used
- Python 3
- `socket` for basic networking
- `requests` for API calls
- `jinja2` + `weasyprint` for HTML/PDF reporting

---

## Installation
```bash
# Clone the repo
git clone https://github.com/IG-04/PaulScans.git
cd paulscans

# Install dependencies
pip install -r requirements.txt
```

---

## Usage
```bash
# Basic scan of an IP
python paulscans.py --target 192.168.1.1

# With custom port range
python paulscans.py --target 192.168.1.1 --ports 20-1024

# Output to HTML report
python paulscans.py --target 192.168.1.1 --output report.html
```

---

## Example Output
![screenshot](screenshots/sample_report.png)

---

## Folder Structure
```
paulscans/
├── paulscans.py            # Main script
├── utils.py                # Helper functions (e.g., API calls, parsing)
├── report_generator.py     # Report output logic
├── templates/              # HTML templates for report
│   └── report.html         # Jinja2 template
├── requirements.txt        # Python dependencies
├── README.md
├── screenshots/            # Example screenshots
└── reports/                # Generated reports
```

---

## APIs Used
- [Vulners API](https://vulners.com/) for CVE lookup

---

## TODO
- Add UDP scanning support
- Integrate multithreading for faster scans

---

## Disclaimer
This tool is for educational and authorized use only. Do not scan systems you do not have permission to test.
