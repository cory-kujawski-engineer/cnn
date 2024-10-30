# Usage Examples

## Basic Usage

### Scraping All Articles from Main Page

    from cnn_scraper import CNNNewsScraper
    
    # Create a scraper instance
    scraper = CNNNewsScraper()
    
    # Get all articles from the main page
    articles = scraper.get_main_page_articles()
    
    # Print article details
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"URL: {article['url']}")
        print("---")

### Working with Article Content

    # Get articles and process their content
    articles = scraper.get_main_page_articles()
    
    for article in articles:
        # Print first 200 characters of content
        print(f"Title: {article['title']}")
        print(f"Preview: {article['content'][:200]}...")
        print("---")

## Advanced Usage

### Custom Base URL

    # Use a different CNN domain or subdomain
    scraper = CNNNewsScraper(base_url="https://edition.cnn.com")
    articles = scraper.get_main_page_articles()

### Error Handling

    try:
        scraper = CNNNewsScraper()
        articles = scraper.get_main_page_articles()
        if not articles:
            print("No articles found")
    except Exception as e:
        print(f"An error occurred: {e}")

### Saving Results

    import json
    
    # Get articles
    scraper = CNNNewsScraper()
    articles = scraper.get_main_page_articles()
    
    # Save to JSON file
    with open('cnn_articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

### Processing Specific Articles

    scraper = CNNNewsScraper()
    
    # Get article URLs from main page
    html_content = scraper.fetch_main_page()
    article_list = scraper.parse_main_page(html_content)
    
    # Process only the first 5 articles
    for article in article_list[:5]:
        full_article = scraper.fetch_article(article)
        if full_article:
            print(f"Processed: {full_article['title']}")

## Performance Tips

1. The scraper uses multithreading by default for better performance
2. Adjust the number of worker threads in ThreadPoolExecutor for your needs
3. Consider implementing delays between requests for respectful scraping
4. Use session management for better performance over multiple requests

## Best Practices

1. Always check the robots.txt file before scraping
2. Implement proper error handling
3. Use appropriate delays between requests
4. Save your data incrementally
5. Respect CNN's terms of service and robots.txt guidelines

## Common Patterns

### Filtering Articles

    # Get articles and filter by keyword
    articles = scraper.get_main_page_articles()
    tech_articles = [
        article for article in articles
        if any(keyword in article['title'].lower() 
               for keyword in ['tech', 'technology', 'digital'])
    ]

### Date-based Processing

    from datetime import datetime
    
    articles = scraper.get_main_page_articles()
    
    # Process only today's articles
    today = datetime.now().strftime("%Y-%m-%d")
    todays_articles = [
        article for article in articles
        if article['date'].startswith(today)
    ]

### Content Analysis

    import re
    
    articles = scraper.get_main_page_articles()
    
    # Find articles mentioning specific terms
    pattern = re.compile(r'artificial intelligence|AI|machine learning', re.IGNORECASE)
    ai_articles = [
        article for article in articles
        if pattern.search(article['content'])
    ]