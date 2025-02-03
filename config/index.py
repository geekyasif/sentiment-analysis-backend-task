import os
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_APP_API_KEY")
NEWS_APP_END_POINT = os.getenv("NEWS_APP_END_POINT")
debug=True