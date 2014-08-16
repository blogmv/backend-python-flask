from flask import Flask, request, escape
from google.appengine.ext import ndb
from models import Article, Comment
from json_serializer import JSONEncoder
import json

app = Flask(__name__)


def serialize(result):
    if not result and not isinstance(result, list):
        return "", 404, {"Content-Type": "application/json"}
    return json.dumps(result, cls=JSONEncoder), 200, {"Content-Type": "application/json"}

@app.route("/api/articles/", methods=['GET'])
def getArticles():
	return serialize(list(Article.query().fetch(10)))

@app.route("/api/articles/<int:article_id>/", methods=['GET'])
def getArticle(article_id):
	return serialize(Article.get_by_id(article_id))

@app.route("/api/articles/<int:article_id>/comments/", methods=['GET'])
def getComments(article_id):
	if not Article.get_by_id(article_id):
		return "", 404, {"Content-Type": "application/json"}
	return serialize(list(Comment.query(Comment.article == ndb.Key(Article, article_id)).fetch(10)))

@app.route("/api/articles/<int:article_id>/comments/<int:comment_id>/", methods=['GET'])
def getComment(article_id, comment_id):
	return serialize(
		Comment.query(
			ndb.AND(
				Comment.article == ndb.Key(Article, article_id),
				Comment.key == ndb.Key(Comment, comment_id)
			)
		).get()
	)

@app.route("/api/articles/<int:article_id>/comments/", methods=['POST'])
def postComment(article_id):
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
	comments = Comment.query().order(Comment.key).fetch(keys_only=True)
	if len(comments) > 10:
		comments[0].delete()
	return serialize(comment)

articles = Article.query().fetch(keys_only=True)
if len(articles) == 0:
	hello = Article()
	hello.title = "Hello World"
	hello.content = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur, voluptatum. Provident accusamus sit, commodi corrupti illo, veniam possimus minima rerum itaque. Magni, beatae, facere."
	hello.put()
	bye = Article()
	bye.title = "Bye World"
	bye.content = "Iraqi PM Nouri Maliki steps aside, ending political deadlock in Baghdad as the government struggles against insurgents in the north."
	bye.put()
	del hello, bye, articles
if __name__ == "__main__":
	app.run()