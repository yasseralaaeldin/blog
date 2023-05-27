from flask import Flask
from blog.models.sqlalchemy import db
from blog.api.posts import posts
from blog.api.comments import comments

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)
app.register_blueprint(posts)
app.register_blueprint(comments)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
	app.run(debug=True)
        