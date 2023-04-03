import requests
from bs4 import BeautifulSoup
from lxml import html

# スクレイピングターゲットのURL
url = "https://blog.ablaze.one"


def load(path: str):
    with open(path, "r") as f:
        return f.read()


def fetch(url: str) -> str:
    """urlからページのHTMLを取得する"""

    resp = requests.get(url)

    return resp.text


# インターネットからHTMLを取得する
# soup = BeautifulSoup(fetch(url), "html.parser")

# アクセス数を抑えるためローカルに保存したデータで解析を行う
soup = BeautifulSoup(load("./blog.html"), "html.parser")
xmltree = html.fromstring(str(soup))

content_xml = xmltree.xpath('//*[@id="content"]/div')

posts = BeautifulSoup(html.tostring(content_xml[0]).decode(), "html.parser")

for post in posts.find_all("article"):
    titles = post.find_all("h2")

    for title in titles:
        for titles in title.find("a"):
            title_text = titles.get_text()

            print(title_text)
