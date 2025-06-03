# 📰 News Fetcher CLI using NewsAPI

This is a simple **command-line Python script** that fetches the latest news articles on any topic using the [NewsAPI](https://newsapi.org/). It allows users to enter a topic of interest (e.g., "AI", "sports", "politics") and displays the most recent news headlines related to that topic.

---

## 🔧 Features

* 🔎 Search news by any topic
* 🕒 Sorted by latest published date
* 🌐 Retrieves real-time data using the NewsAPI
* 🛌 Adds a 2-second delay between articles for easy reading

---

## 🛆 Requirements

* Python 3.x
* `requests` module

> Install dependencies (if not already installed):

```bash
pip install requests
```

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/news-fetcher.git
   cd news-fetcher
   ```

2. Open `news_fetcher.py` (or your script filename) and replace `apiKey` with your own [NewsAPI key](https://newsapi.org/register).

3. Run the script:

   ```bash
   python news_fetcher.py
   ```

4. Enter a topic when prompted:

   ```
   enter the topic : technology
   ```

---

## 💻 Example Output

```
enter the topic : AI

*************************************************

0 OpenAI launches new GPT-5 model with advanced reasoning

_________________________________________________

https://example.com/openai-gpt5-news

(wait 2 seconds...)

*************************************************

1 AI regulation becomes global priority, says UN

_________________________________________________

https://example.com/ai-regulation-news
```

---

## 📌 Notes

* Make sure your API key has not exceeded its quota.
* Modify the `from` date or other parameters in the API URL to customize search.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
