URLInspector - README

Welcome to URLInspector! 🌐🔍 A simple yet powerful tool designed for inspecting and analyzing key aspects of any URL you provide. Whether you’re a developer, SEO specialist, or just want to gather essential information about a webpage, URLInspector will help you dig deeper and get all the data you need in a clean and easy-to-understand format.

🛠️ Key Features

🗓️ scan_date

The scan_date function provides the exact timestamp of when the URL was scanned. This is particularly useful for tracking when a webpage was last analyzed, ensuring that your data is up-to-date.

Example:

inspector.scan_date()
# Output: "2024-11-12 10:00 AM"

🚦 status_code

The status_code function retrieves the HTTP status code from the URL, giving you an indication of the webpage’s health. Common status codes include:
 • 200 OK: The page is working fine.
 • 404 Not Found: The page doesn’t exist.
 • 500 Internal Server Error: There’s an issue with the server.

Example:

inspector.status_code()
# Output: "200 OK"

📑 headers

The headers function returns all HTTP headers associated with the URL. Headers contain important metadata such as content type, caching information, and server details. This information can help developers and webmasters diagnose issues or optimize the website’s performance.

Example:

inspector.headers()
# Output:
# {
#   "Content-Type": "text/html; charset=UTF-8",
#   "Server": "Apache",
#   "Cache-Control": "no-cache"
# }

🏷️ title

The title function extracts the <title> tag of the webpage, which appears in the browser’s tab and serves as a key SEO element. It’s essential for understanding the context of the page content at a glance.

Example:

inspector.title()
# Output: "Example Domain"

📝 meta

The meta function pulls all meta tags from the HTML source, such as the page description, keywords, and other metadata that affect search engine ranking and how the page is represented on social media.

Example:

inspector.meta()
# Output:
# {
#   "description": "This domain is for use in illustrative examples in documents.",
#   "keywords": "example, demo, test"
# }

🔗 link

The link function returns all internal and external links found on the webpage. This feature helps you analyze the structure of the page’s links, find broken or outdated URLs, and identify areas for improvement in terms of navigation and SEO.

Example:

inspector.links()
# Output:
# [
#   "https://example.com/about",
#   "https://example.com/contact",
#   "https://external-site.com"
# ]

🖥️ Example Usage

from urlinspector import URLInspector

# URL to inspect
url = "https://example.com"

# Initialize URLInspector with the URL
inspector = URLInspector(url)

# Retrieve and display the inspection data
print("Scan Date:", inspector.scan_date())   # 🗓️
print("Status Code:", inspector.status_code())  # 🚦
print("Headers:", inspector.headers())      # 📑
print("Title:", inspector.title())          # 🏷️
print("Meta:", inspector.meta())            # 📝
print("Links:", inspector.links())          # 🔗

Example Output:

Scan Date: 2024-11-12 10:00 AM
Status Code: 200 OK
Headers: 
{
  "Content-Type": "text/html; charset=UTF-8",
  "Server": "Apache",
  "Cache-Control": "no-cache"
}
Title: Example Domain
Meta: 
{
  "description": "This domain is for use in illustrative examples in documents.",
  "keywords": "example, demo, test"
}
Links: 
[
  "https://example.com/about",
  "https://example.com/contact",
  "https://external-site.com"
]

⚙️ Installation

To get started with URLInspector, you need to clone the repository and install the required dependencies. Here’s how to set it up:
 1. Clone the repository:

git clone https://github.com/Riotous-web/URLInspector.git


 2. Navigate to the project directory:

cd URLInspector


 3. Install dependencies:

pip3 install -r requirements.txt

💡 Why Use URLInspector?

 • SEO Optimization: Quickly check if a webpage’s title, meta tags, and headers are optimized for search engines.
 • Website Monitoring: Track the health and performance of websites by monitoring status codes, links, and headers.

 • Developer Debugging: Analyze headers and metadata to troubleshoot issues with web pages or servers.

🤝 Contributing

We welcome contributions to URLInspector! If you’d like to contribute, please follow these steps:
 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-branch).
 3. Commit your changes (git commit -am 'Add new feature').
 4. Push to the branch (git push origin feature-branch).
 5. Submit a pull request.

Let’s work together to make web inspection easier for everyone! 💪

📝 License

URLInspector is open-source software licensed under the MIT License.

Happy inspecting! 🌐🔍
