from blog.models.sqlalchemy import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at,
            'post_id': self.post_id
        }