URLInspector - README

Welcome to URLInspector! 🌐🔍 This powerful tool allows you to analyze and inspect various aspects of any given URL. Whether you’re a web developer, SEO enthusiast, or simply curious about a webpage, URLInspector provides key insights into the status and structure of a website.

Features

URLInspector offers several features to help you assess the health and structure of any webpage. Below are the core functions provided by the tool:

🗓️ scan_date

The scan_date function records the exact date and time when the URL was scanned. This helps keep track of when the webpage data was last checked, ensuring that you’re always working with the most current information.

Example:

Scan Date: 2024-11-12 10:00 AM

🚦 status_code

The status_code function retrieves the HTTP status code from the website’s server. It tells you the state of the webpage — whether it’s accessible, down, or if there’s an error.
 • 200 OK: The page is successfully loaded.
 • 404 Not Found: The page could not be found.
 • 500 Internal Server Error: There’s an issue with the server.

Example:

Status Code: 200 OK

📑 headers

The headers function fetches the HTTP headers sent by the server when the webpage is requested. HTTP headers include useful information such as the content type, server, cache control, and more. Understanding headers is crucial for diagnosing web-related issues and ensuring optimal website performance.

Example:

Headers:
  - Content-Type: text/html; charset=UTF-8
  - Server: Apache
  - Cache-Control: no-cache

🏷️ title

The title function retrieves the title of the webpage from the HTML <title> tag. This is the title shown in the browser tab and is also crucial for SEO, as search engines use it to understand the content of a page.

Example:

Title: Example Domain

📝 meta

The meta function extracts the meta tags from the HTML <head> section. These tags contain metadata about the webpage, such as the description, keywords, and author. Meta tags are important for SEO and social media sharing.

Example:

Meta Description: This domain is for use in illustrative examples in documents.
Meta Keywords: example, domain, web, tutorial

🔗 link

The link function retrieves all the internal and external links found on the webpage. This allows you to identify the connections between pages within the same site or external resources linked from the page. It’s a great way to check for broken or dead links.

Example:

Links:
  - https://example.com/about
  - https://example.com/contact
  - https://external-site.com

Example Output

Here’s an example of what the output might look like when you run URLInspector on a website:

URL: https://example.com

📅 Scan Date: 2024-11-12 10:00 AM
🚦 Status Code: 200 OK
📑 Title: Example Domain
📝 Meta Description: This domain is for use in illustrative examples in documents.
🔗 Links:
  - https://example.com/about
  - https://example.com/contact
  - https://external-site.com

Installation

To install URLInspector, follow these simple steps:
 1. Clone the repository from GitHub.
 2. Install the required dependencies using pip.

git clone https://github.com/Riotous-web/URLInspector.git

cd URLInspector

pip3 install -r requirements.txt

Usage

After installation, you can use URLInspector via command line or in your Python project. Here’s how you can inspect a URL:

from urlinspector import URLInspector

# Initialize the inspector with a URL
url = "https://example.com"
inspector = URLInspector(url)

# Fetch details about the URL
print(inspector.scan_date())      # Shows scan date and time
print(inspector.status_code())    # Shows HTTP status code
print(inspector.headers())        # Displays HTTP headers
print(inspector.title())          # Displays page title
print(inspector.meta())           # Displays meta tags
print(inspector.links())          # Displays internal and external links

Example Output:

Scan Date: 2024-11-12 10:00 AM
Status Code: 200 OK
Title: Example Domain
Meta Description: This domain is for use in illustrative examples in documents.
Links:
  - https://example.com/about
  - https://example.com/contact
  - https://external-site.com

Contributing

We welcome contributions to enhance URLInspector! If you find any bugs or have suggestions for new features, feel free to fork the repository, make your changes, and submit a pull request. Together, we can improve this tool for everyone. 🚀

How to Contribute:

 1. Fork the repository
 2. Create a new branch
 3. Make your changes
 4. Submit a pull request with a description of what you’ve done

License

URLInspector is open-source and licensed under the MIT License. See the LICENSE file for more details.

Thank you for using URLInspector! 🚀 Happy inspecting! 👨‍💻👩‍💻
