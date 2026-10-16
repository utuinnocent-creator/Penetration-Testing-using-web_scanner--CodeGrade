# Automated Reflected XSS Scanner

##  Project Overview
This repository contains `xss_scanner.py`, a custom Python tool developed for authorized penetration testing engagements. The script automates the detection of **Reflected Cross-Site Scripting (XSS)** vulnerabilities by submitting varied test payloads and analyzing HTTP responses for reflection.

Designed for use in the Capstone Project security assessment, this tool helps identify injection flaws in web applications (such as search forms or error handlers) that could allow attackers to execute malicious scripts in a victim's browser.

##  Disclaimer & Ethical Use
**This tool is intended for authorized security testing and educational purposes only.**
- **Authorization:** Always obtain explicit written permission from the website owner before scanning.
- **Impact:** While this scanner is designed to be non-destructive, submitting payloads to live systems may trigger security alerts or logs.
- **Liability:** The authors are not liable for any misuse, legal issues, or disruptions arising from the use of this script.
- **Compliance:** Use only within the defined Rules of Engagement (ROE).

##  Features
- **Dynamic Payload Submission:** Automatically generates and submits a list of varied XSS test strings, including standard, encoded, and obfuscated variants (e.g., URL-encoded `<script>` tags).
- **Advanced Reflection Detection:**
  - Analyzes HTTP response bodies for exact payload matches.
  - Handles encoded responses by decoding them before checking for reflection.
  - **False Positive Mitigation:** Implements strict matching logic to ensure the detected string originated from user input and is not a static part of the page.
- **Safe Testing:** Uses unique, non-malicious strings (e.g., `<xss-test-12345>`) to verify reflection without executing actual JavaScript in the tester's browser.
- **Detailed Reporting:** Provides clear output indicating which payloads were reflected, the specific parameter vulnerable, and the HTTP status code returned.
- **Error Handling:** Robust handling of network errors, timeouts, and invalid URLs.

##  Technical Details
- **Language:** Python 3
- **Libraries:** `requests`, `urllib.parse`, `sys`
- **OS Compatibility:** Linux (Kali, Ubuntu), macOS, Windows
- **Methodology:**
  1. **Payload Generation:** Creates a list of test strings, including URL-encoded versions of common XSS vectors.
  2. **Request Submission:** Sends HTTP GET/POST requests with payloads injected into specified parameters.
  3. **Response Analysis:** Inspects the raw response and decoded response for the presence of the original payload.
  4. **Validation:** Cross-references findings to eliminate false positives.

##  Installation & Requirements
No external libraries beyond standard Python packages are required for basic functionality, though `requests` is recommended for advanced HTTP handling.

**Prerequisites:**
- Python 3.6 or higher
- `pip install requests` (if using the requests library)
- Target web application (e.g., a local test environment like OWASP Juice Shop, DVWA, or a custom Flask app)

##  Usage
Run the script from the command line. You must specify the target URL and the parameter to test.

### Basic Usage
```bash
python3 xss_scanner.py
