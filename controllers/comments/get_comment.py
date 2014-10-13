from controllers.base import Controller
from domain.article import Article
from domain.comment import Comment
from services.serialize import serialize

__author__ = 'fernando'


class GetCommentController(Controller):
    __slots__ = ["serializer", "comment_repository"]

    def __init__(self, request, serializer, comment_repository):
        super(GetCommentController, self).__init__(request)
        self.serializer = serializer
        self.comment_repository = comment_repository

    def __call__(self, *args, **kwargs):
        return self.serializer.encode(
            self.comment_repository.find_one_by_article_and_comment_key(
                article_id,
                comment_id
            )
        )