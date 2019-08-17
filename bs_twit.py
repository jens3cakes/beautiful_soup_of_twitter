import requests
from bs4 import BeautifulSoup


url = "https://twitter.com/search"
subj_tofind = input("What would you like to find?")

def tweet_searcher(param):
  results = requests.get(url,params={"q": param})
  find = BeautifulSoup(results.text, "html.parser")
  




