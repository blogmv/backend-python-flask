from google.appengine.ext import ndb
from json_serializer import JSONSerializable

class Article(ndb.Model, JSONSerializable):
	title = ndb.StringProperty(indexed=False)
	content = ndb.StringProperty(indexed=False)

	@property
	def id(self):
		return self.key.integer_id()

	def toJSON(self):
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content
		}

class Comment(ndb.Model, JSONSerializable):
	article = ndb.KeyProperty(kind=Article, indexed=True)
	author_name = ndb.StringProperty(indexed=False)
	author_email = ndb.StringProperty(indexed=False)
	content = ndb.StringProperty(indexed=False)

	@property
	def id(self):
		return self.key.integer_id()

	def toJSON(self):
		return {
			"id": self.id,
			"author_name": self.author_name,
			"author_email": self.author_email,
			"content": self.content
		}