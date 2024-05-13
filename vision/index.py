

import requests

url = "https://chatgpt-42.p.rapidapi.com/gpt4"

payload = {
	"messages": [
		{
			"role": "user",
			"content": "hi"
		}
	],
	"web_access": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "api",
	"X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())




