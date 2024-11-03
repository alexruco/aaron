# Aaron: Email Extraction Module 🚀

Welcome to **AARON**! This project is designed to extract email addresses from websites, starting with main and contact pages and, if necessary, crawling additional pages to locate contact information.


## Features ✨

- **Email Extraction**: Extracts email addresses from a specified webpage, using advanced parsing to handle formatting issues. 📧
- **Contact Page Finder**: Automatically finds and navigates to contact pages on websites to retrieve email addresses efficiently. 🔍
- **Crawling Additional Pages**: If no email is found on main or contact pages, Aaron crawls through internal pages to locate contact information. 🌐

## Installation 💻

You can install the package via pip:

```bash
pip install git+https://github.com/alexruco/aaron.git@main#egg=aaron
```

## Usage 📚

Here's a quick example to get you started:
<!--
```python
from aaron import get_emails_from_website, extract_emails_from_page

# Use the get_emails_from_website function to search a website for emails
base_url = "https://www.example.com"
emails = get_emails_from_website(base_url, max_crawl_pages=10)
print(emails)

# Or use extract_emails_from_page for a single page
emails_from_page = extract_emails_from_page("https://www.example.com/contact")
print(emails_from_page)
```
-->

Running Tests 🧪

To run the tests, you can use the unittest module or pytest.

```bash

python -m unittest discover tests
# or
pytest
```

## Contributing 🤝

We welcome contributions from the community! Here’s how you can get involved:

1. **Report Bugs**: If you find a bug, please open an issue [here](https://github.com/alexruco/aaron/issues).
2. **Suggest Features**: We’d love to hear your ideas! Suggest new features by opening an issue.
3. **Submit Pull Requests**: Ready to contribute? Fork the repo, make your changes, and submit a pull request. Please ensure your code follows our coding standards and is well-documented.
4. **Improve Documentation**: Help us improve our documentation. Feel free to make edits or add new content.

### How to Submit a Pull Request

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request on the original repository.

## Why Aaron?

Aaron Montgomery Ward was an American entrepreneur based in Chicago who made his fortune through the use of mail order for retail sales of general merchandise to rural customers.  

## License 📄

This project is licensed under the MIT License. Feel free to use, modify, and distribute this software in accordance with the terms outlined in the [LICENSE](LICENSE) file.

