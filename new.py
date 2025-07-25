import requests

url = "https://mail-man.p.rapidapi.com/mail"

payload = {
	"email": "you@gmail.com",
	"password": "app password from google",
	"from": "Company Name <you@gmail.com>",
	"to": "nkwentideshnic@gmail.com",
	"subject": "Greetings",
	"message": "<p>Hello world<p>"
}
headers = {
	"x-rapidapi-key": "6ad0248a75mshf9d81495887932ap17b859jsn4b4e9e15f052",
	"x-rapidapi-host": "mail-man.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())