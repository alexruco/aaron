# main.py

from aaron.contact_page_finder import find_contact_page_url
from aaron.email_extractor import extract_emails_from_page, extract_emails_from_multiple_pages

def get_emails_from_website(base_url, max_crawl_pages=10):
    # Step 1: Try finding the contact page and extracting emails
    contact_page_url = find_contact_page_url(base_url)
    if contact_page_url:
        print(f"Contact page found: {contact_page_url}")
        emails = extract_emails_from_page(contact_page_url)
    else:
        print("No contact page found. Checking main page...")
        emails = extract_emails_from_page(base_url)

    # Step 2: If no emails were found, crawl additional pages
    if not emails:
        print(f"No emails found on the contact page or main page. Crawling up to {max_crawl_pages} pages...")
        emails = extract_emails_from_multiple_pages(base_url, num_pages=max_crawl_pages)

    print(f"Extracted emails: {emails}")

# Test the function
if __name__ == "__main__":
    base_url = "https://360casas.com"  # Replace with the target website URL
    get_emails_from_website(base_url, max_crawl_pages=10)