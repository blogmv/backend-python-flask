from flask.blueprints import Blueprint
from controllers.comments.get_comment import GetCommentController
from controllers.comments.get_comments import get_comments
from controllers.comments.post_comment import post_comment

__author__ = 'fernando'

comments = Blueprint(__name__)

comments.add_url_rule("/api/articles/<int:article_id>/comments/", view_func=get_comments, methods=['GET'])

comments.add_url_rule("/api/articles/<int:article_id>/comments/<int:comment_id>/", view_func=GetCommentController, methods=['GET'])

comments.add_url_rule("/api/articles/<int:article_id>/comments/", view_func=post_comment, methods=['POST'])