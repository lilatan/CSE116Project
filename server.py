import unittest
import requests
#server
class endpointTest(unittest.TestCase):
    def test_something(self):
        r = requests.get('http://127.0.0.1:5000/players')
        self.assertEqual(str(r.json()),"['bob', 'lob', 'tob', 'mob']")
        r = requests.post('http://localhost:5000/join', json = {'name' : 'hao'})
        r = requests.get('http://127.0.0.1:5000/players')
        self.assertEqual(str(r.json()),"['bob', 'lob', 'tob', 'mob', hao']")
        r = requests.post('http://localhost:5000/leave', json = {'name' : 'hao'})
        r = requests.get('http://localhost:5000/players')
        self.assertEqual(str(r.json()),"['bob', 'lob', 'tob', 'mob']")
        r = requests.post('http://localhost:5000/leave', json = {'name' : 'tob'})
        r = requests.post('http://localhost:5000/leave', json = {'name' : 'mob'})
        r = requests.get('http://localhost:5000/players')
        self.assertEqual(str(r.json()),"['bob', 'lob']")
        r = requests.post('http://localhost:5000/join', json = {'name' : 'tob'})
        r = requests.post('http://localhost:5000/join', json = {'name' : 'mob'})
if __name__ == '__main__':
    unittest.main()