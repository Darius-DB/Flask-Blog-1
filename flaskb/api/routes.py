from flaskb import app
from flaskb.models import User, Post
from flask_restful import Api, Resource, abort, fields, marshal_with

api = Api(app)

user_resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'image_file':  fields.String
}

post_resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'date_created': fields.DateTime,
    'user_id': fields.Integer
}

class AllUsers(Resource):
    @marshal_with(user_resource_fields)
    def get(self):
        result = User.query.all()
        return result


class SingleUser(Resource):
    @marshal_with(user_resource_fields)
    def get(self, user_id):
        result = User.query.filter_by(id=user_id).first()
        return result


class AllPosts(Resource):
    @marshal_with(post_resource_fields)
    def get(self):
        result = Post.query.all()
        return result


class SinglePost(Resource):
    @marshal_with(post_resource_fields)
    def get(self, post_id):
        result = Post.query.filter_by(id=post_id).first()
        return result


api.add_resource(AllUsers, '/api/v1/resources/users/all')
api.add_resource(SingleUser, '/api/v1/resources/users/<int:user_id>')
api.add_resource(AllPosts, '/api/v1/resources/posts/all')
api.add_resource(SinglePost, '/api/v1/resources/posts/<int:post_id>')
