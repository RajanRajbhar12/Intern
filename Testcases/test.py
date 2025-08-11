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
            json={"email":"raj@gmailcom", "password":"12345678"}
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
            json={"email":"raj@", "password":"632145"}
        ) 
        self.assertEqual(response.json(),{"success":True})
    
    def test_div_zero(self):
        response = self.client.post(
            "/calc/div",
            json={"num1": 6, "num2":0}
        ) 
        self.assertEqual(response.json(),{"result": " divided by 0 is not allowed"})
        #this is the change i did
    

if __name__ == "__main__":
    unittest.main()