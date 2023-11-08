
















# with open("index.html", encoding="utf-8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="header")
# # print("heading")
# # heading = soup.find(name="h1", class_="")
#
# company_url = soup.select_one(selector="p a")
# print(company_url)