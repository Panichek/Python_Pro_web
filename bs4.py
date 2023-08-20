from bs4 import BeautifulSoup
import requests
html_doc = ("<html><head><title>The Dormouse's story</title></head>\n"
            "<body>\n"
            "<p class=\"title\"><b>The Dormouse's story</b></p>\n"
            "\n"
            "<p class=\"story\">Once upon a time there were three little sisters; and their names were\n"
            "<a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\">Elsie</a>,\n"
            "<a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and\n"
            "<a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;\n"
            "and they lived at the bottom of a well.</p>\n"
            "\n"
            "<p class=\"story\">...</p>\n")
'''
result_code = BeautifulSoup(html_doc,"html.parser")
current_element = result_code.find("p",class_="story")

element = current_element.find("a",id="link1")
print(element.get("class"))
'''
'''
result_code = BeautifulSoup(html_doc,"html.parser")
for link in result_code.find_all("a"):
    print(link.get("href"))
'''
#print(result_code.prettify())
# FIND знайти
# FINDALL