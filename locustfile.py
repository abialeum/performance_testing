from locust import HttpUser, task
import json

class UserBehavior(HttpUser):

    @task
    def get_tests(self):
        self.client.get("/tests")
        
    @task
    def put_tests(self):
        self.client.headers = {'Content-Type': 'application/json'}
        data = {
                    "name": "load testing",
                    "description": "checking if a software can handle the expected load"
				}
        json_data=json.dumps(data)
        self.client.post("/tests", json_data)
        
    