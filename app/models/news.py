class NEWS:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,name,description,Url,country):
        self.id =id
        self.name = name
        self.description = description
        self.Url = Url
        self.country = country

class ARTICLES:
    '''
    NEWS class to define NEWS Objects
    '''

    def __init__(self,id,author,description,Url,urlToImage):
        self.id =id
        self.author = author
        self.description = description
        self.Url = Url
        self.urlToImage = urlToImage          