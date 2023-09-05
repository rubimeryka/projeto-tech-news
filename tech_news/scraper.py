import requests
import time
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_url = selector.css(".nav-links a.next::attr(href)").get()
    return next_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").re_first(r"\d+")
        )
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    category = selector.css(".category-style .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": "".join(summary).strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    links = []

    while amount > len(links):
        html_content = fetch(url)
        if not html_content:
            break
        links.extend(scrape_updates(html_content))
        url = scrape_next_page_link(html_content)

    links_content = []

    for link in links:
        news = scrape_news(fetch(link))
        links_content.append(news)

    create_news(links_content[:amount])

    return links_content[:amount]
