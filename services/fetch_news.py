import requests
from config.index import NEWS_API_KEY, NEWS_APP_END_POINT
import traceback

def fetch_news(page = 1, pageSize = 10, search=""):
    try: 
        params = {
            "q": search,
            "apiKey": NEWS_API_KEY,
            "pageSize": int(pageSize),
            "page": int(page),
        }

        url = f'{NEWS_APP_END_POINT}/everything'
        res = requests.get(url, params=params)

        if res.status_code != 200:
            return {"error": "Failed to fetch news", "status_code": res.status_code}
        news  = res.json()

        return news['articles']
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        return {"error": 'Failed to fetch news', "status_code": 500}