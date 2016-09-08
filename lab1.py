import requests

response = requests.get("https://github.com/PreviousHippo/cmput404lab1/raw/master/lab1.py")

print response.text

print requests.__version__
