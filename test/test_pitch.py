import unittest
from app.models import Comment, User, Post
from app import db


class PostTest(unittest.TestCase):
    def setUp(self):
        self.user_test = User(username='test9', email='test9@gmail.com', password='testpass')
    
        self.new_post = Post(post_category='til', post_title='test',post_text='test post', user='test')
    
    def tearDown(self):        
        Post.query.delete()
        User.query.delete()
    
    def test_get_post_by_category(self):
        self.new_post.save_post()
        got_posts = Post.get_posts('til')
        self.assertTrue(len(got_posts)==1) 
