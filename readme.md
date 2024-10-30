# CNN News Scraper

A robust Python web scraper designed to extract articles from CNN's website. This tool efficiently collects article titles, dates, content, and URLs using multithreaded operations.

## Features

- Scrapes CNN's main page for article links
- Extracts article content, titles, dates, and URLs
- Utilizes multithreading for efficient scraping
- Handles network errors gracefully
- User-agent spoofing to prevent blocking
- Automatic rate limiting and timeout handling
- Command-line interface (CLI) with customizable options

## Installation

Install using pip:

    pip install -r requirements.txt

Or install using setup.py:

    python setup.py install

## Quick Start

### As a Module

Basic usage example:

    from cnn_scraper import CNNNewsScraper
    
    scraper = CNNNewsScraper()
    articles = scraper.get_main_page_articles()
    
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Content: {article['content'][:300]}...")
        print(f"URL: {article['url']}\n")

### Command Line Interface

Basic CLI usage:

    python cnn_scraper.py

With options:

    python cnn_scraper.py --threads 15 --content-preview all --output json

Available CLI options:
- `-t, --threads`: Number of threads (default: 10)
- `-u, --user-agent`: Custom user agent string
- `-c, --content-preview`: Content preview length (300, 500, 1000, or all)
- `-o, --output`: Output format (console or json)
- `-f, --file`: Output file name for JSON format

## Using as a Module

Import and use in your own Python projects:

    from cnn_scraper import CNNNewsScraper
    
    def my_news_function():
        scraper = CNNNewsScraper()
        articles = scraper.get_main_page_articles()
        return process_my_way(articles)

See the [API Reference](docs/api.md) for detailed integration examples.

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

## Acknowledgments

- CNN for providing the content
- BeautifulSoup4 for HTML parsing
- Requests library for HTTP operations
- Sake for endless hugs
- Acid for getting me Tacobell
- My dog pixel who has a UTI (poor baby)

## Disclaimer

This tool is for educational purposes only. Please review CNN's terms of service and robots.txt before use. Ensure your scraping activities comply with CNN's policies and local regulations.

## Support

For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

## Project Status

Active development - Bug reports and feature requests welcome!
