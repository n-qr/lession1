import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1348034457893863484/LvB8d_NAaCXlGxf0L53oY-5sHaDBz25gPcyfVUdpx3uY-7rGA7XDxI8bE23avS4GijXS" 

data = {
    "content": "test"
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.status_code}")
    print(response.text)
