# contact_page_finder.py

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