import requests
from bs4 import BeautifulSoup


url = "https://twitter.com/search"
subj_tofind = input("What would you like to find?")

find_tweet = requests.get(url,
  params={"q": subj_tofind},
  headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
)
#results = requests.get(url,params={"q": })
find_soup = BeautifulSoup(find_tweet.text, "html.parser")

recipe_for_soup = open("yummy.txt", "a")

def user_searcher(param):
  usernames = find_soup.select("div.content strong.fullname")
  for username in usernames:
    tweet_searcher()
    print(username.text)
    recipe_for_soup.write("\n"+ username.text + "\n" + tweet_searcher())    



def tweet_searcher():
  tweets = find_soup.select("div.content p.tweet-text")
  for tweet in tweets:
    return(tweet.get_text())

if __name__ == "__main__":

    user_searcher(subj_tofind)
    tweet_searcher()

