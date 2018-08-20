from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        # same assert as above, just another way to do it:
        # self.asertEqual(0, len(b.posts))
       # print("tests in test_create_blog complete")

    def test_repr(self):
        b = Blog('Title', 'Author')
        c = Blog('My Day', 'Bob')
        self.assertEqual(b.__repr__(), 'Title by Author (0 posts)')
        self.assertEqual(c.__repr__(), 'My Day by Bob (0 posts)')
       # print("tests in test_repr complete")

    def test_repr_multiple_posts(self):
        b = Blog('Title', 'Author')
        b.posts = ['post1']
        b2 = Blog('My Day', 'Bob')
        b2.posts = ['Test Blog', 'another']

        self.assertEqual(b.__repr__(), 'Title by Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Bob (2 posts)')

       # print("tests in test_repr_multiple_posts complete")

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

