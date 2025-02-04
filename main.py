from flask import Flask, jsonify, request
from config.index import debug
from services import fetch_news, analyse_sentiment
import traceback

app = Flask(__name__)


@app.route("/news", methods=["GET"])
def news():
    try: 
        query = request.args
        page = query.get("page", 1)
        pageSize = query.get("pageSize", 10)
        search = query.get("search", "")
        
        if not search: 
            return jsonify({"success": False , "message": "Search parameter is required!"}), 400
        
        #Fetch news
        news = fetch_news(page, pageSize, search)

        if "error" in news:
            return jsonify({"success": False , "message": "Something went wrong while fetching the news!"}) , 500
        
        # do sentiment analysis
        if len(news['articles']) == 0 or news['totalResults'] == 0:
            return jsonify({"success": True, "message": "No News Found!", "data": {"articles": [], "total": 0}}), 200

        analysed_data = []

        for article in news['articles']:
        
            analysed_news_sentiment = analyse_sentiment(article['description'])
            if "error" in analysed_news_sentiment:
                analysed_news_sentiment = "Error"

            analysed_data.append({
                "url": article["url"], 
                "sentiment": analysed_news_sentiment
            })

        #return the response
        return jsonify({
            "success": True,
            "message": "Search News and Sentiment Analysis Successfully",
            "data": {
                    "articles": analysed_data,
                    "total": news['totalResults'],
                }
        }), 200
    
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            "error": str(e),
            "message": traceback.format_exc()
        }), 500
    


if __name__ == "__main__":
    app.run(debug) 
