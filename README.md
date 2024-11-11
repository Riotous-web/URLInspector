Here’s a README for your GitHub tool UrlInspector, designed to retrieve details from the given link "https://github.com/Riotous-web/UrlInspector.git", with a cool output display and animation for showing results:

UrlInspector 🕵️‍♂️🔍

UrlInspector is a powerful tool designed to inspect and retrieve key information from any given URL. It fetches the HTTP status code, headers, title, meta information, and all links from a website. With a built-in cool animation display, UrlInspector makes the process of inspecting websites both fun and informative!

🚀 Features

 • scan_date: Get the exact time when the URL was scanned.
 • status_code: Retrieves the HTTP status code of the website (e.g., 200, 404, etc.).
 • headers: Shows the headers sent by the web server.
 • title: Extracts the <title> tag of the page.
 • meta: Retrieves the meta description and keywords.
 • links: Extracts all hyperlinks (URLs) from the page.

🌐 How to Use

To inspect any URL, follow these simple steps:

1. Clone the repository:

git clone https://github.com/Riotous-web/UrlInspector.git
cd UrlInspector

2. Install the dependencies:

pip install -r requirements.txt

3. Run the UrlInspector tool:

python urlinspector.py --url https://github.com/Riotous-web/UrlInspector.git

This will retrieve all relevant details from the GitHub URL and show the results.

🖥️ Example Output with Animation

Once the scan is complete, UrlInspector will display the following details in a dynamic and interactive format:

[====================] 0% Scanning: https://github.com/Riotous-web/UrlInspector.git
[🕵️‍♂️] Scan Date: 2024-11-12 14:23:45
[🔗] Status Code: 200 OK
[📝] Title: UrlInspector – GitHub Repository
[🔑] Meta Description: A Python tool to inspect and analyze URLs, providing details like status codes, headers, titles, and links.
[⚙️] Meta Keywords: Python, URL Inspector, Website Scanner
[🔍] Headers:
  - Content-Type: text/html; charset=utf-8
  - Server: GitHub.com
  - Date: Mon, 12 Nov 2024 14:23:45 GMT
[🔗] Links Found:
  - https://github.com/Riotous-web/UrlInspector
  - https://github.com/Riotous-web
  - https://github.com

The animation starts with a progress bar, followed by each result appearing in real time with a smooth, visually appealing display.

🛠️ Available Functions

1. scan_date

 • Retrieves the exact time when the website was scanned.
 • Example: 2024-11-12 14:23:45

2. status_code

 • Retrieves the HTTP status code of the website (e.g., 200 OK, 404 Not Found, 301 Moved Permanently).
 • Example: 200 OK

3. headers

 • Displays the HTTP headers returned by the web server.
 • Example:

- Content-Type: text/html; charset=UTF-8
- Server: GitHub.com



4. title

 • Retrieves the <title> tag of the page.
 • Example: UrlInspector – GitHub Repository

5. meta

 • Retrieves the meta description and keywords from the page.
 • Example:

Meta Description: A Python tool to inspect and analyze URLs, providing details like status codes, headers, titles, and links.
Meta Keywords: Python, URL Inspector, Website Scanner



6. links

 • Extracts and displays all links (URLs) found on the page.
 • Example:

- https://github.com/Riotous-web/UrlInspector
- https://github.com/Riotous-web
- https://github.com

🖼️ Cool Animation Display

The scan process is visually enhanced with a cool animation showing a progress bar while UrlInspector retrieves data.

Here’s an example of the progress bar animation:

import time
import sys

def animate_scan():
    print("[====================] 0% Scanning: https://github.com/Riotous-web/UrlInspector.git")
    for i in range(1, 101):
        sys.stdout.write(f"\r[{'=' * (i // 2)}{' ' * (50 - i // 2)}] {i}% Scanning: https://github.com/Riotous-web/UrlInspector.git")
        sys.stdout.flush()
        time.sleep(0.05)  # Simulate time delay for scanning
    print("\nScan complete! Now fetching results...")

animate_scan()

This simple script simulates a progress bar while the scan is running, creating a dynamic user experience.

🔧 Installation

 1. Clone the repository:

git clone https://github.com/Riotous-web/UrlInspector.git
