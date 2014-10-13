from google.appengine.ext import ndb
from services.serialize import JSONSerializable

__author__ = 'fernando'

class Article(ndb.Model, JSONSerializable):
    title = ndb.StringProperty(indexed=False)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

    @property
    def id(self):
        return self.key.integer_id()

    def toJSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }