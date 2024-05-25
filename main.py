import requests
from send_email import send_email


API_KEY = "962db8ac56fd4382b50a904a263aa1f2"
url = "https://newsapi.org/v2/everything?q=tesla&"\
     "from=2024-04-25&sortBy=publishedAt&apiKey="\
     "962db8ac56fd4382b50a904a263aa1f2"

#Make request
request = requests.get(url)

#Get a dictionanry with data
content = request.json()

#Access the article titles and description

body = " "
for article in content["articles"]:
    body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
    

