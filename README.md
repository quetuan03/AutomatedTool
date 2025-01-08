1. Vulnerability Scanning
- SQL Injection:
    + Login Form
- Cross-Site Scripting (XSS):
    + Reflected XSS
2. Project Structure
main.py: main executable file of the tool
utils.py: extract and submit param to server
sql_injection_scanner.py: Scan file for sql injection vulnerability
xss_scanner.py: Scan file for XSS vulnerability
payloads:
    + sql_injection.txt: sql injection vulnerability test payload list
    + xss_injection.txt: XSS vulnerability test payload 
3. Installation
git clone https://github.com/quetuan03/AutomatedTool.git
Interactive ModeL: python main.py
