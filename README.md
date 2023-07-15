# Example taken from https://pflb.us/blog/load-testing-using-locust/

# Requires Python 3 or higher

# Running from terminal
# locust -f ./tests/locust_example.py --headless -u 2000  -r 5  -t 60m --html report.html

# does:
# running headless request to search at kw.com - city Austin
# Load up to 2000 users - ramp up 5 and move up
# run for 60 minutes