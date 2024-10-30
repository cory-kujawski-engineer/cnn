import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


class CNNNewsScraper:
    def __init__(self, base_url="https://www.cnn.com"):
        """
        Initializes the CNNNewsScraper with a base URL and a requests session.

        Args:
            base_url (str): The base URL of the CNN website. Defaults to "https://www.cnn.com".
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
            }
        )

    def fetch_main_page(self):
        """
        Fetches the HTML content of the CNN main page.

        Returns:
            str: The HTML content of the main page if successful, None otherwise.

        Raises:
            requests.RequestException: If there is an issue with the network request.
        """
        try:
            start_time = time.time()
            print("Fetching main page...")
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()
            fetch_time = time.time() - start_time
            print(f"Collected main page. Fetch time: {fetch_time:.2f} seconds")
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching CNN main page: {e}")
            return None

    def parse_main_page(self, html_content):
        """
        Parses the main page HTML to extract article links and titles.

        Args:
            html_content (str): The HTML content of the main page.

        Returns:
            list: A list of dictionaries containing article titles and URLs.

        Raises:
            None
        """
        parse_start = time.time()
        soup = BeautifulSoup(html_content, "html.parser")
        articles = []

        print("Parsing main page for articles...")
        article_pattern = re.compile(r"/\d{4}/\d{2}/\d{2}/")

        for link in soup.find_all("a", href=True):
            article_url = link.get("href")
            title = link.get_text(strip=True)

            if "Video" in title or "Gallery" in title:
                continue

            if article_url and article_pattern.search(article_url):
                if article_url.startswith("/"):
                    article_url = f"{self.base_url}{article_url}"

                if title:
                    articles.append({"title": title, "url": article_url})

        unique_articles = {article["url"]: article for article in articles}.values()

        parse_time = time.time() - parse_start
        print(f"Parse time for main page: {parse_time:.2f} seconds")
        print(f"Found {len(unique_articles)} unique articles on the main page.")
        return list(unique_articles)

    def fetch_article(self, article_info):
        """
        Fetches and parses a single article page to extract its content.

        Args:
            article_info (dict): A dictionary containing the article's title and URL.

        Returns:
            dict: A dictionary containing the article's title, date, content, and URL.

        Raises:
            requests.RequestException: If there is an issue with the network request.
        """
        url = article_info["url"]
        try:
            fetch_start = time.time()
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            fetch_time = time.time() - fetch_start
            print(
                f"Fetched article: {article_info['title']} in {fetch_time:.2f} seconds"
            )

            parse_start = time.time()
            soup = BeautifulSoup(response.text, "html.parser")

            title_tag = soup.find("h1")
            title = title_tag.text.strip() if title_tag else article_info["title"]

            date_tag = soup.find("div", class_="timestamp vossi-timestamp")
            date_str = date_tag.text.strip() if date_tag else None
            try:
                date = (
                    datetime.strptime(
                        date_str, "Updated %I:%M %p %Z, %a %B %d, %Y"
                    ).strftime("%Y-%m-%d %H:%M:%S")
                    if date_str
                    else "No Date Found"
                )
            except (ValueError, TypeError):
                date = "No Date Found"

            paragraphs = soup.find_all(
                "div", class_="paragraph__content"
            ) or soup.find_all("p")
            content = (
                "\n".join(p.get_text(strip=True) for p in paragraphs)
                if paragraphs
                else "No Content Found"
            )
            content = content.replace("Follow:", "").strip()

            parse_time = time.time() - parse_start
            print(f"Parsed article: {title} in {parse_time:.2f} seconds")

            return {"title": title, "date": date, "content": content, "url": url}
        except requests.RequestException as e:
            print(f"Error fetching article: {e}")
            return None

    def get_main_page_articles(self):
        """
        Scrapes articles from the CNN main page using multithreading.

        Returns:
            list: A list of dictionaries containing the scraped articles' details.

        Raises:
            None
        """
        html_content = self.fetch_main_page()
        if html_content:
            articles = self.parse_main_page(html_content)
            if articles:
                print(f"Starting threaded download of {len(articles)} articles...")

                results = []
                with ThreadPoolExecutor(max_workers=10) as executor:
                    future_to_article = {
                        executor.submit(self.fetch_article, article): article
                        for article in articles
                    }
                    for future in as_completed(future_to_article):
                        result = future.result()
                        if result:
                            results.append(result)

                print(f"Successfully retrieved {len(results)} articles.")
                return results
            else:
                print("No articles were found on the main page.")
                return []
        else:
            print("Failed to retrieve main page articles.")
            return []


if __name__ == "__main__":
    scraper = CNNNewsScraper()
    total_start = time.time()
    articles = scraper.get_main_page_articles()
    total_time = time.time() - total_start
    print(f"Total scraping time: {total_time:.2f} seconds")
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"Content: {article['content'][:300]}...")
        print(f"URL: {article['url']}\n")
