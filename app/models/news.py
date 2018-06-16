class NEWS:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,title,source,image,description,publishedAt,Url):
        self.id =id
        self.title = title
        self.image = 'https://ichef.bbci.co.uk/news/1024/branded_news/7CB7/production/_102072913_p06b7tjm.jpg'+image
        self.description = description
        self.publishedAt = publishedAt
        Url = Url