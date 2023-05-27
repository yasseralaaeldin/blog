from flask import jsonify, request
from flask import Blueprint
from blog.models.post import Post
from blog.models.sqlalchemy import db


posts = Blueprint('posts', __name__)

@posts.route('/posts/')
def get_posts():
    posts = Post.query.all()
    posts_json = []
    for post in posts:
        posts_json.append(post.to_json())
    return jsonify({'posts': posts_json})

@posts.route('/posts/<id>/')
def get_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'error': 'Post not found'})
    return jsonify({'post': post.to_json()})

@posts.route('/posts/', methods=['POST'])
def create_post():
    data = request.get_json()

    if data['title'] == '':
        return jsonify({'error': 'Title is required.'}), 400
    
    if data['content'] == '':
        return jsonify({'error': 'Content is required.'}), 400
    
    post = Post(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'post': post.to_json()}), 201

@posts.route('/posts/<id>/', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = Post.query.get(id)
    if not post:
        return jsonify({'error': 'Post not found'})
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'post': post.to_json()})

@posts.route('/posts/<id>/', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({'error': 'Post not found'})
    db.session.delete(post)
    db.session.commit()
    return jsonify({'success': True})