# crawler.py

import os
from bertha import crawl_website  # Importing crawl_website from Bertha

# Define the path to the database file in the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root of the project
DATABASE_PATH = os.path.join(ROOT_DIR, "db_websites.db")

def crawl_internal_pages(base_url):
    """Wrapper for crawling internal pages with bertha's crawl_website."""
    internal_urls = crawl_website(base_url)
    delete_database()  # Delete the database after use
    return internal_urls

def delete_database():
    """Deletes the db_websites.db file if it exists."""
    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)
        print(f"Deleted temporary database file: {DATABASE_PATH}")
    else:
        print(f"No database file found at: {DATABASE_PATH}")