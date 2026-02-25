import requests
import webbrowser

URL = requests.get("https://cataas.com/cat?json=true")
data = URL.json()

print(f"\nСсылка: {data["url"]}\nДата создания: {data["created_at"]}\nТеги: {data["tags"]}\n")

webbrowser.open(data["url"])