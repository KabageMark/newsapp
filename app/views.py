from .request import get_source
from .request import get_articles
from flask import render_template,request,redirect,url_for
from app import app
                  
@app.route('/')
def sources():

    '''
    View root page function that returns the index page and its data
    '''
    
    source_news_general = get_source('general')
    source_news_url = get_source('Url')
    print(source_news_general)
    print(source_news_url)
    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('sources.html', title = title,general = source_news_general,Url = source_news_url) #image = image_news, description = description_news url=url_news)

# @app.route('/')
# def sources():


#     '''
#     View root page function that returns the index page and its data
#     '''
#     articles_news_general = get_articles('general')
#     articles_news_author=get_articles('author')
#     articles_news_description=get_articles('description')
#     articles_news_urlToImage=get_articles('urlToImage')
#     print(articles_news_general)
#     print(articles_news_author)
#     print(articles_news_description)
#     print(articles_news_urlToImage)
#     title = 'Home - Welcome to The best Movie Review Website Online'

#     return render_template('sources.html', title = title,general = articles_news_general,author = articles_news_author,description = articles_news_description, image = articles_news_urlToImage) #image = image_news, description = description_news url=url_news)    
    
