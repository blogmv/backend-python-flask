from google.appengine.ext import ndb
from .article import Article
from services.serialize import JSONSerializable

__author__ = 'fernando'

class Comment(ndb.Model, JSONSerializable):
    article = ndb.KeyProperty(kind=Article, indexed=True)
    author_name = ndb.StringProperty(indexed=False)
    author_email = ndb.StringProperty(indexed=False)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

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