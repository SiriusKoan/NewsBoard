from lxml import etree
import requests
from html2text import html2text


def get_news(keyword, language):
    # language: zh-TW or en
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    }
    r = requests.get(
        "https://www.google.com/search?q=%s&tbm=nws&lr=lang_%s&hl=%s"
        % (keyword, language, language),
        headers=headers,
    )
    content = r.content.decode("utf-8")

    news = []

    web = etree.HTML(content)
    for i in range(1, 5):
        piece = dict()
        href = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a"
            % i
        )
        piece["href"] = (href[0].attrib["href"]).replace("\n", "")

        title = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[2]"
            % i
        )
        piece["title"] = (html2text(etree.tostring(title[0]).decode("utf-8"))).replace(
            "\n", ""
        )

        time = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[3]/div[2]"
            % i
        )
        piece["time"] = (html2text(etree.tostring(time[0]).decode("utf-8"))).replace(
            "\n", ""
        )

        author = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[1]"
            % i
        )
        author = html2text(etree.tostring(author[0]).decode("utf-8"))
        # separate author's avatar(base64) and name
        piece["author_avatar"] = (author[0 : author.index(")")]).replace("\n", "")
        piece["author_name"] = (author[author.index(")") + 1 :]).replace("\n", "")

        news.append(piece)
    return news


# test
print(get_news("nba", "zh-TW"))
print(get_news("cat", "en"))
