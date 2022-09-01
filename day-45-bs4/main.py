# Check <rootURL> robots.txt before scraping any website
from bs4 import BeautifulSoup
# with open ("website.html", encoding="utf8") as file:
#     contents = file.read()
# #print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.text)
# #print(soup.prettify())
# # print(soup.p)
#
# li_list = [li.getText() for li in soup.find_all(name="li")]
# print(li_list)
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name) # getting the name of the tag
# print(section_heading.get("class")) # getting the name of the class
#
# list_a = [a for a in soup.find_all(name="a")]
# print(list_a[1])
#
# company_url = soup.select_one(selector="p a") # select_one would return the first matching element while select returns all
# print(company_url)
#
# name = soup.select_one(selector="#name") # getting id="name"
# print(name)
#
# headings = soup.select(".heading") # getting class="heading
# print(headings)
#
# links = [link.get('href') for link in soup.find_all(name="a")] # getting the actual hrefs
# print(links)
#
# parent_tag = soup.title.parent.name # getting parent tag name
# print(parent_tag)
#
# #soup.find_all("a", "li") # find all a in a li tag

import requests
ycomb = requests.get("https://news.ycombinator.com/")
ycomb.raise_for_status()
#print(ycomb.text)

soup = BeautifulSoup(ycomb.text, "html.parser")
# print(soup.title)
# print(soup.title.text)
# print(soup.prettify())

link = soup.select(selector=".storylink")
#print(link)

#texts, links, upvotes.

score_list = soup.select(selector=".score")
score = [int(score.getText().replace(" points", "")) for score in score_list] # can use strip here and use <>[0]
print(score)

#print(max(score_1))
title_list = soup.select(selector=".storylink")
link = [link.get('href') for link in title_list]
text = [link.getText() for link in title_list]
print(link)
print(text)

print(max(score))
max_score_index = score.index(max(score))
print(link[max_score_index])
print(text[max_score_index])


# score_max = ""
# track = 0
# for score in score_list:
#     score_int = int(score.getText().replace(" points", ""))
#     if score_int > track:
#         track = score_int
#         score_max = score
#
# print(track)
# print(score_max)
# print(soup.select(selector=".storylink"))
