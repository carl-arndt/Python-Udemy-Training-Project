
from blog.post import Post
from unittest import TestCase  # TestCase is part of the unittest library


# from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        # assert uses the TestCase API
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        # checks that the keys and values are the same as oppposed to the object being the same
        self.assertDictEqual(expected, p.json())

