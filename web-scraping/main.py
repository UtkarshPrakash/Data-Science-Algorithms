from bs4 import BeautifulSoup

with open("index.html", 'r') as html_file:
    contents = html_file.read()
    print(contents)