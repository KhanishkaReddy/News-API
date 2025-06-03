import requests
import time

# Replace with your own API key from https://newsapi.org/
api_key = "YOUR_API_KEY_HERE"

topic = input("Enter the topic: ")
url = f"https://newsapi.org/v2/everything?q={topic}&from=2025-05-03&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(url)
data = response.json()

articles = data.get("articles", [])

if not articles:
    print("No articles found.")
else:
    for i, article in enumerate(articles):
        print("\n*************************************************\n")
        print(f"{i} {article['title']}")
        print("\n_________________________________________________\n")
        print(article["url"])
        time.sleep(2)
