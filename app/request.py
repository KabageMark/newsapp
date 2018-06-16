from app import app
import urllib.request,json
from .models import news
News = news.NEWS

# Getting api key
api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_news(news_results_list)


    return news_results

    def process_news(news_list):
      '''
       Function  that processes the news result and transform them to a list of Objects

         Args:
        news_list: A list of dictionaries that contain movie details

         Returns :
        news_results: A list of news objects
       '''
    news_results = []
    for news_item in news_results:
        id = news_item.get('id')
        title = news_item.get('title')
        source = news_item.get('source')
        image = news_item.get('image')
        Url = news_item.get('Url')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')

        if source:
            news_object = News(id,title,source,image,description,publishedAt,Url)
            news_results.append(news_object)

    return news_results
