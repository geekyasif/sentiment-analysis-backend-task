import requests
from config.index import NEWS_API_KEY, NEWS_APP_END_POINT

def fetch_news(search):
    params = {
        "q": search,
        "apiKey": NEWS_API_KEY
    }
    url = f'{NEWS_APP_END_POINT}/everything'
    res = requests.get(url, params=params)
    
    if res.status_code != 200:
        return {"error": "Failed to fetch news", "status_code": res.status_code}
    news = res.json()
    # data = [{"url": new['url'], "content": new['content']} for new in news['articles']]  # Assuming 'articles' is the key in the response
    
    return news
