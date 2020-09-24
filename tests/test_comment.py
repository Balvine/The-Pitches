import unittest
from app.models import Comment, User, Post
from app import db


class CommentTest(unittest.TestCase):
        def setUp(self):
            self.user_test = User(username='test', email='test@gmail.com', password='testpass')
            self.new_post=Post(post_category='til', post_title='test', post_text='test post', user_id=1)
            self.new_comment=Comment(comment_text='test comment', post_id=1, user_id=1)

        def tearDown(self):
            User.query.delete()
            Post.query.delete()
            Comment.query.delete()

        def test_get_comment_by_id(self):
            # self.user_test.save()
            self.new_post.save_post()
            self.new_comment.save_comment()
            got_comments=Comment.get_comments(1)
            self.assertTrue(len(got_comments) == 1)
