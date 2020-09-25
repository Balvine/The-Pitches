# import unittest
# from app.models import Comment, User, Post
# from app import db


# class CommentTest(unittest.TestCase):
#         def setUp(self):
#             self.user_test = User(username='test6', email='test6@notgmail.com', password='testpass')
#             self.user_test.save()
#             self.new_post=Post(post_category='ti65', post_title='test', post_text='test post', user_id = self.user_test.id)
#             self.new_post.save_post()            
#             self.new_comment=Comment(comment_text='test comment', post_id = self.new_post.id)
#             self.new_comment.save_comment()

#         def tearDown(self):            
#             Comment.query.delete()
#             Post.query.delete()
#             User.query.delete()

#         def test_get_comment_by_id(self):
#               got_comments = Comment.get_comments(self.new_post.id)
#               self.assertTrue(len(got_comments) == 1)
            
        
#         def test_get_comment_id(self):
#             _id = self.new_comment.id
#             got_comment_id = Comment.get_comments(self.new_post.id)[0].id
#             self.assertTrue(_id  == got_comment_id)
              
              
        
