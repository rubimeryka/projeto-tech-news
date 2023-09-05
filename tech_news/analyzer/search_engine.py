from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    search_results = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = [(news["title"], news["url"]) for news in search_results]
    return list_news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
