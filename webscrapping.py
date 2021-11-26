import requests
from bs4 import BeautifulSoup as bs

github_user_name = input("Input Github User Name: ")
url = "https://github.com/"+github_user_name
r = requests.get(url)
soup = bs(r.content, "html.parser")
prifile_image = soup.find("img", {"alt" : "Avatar"})["src"]
print(prifile_image)
