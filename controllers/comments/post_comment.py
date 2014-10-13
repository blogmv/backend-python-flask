from domain.article import Article
from domain.comment import Comment
from google.appengine.ext import ndb
from services.serialize import serialize


__author__ = 'fernando'

def post_comment(article_id):
    article = Article.get_by_id(article_id)
    if not article:
        return "", 404, {"Content-Type": "application/json"}
    data = request.get_json()
    if not data:
        return "Missing data", 400
    comment = Comment()
    comment.article = article.key
    comment.author_name = escape(data.get("author_name"))
    comment.author_email = escape(data.get("author_email"))
    comment.content = escape(data.get("content"))
    comment.put()
    comments = Comment.query().order(Comment.date).fetch(keys_only=True)
    if len(comments) >= 10:
        comments[0].delete()
    return serialize(comment)