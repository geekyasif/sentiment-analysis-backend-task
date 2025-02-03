from flask import Flask, jsonify, request
from config.index import debug
from services import fetch_news, analyse_news_sentiment
from dummy import data

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def search_news():
    try: 
        body = request.json
        search = body['search']
        if not search: 
            return jsonify({"message": "Search parameter is required!"}), 400
        #Fetch news
        # news = fetch_news(search)
        # print(news)
        # do sentiment analysis
        analysed_data = []
        for new in data:
            analysed_news_sentiment = analyse_news_sentiment(new['content'])
            analysed_data.append({"url": new["url"], "sentiment": analysed_news_sentiment})
            
        #return the response
        return jsonify({
            "message": "Search Successfully",
            "data": analysed_data
        }), 200
    except Exception as e:
        print(str(e))
        return jsonify({
            "error": str(e),
            "message": "Something went wrong"
        }), 500
    


if __name__ == "__main__":
    app.run(debug)  # Enables auto-restart on code changes
