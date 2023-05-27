from flask import Blueprint, jsonify, request
from blog.models.comment import Comment
from blog.models.post import Post
from blog.models.sqlalchemy import db


comments = Blueprint('comments', __name__)

@comments.route('/posts/<post_id>/comments/')
def get_comments(post_id):
    
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'})
    
    comments = Comment.query.filter_by(post_id=post_id).all()
    
    comments_json = []
    for comment in comments:
        comments_json.append(comment.to_json())
        
    return jsonify({'comments': comments_json})

@comments.route('/posts/<post_id>/comments/', methods=['POST'])
def create_comment(post_id):
    data = request.get_json()

    post = Post.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'})
    
    if data['content'] == '':
        return jsonify({'error': 'Invalid comment data.'}), 400

    content = data['content']

    comment = Comment(post_id=post_id, content=content)

    db.session.add(comment)
    db.session.commit()

    return jsonify({'comment': comment.to_json()}), 201