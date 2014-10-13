from controllers.base import Controller
from domain.article import Article
from domain.comment import Comment
from google.appengine.ext import ndb
from services.serialize import serialize

__author__ = 'fernando'

class GetCommentsController(Controller):
    __slots__ = ["serializer", "comment_repository"]

    def __init__(self, request, serializer, comment_repository):
        super(GetCommentsController, self).__init__(request)
        self.serializer = serializer
        self.comment_repository = comment_repository

    def __call__(self, *args, **kwargs):
        return self.serializer.encode(
            self.comment_repository.find_by_article_key_ordered_by_date(
                10,
                article_id
            )
        )