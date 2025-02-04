from bs4 import BeautifulSoup
import requests
from config.index import NEWS_API_KEY, NEWS_APP_END_POINT
import traceback



def scrape_article_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")  
        full_content = "\n".join([p.get_text() for p in paragraphs])

        return full_content if full_content else False
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        return False



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

        articles_with_full_content = []
        for article in news["articles"]:
            full_content = scrape_article_content(article["url"])
            articles_with_full_content.append({
                "url": article["url"],
                "description": full_content if full_content else article["description"]
            })
            
        return {"articles": articles_with_full_content, "totalResults": news["totalResults"]}
    
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        return {"error": 'Failed to fetch news', "status_code": 500}