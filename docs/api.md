# API Reference

## CNNNewsScraper Class

The main class for scraping CNN articles.

### Constructor

    CNNNewsScraper(base_url="https://www.cnn.com")

Parameters:
- base_url (str): The base URL of the CNN website. Defaults to "https://www.cnn.com"

### Methods

#### fetch_main_page()

Fetches the HTML content of the CNN main page.

Returns:
- str: The HTML content of the main page if successful
- None: If the request fails

Raises:
- requests.RequestException: If there is an issue with the network request

#### parse_main_page(html_content)

Parses the main page HTML to extract article links and titles.

Parameters:
- html_content (str): The HTML content of the main page

Returns:
- list: A list of dictionaries containing article titles and URLs
    - Each dictionary has keys:
        - 'title': The article title
        - 'url': The full URL to the article

#### fetch_article(article_info)

Fetches and parses a single article page to extract its content.

Parameters:
- article_info (dict): A dictionary containing:
    - 'title': The article title
    - 'url': The article URL

Returns:
- dict: A dictionary containing:
    - 'title': The article title
    - 'date': Publication date (format: "YYYY-MM-DD HH:MM:SS")
    - 'content': The full article text
    - 'url': The article URL
- None: If the article fetch fails

Raises:
- requests.RequestException: If there is an issue with the network request

#### get_main_page_articles()

Scrapes articles from the CNN main page using multithreading.

Returns:
- list: A list of dictionaries containing scraped articles' details
    - Each dictionary contains:
        - 'title': The article title
        - 'date': Publication date
        - 'content': The full article text
        - 'url': The article URL

## Response Objects

### Article Dictionary

The standard article dictionary contains:

    {
        'title': str,    # The article title
        'date': str,     # Publication date (YYYY-MM-DD HH:MM:SS)
        'content': str,  # The full article text
        'url': str      # The complete article URL
    }

## Error Handling

The scraper implements the following error handling:

1. Network Errors
   - Returns None on failed requests
   - Logs errors to console
   - Continues processing remaining articles

2. Parsing Errors
   - Provides fallback parsing methods
   - Returns partial data if available
   - Logs parsing failures

3. Rate Limiting
   - Uses session management
   - Implements user-agent spoofing
   - Handles timeout scenarios

## Performance Considerations

1. Multithreading
   - Uses ThreadPoolExecutor
   - Default max_workers: 10
   - Configurable through code

2. Session Management
   - Reuses connections
   - Maintains cookies
   - Implements connection pooling

3. Memory Usage
   - Streams responses
   - Processes articles incrementally
   - Cleans up resources automatically

## Best Practices

1. Error Handling:
   - Always wrap API calls in try-except blocks
   - Check return values for None
   - Implement appropriate timeouts

2. Rate Limiting:
   - Implement delays between requests
   - Monitor response headers
   - Respect robots.txt guidelines

3. Resource Management:
   - Close sessions when done
   - Process large datasets in chunks
   - Monitor memory usage

## Examples

See [Usage Examples](examples.md) for detailed code examples and patterns.