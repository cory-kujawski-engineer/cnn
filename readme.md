# CNN News Scraper

A robust Python web scraper designed to extract articles from CNN's website. This tool efficiently collects article titles, dates, content, and URLs using multithreaded operations.

## Features

- Scrapes CNN's main page for article links
- Extracts article content, titles, dates, and URLs
- Utilizes multithreading for efficient scraping
- Handles network errors gracefully
- User-agent spoofing to prevent blocking
- Automatic rate limiting and timeout handling

## Installation

Install using pip:

    pip install -r requirements.txt

Or install using setup.py:

    python setup.py install

## Quick Start

Basic usage example:

    from cnn_scraper import CNNNewsScraper
    
    scraper = CNNNewsScraper()
    articles = scraper.get_main_page_articles()
    
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Content: {article['content'][:300]}...")
        print(f"URL: {article['url']}\n")

## Documentation

- [Installation Guide](docs/installation.md)
- [API Reference](docs/api.md)
- [Usage Examples](docs/examples.md)

## Requirements

- Python 3.6+
- beautifulsoup4
- requests
- lxml
- html5lib

See requirements.txt for specific versions.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- CNN for providing the content
- BeautifulSoup4 for HTML parsing
- Requests library for HTTP operations

## Disclaimer

This tool is for educational purposes only. Please review CNN's terms of service and robots.txt before use. Ensure your scraping activities comply with CNN's policies and local regulations.

## Support

For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

## Project Status

Active development - Bug reports and feature requests welcome!
