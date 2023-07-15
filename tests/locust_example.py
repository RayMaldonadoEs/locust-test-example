# In locust_example.py
# Example taken from https://pflb.us/blog/load-testing-using-locust/

# Requires Python 3 or higher

# Running from terminal
# locust -f ./tests/locust_example.py --headless -u 2000  -r 5  -t 60m --html report.html

# does:
# running headless request to search at kw.com - city Austin
# Load up to 2000 users - ramp up 5 and move up
# run for 60 minutes




from locust import HttpUser, task, between, constant


class QuickstartUser(HttpUser):
    min_wait = 5000
    max_wait = 10000
    host = "https://kw.com"

    @task(5)
    def test_get_search_method(self):
        resp = self.client.get("/search/TX/Austin?searchedText=Austin%2C%20TX%2C%20US")
        print(resp.status_code)
        print(resp.headers)
        print(resp.request.headers)
        # print(resp.text)  # this might be too verbose for a test load
        
    def on_start(self):
        # Setup method; e.g. log in .
        # self.client.post("/login", {"username": "foo", "password": "bar"})
        pass