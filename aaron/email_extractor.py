# email_extractor.py

import re
import requests
from bs4 import BeautifulSoup
from crawler import crawl_website  # Importing bertha's crawl function from crawler module

def extract_emails_from_page(url):
    """Extracts email addresses from the specified URL content, handling common formatting issues."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        page_content = response.text
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Get all text content, replacing newlines with spaces to prevent word concatenation
    text_content = soup.get_text(separator=" ").replace("\n", " ")

    # Regex pattern for finding email addresses with word boundaries
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    emails = re.findall(email_pattern, text_content)

    # Removing duplicates by converting to a set
    return list(set(emails))
    # Removing duplicates by converting to a set
    return list(set(emails))
def extract_emails_from_multiple_pages(base_url, num_pages=10):
    """Crawls internal pages and attempts to extract emails from the first `num_pages` URLs found."""
    internal_urls = crawl_website(base_url)
    emails = set()

    # Limit to the first `num_pages` URLs
    for i, url in enumerate(internal_urls[:num_pages]):
        print(f"Checking page {i+1}: {url}")
        page_emails = extract_emails_from_page(url)
        emails.update(page_emails)
        if emails:
            break  # Stop if emails are found

    return list(emails)