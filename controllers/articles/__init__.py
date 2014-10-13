from flask.blueprints import Blueprint
from controllers.articles.get_article import get_article
from controllers.articles.get_articles import get_articles

__author__ = 'fernando'

articles = Blueprint(__name__)
articles.add_url_rule("articles/", view_func=get_articles, methods=['GET'])
articles.add_url_rule("articles/<int:article_id>/", view_func=get_article, methods=['GET'])