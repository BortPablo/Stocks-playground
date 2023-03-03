import requests

url = "https://twelve-data1.p.rapidapi.com/stocks"

querystring = {"exchange":"NASDAQ","format":"json"}

headers = {
	"X-RapidAPI-Key": "b3dac945efmsh306d272384675c2p1a6d1fjsn67b0e195ac2e",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)