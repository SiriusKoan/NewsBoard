from lxml import etree
import requests
from html2text import html2text

def delete_space(x):
    return x.replace('\n', "")

def get_news(keyword, language):
    # language: zh-TW or en
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    r = requests.get('https://www.google.com/search?q=%s&tbm=nws&lr=lang_%s&hl=%s' % (keyword, language, language),
                     headers=headers,)
    content = r.content.decode("utf-8")

    news = []

    web = etree.HTML(content)
    for i in range(1, 2):
        href = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a" % i)[0]
        title = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[2]" % i)[0]
        time = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[3]/div[2]" % i)[0]

        author = web.xpath(
            "/html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[%d]/g-card/div/div/div[2]/a/div/div[2]/div[1]"% i)[0]
        author = html2text(etree.tostring(author).decode('utf-8'))
        author_picture = author[0:author.index(")")]
        author_name = author[author.index(")")+1:]

        news.append([href.attrib['href'],
                     html2text(etree.tostring(title).decode('utf-8')),
                     html2text(etree.tostring(time).decode('utf-8')),
                     author_picture,
                     author_name
                     ])
    for li in news:
        final = list(map(delete_space,li))

    return final


# test
print(get_news('cat', 'zh-TW'))
print(get_news('cat', 'en'))
