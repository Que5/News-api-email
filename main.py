import requests


API_KEY = "962db8ac56fd4382b50a904a263aa1f2"
url = "https://newsapi.org/v2/everything?q=tesla&"\
     "from=2024-04-25&sortBy=publishedAt&apiKey="\
     "962db8ac56fd4382b50a904a263aa1f2"

#Make request
request = requests.get(url)

#Get a dictionanry with data
content = request.json()

#Access the article titles and description

for article in content["articles"]:
    print(article["articles"])
    print(article["description"])

