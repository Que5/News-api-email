import requests
from send_email import send_email


topic = "cryptocurrency"


API_KEY = "962db8ac56fd4382b50a904a263aa1f2"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
     "from=2024-04-25&sortBy=publishedAt&apiKey="\
     "962db8ac56fd4382b50a904a263aa1f2&language=en"

#Make request
request = requests.get(url)

#Get a dictionanry with data
content = request.json()

#Access the article titles and description

body = " "
for article in content["articles"][:10]:
    body =  "Subject: Today's news" + "\n" \
    + body + str(article["title"]) + "\n" \
        + str(article["description"]) \
              + "\n" + str(article["url"])  + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
    

