import requests

freekatvdbergdotus_news_api_key = "0558ecaaf24c435691f8a1f82b761b9a"
news_keyword = "stock&20market"
country = "us"

# returns a list of news articles based on the keyword
r1 = requests.get(f"https://newsapi.org/v2/everything?qInTitle={news_keyword}&sortBy=popularity&language=en&apiKey={freekatvdbergdotus_news_api_key}")
content1 = r1.json()

print(f"\n\n\nNews articles based on the keyword '{news_keyword}':")
for article in content1["articles"]:
    print(20*"-")
    print(article["title"])
    print(article["description"])


# returns a list of news articles based on the country
r2 = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&sortBy=popularity&language=en&apiKey={freekatvdbergdotus_news_api_key}")
content2 = r2.json()

print(f"\n\n\nNews articles based on the country '{country}':")
for article in content2["articles"]:
    print(20*"-")
    print(article["title"])
    print(article["description"])