URLInspector - README

Welcome to URLInspector! 🔍 This powerful tool is designed to provide detailed insights into any URL, allowing you to analyze key elements of a website. Whether you’re a developer, SEO professional, or simply curious about a webpage, URLInspector is here to help you get the information you need quickly and efficiently.

Features 🛠️

🗓️ scan_date

The scan_date function returns the date and time when the URL was last inspected. It helps you keep track of when the website data was last fetched, which is especially important for ensuring that the information is up-to-date.

Example:

print(inspector.scan_date())  
# Output: 2024-11-12 10:00 AM

🚦 status_code

The status_code function provides the HTTP status code for the URL. This is a standard way of indicating the result of the server’s attempt to fulfill a request. Common codes include:
 • 200: Success ✅
 • 404: Not Found ❌
 • 500: Server Error 🔴

Example:

print(inspector.status_code())  
# Output: 200 OK

📑 headers

The headers function fetches the HTTP headers from the website, which contain essential information about the page, like the content type, server details, and caching settings. This is a valuable resource for web developers and SEO experts.

Example:

print(inspector.headers())  
# Output: 
# {
#   'Content-Type': 'text/html; charset=UTF-8',
#   'Server': 'Apache/2.4.41',
#   'Cache-Control': 'no-cache'
# }

🏷️ title

The title function retrieves the <title> tag from the webpage’s HTML. This tag defines the title of the webpage as it appears on the browser tab and is often used by search engines for ranking and display purposes.

Example:

print(inspector.title())  
# Output: Example Domain

📝 meta

The meta function extracts the metadata from the page’s HTML, including the meta description, keywords, and other SEO-related tags. Meta tags are crucial for search engines to understand the content and context of the page.

Example:

print(inspector.meta())  
# Output: 
# {
#   'description': 'This domain is for use in illustrative examples in documents.',
#   'keywords': 'example, domain, test'
# }

🔗 link

The link function collects all the internal and external hyperlinks on the webpage. This is useful for analyzing the structure of the site and for finding any broken or missing links.

Example:

print(inspector.links())  
# Output:
# [
#   'https://example.com/about',
#   'https://example.com/contact',
#   'https://external-site.com'
# ]

Example Output 📊

Here’s what the output might look like when you run URLInspector:

URL: https://example.com

🗓️ Scan Date: 2024-11-12 10:00 AM
🚦 Status Code: 200 OK
📑 Title: Example Domain
📝 Meta Description: This domain is for use in illustrative examples in documents.
🔗 Links:
  - https://example.com/about
  - https://example.com/contact
  - https://external-site.com

Installation 🚀

To get started with URLInspector, you can clone the repository and install the dependencies. Here’s how to do it:

git clone https://github.com/Riotous-web/URLInspector.git

cd URLInspector

pip3 install -r requirements.txt

Usage 📘

Once installed, you can use URLInspector in your Python project by importing it and calling the various functions.

Example usage:

from urlinspector import URLInspector

url = "https://example.com"
inspector = URLInspector(url)

print(inspector.scan_date())  # Outputs scan date
print(inspector.status_code())  # Outputs status code
print(inspector.headers())  # Outputs headers
print(inspector.title())  # Outputs title tag
print(inspector.meta())  # Outputs meta data
print(inspector.links())  # Outputs list of links

Contributing 🤝

We welcome contributions to improve URLInspector! If you’d like to contribute:
 1. Fork the repository
 2. Create a new branch (git checkout -b feature-name)
 3. Make your changes
 4. Commit your changes (git commit -am 'Add new feature')
 5. Push to your branch (git push origin feature-name)
 6. Open a Pull Request

License 📄

URLInspector is open-source software licensed under the MIT License. Feel free to modify and share!

Support 🛠️

If you have any issues, questions, or suggestions, feel free to open an issue in the GitHub repository or contact the maintainers.

Happy inspecting! 🌐🕵️‍♀️
