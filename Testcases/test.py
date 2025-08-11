import unittest
import sys
import os
sys.path.append(r'C:\Users\rajan\OneDrive\Desktop\Intern\tih1')
from fastapi.testclient import TestClient
from main import app,client


class TestMainAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        cls.client = TestClient(app)

    @classmethod
    def tearDownClass(cls):
       
        client.close()
        cls.client.close()
   

    def test_signup(self):
        response = self.client.post(
            "/signup",
            json={"email":"rajannrajb502@gmail.com", "password":"12568"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "User saved!"})

    def test_add(self):
        response = self.client.post(
            "/calc/add",
            json={"num1": 5, "num2": 5}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 10})
       

    def test_sub(self):
        response = self.client.post(
            "/calc/sub",
            json={"num1": 6, "num2":2}
        ) 
        self.assertEqual(response.json(),{"result":4})
       
    def test_div(self):
        response = self.client.post(
            "/calc/div",
            json={"num1": 6, "num2":2}
        ) 
        self.assertEqual(response.json(),{"result":3})
    
    def test_mul(self):
        response = self.client.post(
            "/calc/mul",
            json={"num1": 6, "num2":2}
        ) 
        self.assertEqual(response.json(),{"result":12})

    def test_login(self):
       
        response = self.client.post(
            "/login",
            json={"email":"rajannrajb502@gmail.com", "password":"12568"}
        ) 
        self.assertEqual(response.json(),{"success":True})

if __name__ == "__main__":
    unittest.main()