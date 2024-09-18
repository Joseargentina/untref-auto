import requests
import unittest

class Test_Json(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://jsonplaceholder.typicode.com/'
        self.my_post = {'title': 'foo','body': 'bar','userId': 1}
    def test_get_title(self):
        r = requests.get(self.url+'posts/5')
        self.assertEqual(r.status_code,200)
        post_data = r.json()
        self.assertEqual(post_data['userId'],1)
        self.assertEqual(post_data['title'], 'nesciunt quas odio')
        self.assertEqual({'userId': 1, 'id': 5, 'title': 'nesciunt quas odio', 'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'},post_data)

    def test_post_article(self):
        r = requests.post(self.url+'posts', data = self.my_post)
        self.assertEqual(r.status_code,201)
        post_data = r.json()
        self.assertTrue(post_data['title'] == self.my_post['title'])
        self.assertTrue(post_data['body'] == self.my_post['body'])