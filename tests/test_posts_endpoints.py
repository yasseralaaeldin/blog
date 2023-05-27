import json
import unittest
from app import app
from blog.models.sqlalchemy import db

class TestPostsEndpoints(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_post_with_valid_data(self):
        data = {'title': 'This is a post.', 'content': 'This is the content of the post.'}
        response = self.app.post('/posts/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        post = response.json['post']
        self.assertIsNotNone(post)
        self.assertIsInstance(post, dict)
        self.assertEqual(post['title'], 'This is a post.')
        self.assertEqual(post['content'], 'This is the content of the post.')

    def test_create_post_with_empty_title(self):
        data = {'title': '', 'content': 'This is the content of the post.'}
        response = self.app.post('/posts/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        error = response.json['error']
        self.assertIsNotNone(error)
        self.assertEqual(error, 'Title is required.')

    def test_create_post_with_empty_content(self):
        data = {'title': 'This is a post.', 'content': ''}
        response = self.app.post('/posts/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        error = response.json['error']
        self.assertIsNotNone(error)
        self.assertEqual(error, 'Content is required.')


    def test_get_posts(self):
        response = self.app.get('/posts/')
        self.assertEqual(response.status_code, 200)
        posts = response.json['posts']
        self.assertIsNotNone(posts)
        self.assertIsInstance(posts, list)