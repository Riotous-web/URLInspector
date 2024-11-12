import requests
from bs4 import BeautifulSoup
import json
import argparse
from datetime import datetime


def scan_website(url):
    """Scan the given website for useful data and return the results in JSON format."""

    scan_results = {
        "url": url,
        "scan_date": str(datetime.now()),
        "status_code": None,
        "headers": {},
        "title": "",
        "meta": {},
        "links": []
    }

    try:
        # Send a request to the URL
        response = requests.get(url, timeout=10)
        scan_results["status_code"] = response.status_code
        scan_results["headers"] = dict(response.headers)

        # Parse the content if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Get title
            if soup.title:
                scan_results["title"] = soup.title.string

            # Get meta tags
            meta_tags = soup.find_all('meta')
            for meta in meta_tags:
                if meta.get("name"):
                    scan_results["meta"][meta.get("name")] = meta.get("content")

            # Get all links
            for link in soup.find_all('a', href=True):
                scan_results["links"].append(link['href'])

    except requests.exceptions.RequestException as e:
        scan_results["error"] = f"An error occurred: {e}"

    return scan_results


def save_results_to_json(data, filename="scan_results.json"):
    """Save the scan results to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Results saved to {filename}")


def display_help():
    """Display help message for the tool."""
    help_message = """
SiteSleuth Tool
--------------------

Usage:
    python3 webinspector.py -u <URL> [-o <OUTPUT_FILE>] [OPTIONS]

Options:
    -u, --url         URL of the website to scan (required).
    -o, --output      Output JSON file to save the scan results.
    -a, --author      Display information about the tool's author.
    -v, --version     Show the version of the tool.
    -h, --help        Show this help message.

Example:
    python3 webinspector.py -u https://example.com -o results.json
    """
    print(help_message)


def display_author():
    """Display author information."""
    print("SiteSleuth Tool\nAuthor: Vex\nContact: vex@fortinet.com")


def main():
    parser = argparse.ArgumentParser(add_help=False)

    # Define arguments
    parser.add_argument("-u", "--url", type=str, help="URL of the website to scan")
    parser.add_argument("-o", "--output", type=str, default="scan_results.json",
                        help="Output JSON file to save the scan results")
    parser.add_argument("-a", "--author", action="store_true", help="Show author information")
    parser.add_argument("-v", "--version", action="version", version="SitteSleuth Tool 1.0",
                        help="Show tool version")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")

    # Parse arguments
    args = parser.parse_args()

    if args.help:
        display_help()
        return

    if args.author:
        display_author()
        return

    if not args.url:
        print("Error: The URL parameter (-u or --url) is required.")
        display_help()
        return

    # Run the website scan
    print(f"Scanning website: {args.url}")
    results = scan_website(args.url)

    # Save results to JSON
    save_results_to_json(results, args.output)

    # Print results to console
    print("\nScan Results:")
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
