# email_extractor_with_button_check.py

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_contact_page_url(base_url):
    """Finds the contact page URL from the base page, including buttons with specific texts."""
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Keywords for common contact-related pages and specific button text
        contact_keywords = ['contact', 'about', 'support', 'get-started']
        button_texts = ['start now']  # Specific text on buttons that link to contact

        # Check links
        for link in soup.find_all('a', href=True):
            href = link['href'].lower()
            if any(keyword in href for keyword in contact_keywords):
                contact_url = urljoin(base_url, link['href'])
                return contact_url

        # Check buttons
        for button in soup.find_all(['a', 'button']):
            button_text = button.get_text(strip=True).lower()
            if button_text in button_texts:
                contact_url = urljoin(base_url, button.get('href'))
                return contact_url

        return None
    except requests.RequestException as e:
        print(f"Error accessing {base_url}: {e}")
        return None

def extract_emails_from_website(url):
    """Extracts email addresses from the specified URL content."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        page_content = response.text
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

    soup = BeautifulSoup(page_content, 'html.parser')
    text_content = soup.get_text()

    # Regex pattern for finding email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text_content)

    # Removing duplicates by converting to a set
    return list(set(emails))

# Main function to find contact page and extract emails
def main(base_url):
    contact_page_url = find_contact_page_url(base_url)
    if contact_page_url:
        print(f"Contact page found: {contact_page_url}")
        emails = extract_emails_from_website(contact_page_url)
        print(f"Extracted emails from {contact_page_url}: {emails}")
    else:
        print("No contact page found.")
        # Optionally, extract emails from the main page if contact page is not found
        emails = extract_emails_from_website(base_url)
        print(f"Extracted emails from {base_url}: {emails}")

# Test the function
base_url = "https://mysitefaster.com"  # Replace with the target website URL
main(base_url)