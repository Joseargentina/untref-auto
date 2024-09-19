import requests
import unittest

class Test_Json(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://jsonplaceholder.typicode.com/'
        self.my_post = {'title': 'foo','body': 'bar','userId': 1}
    def test_get_title(self):
        r = requests.get(self.url+'posts/5')
        self.assertEqual(r.status_code,200)
       