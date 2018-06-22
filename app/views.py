from .request import get_source
from .request import get_articles
from flask import render_template,request,redirect,url_for
from app import app
                  
@app.route('/')
def sources():

    '''
    View root page function that returns the index page and its data
    '''
    source_news_sports = get_source('sports')
    source_news_politics = get_source('general')
    print(source_news_sports)
    print(source_news_politics)
    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('sources.html', title = title,sports = source_news_sports,general = source_news_politics) #image = image_news, description = description_news url=url_news)

@app.route('/')
def articles():

    '''
    View root page function that returns the index page and its data
    '''
    articles_news_sports = get_articles('sports')
    articles_news_politics = get_articles('general')
    print(articles_news_sports)
    print(articles_news_politics)
    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('articles.html', title = title,sports = articles_news_sports,general = articles_news_politics) #image = image_news, description = description_news url=url_news)    
    