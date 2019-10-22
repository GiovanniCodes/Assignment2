import unittest

from flask_request import app

class testFlask(unittest.TestCase):
    def test_distance_response(self):
        c = app.test_client()
        response = c.get('/distance/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_retirement_response(self):
        c = app.test_client()
        response = c.get('/retirement/')
        self.assertEqual(response.status_code, 200)

    def test_retirement_data(self):
        c = app.test_client()
        response = c.post('/retirement/')
        self.assertEqual(response.status_code, 200)


    def test_distance_data(self):
        c = app.test_client()
        response = c.delete('/distance/')
        self.assertEqual(response.status_code, 405)


if __name__ == "__main__":
  unittest.main()