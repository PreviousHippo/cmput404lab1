import requests

response = requests.post("http://ccid-eddieantonio.rhcloud.com/thu2")

print response.status_code
print requests.__version__
