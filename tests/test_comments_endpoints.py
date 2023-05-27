import json
import unittest
from app import app

class TestCommentsEndpoints(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_create_comment_with_valid_data(self):
        data = {'content': 'This is a comment.'}
        response = self.app.post('/posts/2/comments/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        comment = response.json['comment']
        self.assertEqual(comment['post_id'], 2)
        self.assertEqual(comment['content'], 'This is a comment.')

    def test_create_comment_with_invalid_data(self):
        data = {'content': ''}
        response = self.app.post('posts/2/comments/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid comment data.')

    def test_get_comments(self):
        response = self.app.get('/posts/2/comments/')
        self.assertEqual(response.status_code, 200)
        comments = response.json['comments']
        self.assertIsNotNone(comments)
        self.assertIsInstance(comments, list)

    def test_create_comment(self):
        data = {'content': 'This is a comment.'}
        response = self.app.post('/posts/2/comments/', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)
        comment = response.json['comment']
        self.assertIsNotNone(comment)
        self.assertIsInstance(comment, dict)
        self.assertEqual(comment['content'], 'This is a comment.')