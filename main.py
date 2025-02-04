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
            return jsonify({"message": "Search parameter is required!"}), 400
        
        #Fetch news
        news = fetch_news(page, pageSize, search)
        
        # do sentiment analysis
        if len(news) == 0:
            return jsonify({"message": "No News Found!"}), 404

        analysed_data = []
        for article in news:
            analysed_news_sentiment = analyse_sentiment(article['description'])
            analysed_data.append({
                "url": article["url"], 
                "sentiment": analysed_news_sentiment
            })
        
        #return the response
        return jsonify({
            "message": "Search Successfully",
            "data": analysed_data
        }), 200
    
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            "error": str(e),
            "message": traceback.format_exc()
        }), 500
    


if __name__ == "__main__":
    app.run(debug) 
