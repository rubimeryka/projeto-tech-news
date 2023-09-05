from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    search_results = search_news({"title": {"$regex": title, "$options": "i"}})
    lis_of_news = [(news["title"], news["url"]) for news in search_results]
    return lis_of_news


# Requisito 8
def search_by_date(date):
    try:
        iso_format = datetime.strptime(date, "%Y-%m-%d")
        date_in_format = iso_format.strftime("%d/%m/%Y")
        search = search_news({"timestamp": {"$regex": date_in_format}})
        list_of_news = [(news["title"], news["url"]) for news in search]
        return list_of_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    list_of_news = [(news["title"], news["url"]) for news in search]
    return list_of_news
