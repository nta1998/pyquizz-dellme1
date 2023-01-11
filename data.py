import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", verify=False)
response.raise_for_status()
data = response.json()
question_data = data["results"]