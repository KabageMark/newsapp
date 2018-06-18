from .request import get_source
from flask import render_template,request,redirect,url_for
from app import app
                  
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    # title_news = get_news(title)
    source_news = get_source('sports')
    print(source_news)
    # image_news = get_news('image')
    # description_news = get_news('description')
    # url_news = get_news('url')
    
    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('index.html', title = title,sports = source_news) #image = image_news, description = description_news url=url_news)
    