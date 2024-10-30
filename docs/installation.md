# Installation Guide

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation Methods

### 1. Using pip

    pip install -r requirements.txt

### 2. Using setup.py

    python setup.py install

## Manual Installation

If you prefer to install dependencies manually, you can install the following required packages:

    pip install beautifulsoup4==4.12.3
    pip install requests==2.32.3
    pip install lxml==5.3.0
    pip install html5lib==1.1

## Virtual Environment (Recommended)

It's recommended to install the package in a virtual environment:

    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On Unix or MacOS:
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

## Verification

To verify the installation, run the following in Python:

    from cnn_scraper import CNNNewsScraper

    # Create an instance
    scraper = CNNNewsScraper()

    # Test the scraper
    articles = scraper.get_main_page_articles()
    if articles:
        print("Installation successful!")

## Troubleshooting

### Common Issues

1. **SSL Certificate Errors**
   - Update your certificates: `pip install --upgrade certifi`
   - Or install requests with security extras: `pip install requests[security]`

2. **Permission Errors**
   - Try installing with user permissions: `pip install --user -r requirements.txt`
   - Or use sudo (Linux/Mac): `sudo pip install -r requirements.txt`

3. **Missing Dependencies**
   - Install build tools:
     - Windows: Install Visual C++ build tools
     - Linux: `sudo apt-get install python3-dev build-essential`
     - Mac: Install Xcode Command Line Tools

### Getting Help

If you encounter any issues during installation:

1. Check the [GitHub Issues](https://github.com/cory-kujawski-engineer/cnn_scraper/issues)
2. Create a new issue with:
   - Your Python version
   - Your operating system
   - The complete error message
   - Steps to reproduce the error

## Next Steps

After installation, check out the [Usage Examples](examples.md) to get started with the scraper.