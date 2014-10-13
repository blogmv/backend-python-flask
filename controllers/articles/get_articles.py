from domain.article import Article
from google.appengine.ext import ndb
from services.serialize import serialize
__author__ = 'fernando'


def get_articles():
    articles = Article.query()
    if articles.count() == 0:
        hello = Article()
        hello.title = "Hello World"
        hello.content = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur, voluptatum." \
                        " Provident accusamus sit, commodi corrupti illo, veniam possimus minima rerum itaque." \
                        " Magni, beatae, facere."
        hello.put()
        bye = Article()
        bye.title = "Bye World"
        bye.content = "Iraqi PM Nouri Maliki steps aside, ending political deadlock in Baghdad as" \
                      " the government struggles against insurgents in the north."
        bye.put()
        del hello, bye
        articles = Article.query()
    return serialize(list(articles.order(Article.date).fetch(10)))