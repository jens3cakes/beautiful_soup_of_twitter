from bs4 import BeautifulSoup


url = "https://twitter.com/search"
results = requests.get(url,params={"q": param})
find = BeautifulSoup(results.text, "html.parser")
  
def comments(param):
  twit_comment = find.select("div.js-tweet-text-container")
  

