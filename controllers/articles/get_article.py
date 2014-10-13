from domain.article import Article
from services.serialize import serialize

__author__ = 'fernando'

def get_article(article_id):
    return serialize(Article.get_by_id(article_id))