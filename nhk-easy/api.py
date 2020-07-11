import requests
import time
from lxml import etree as le


class Api(object):
    BASE_URL = "https://www3.nhk.or.jp/news/easy"

    def __init__(self):
        self.timestamp = str(time.time()).split(".")[0]
        self.top_news = self.get_top_news_list()

    def get_top_news_list(self):
        url = self.BASE_URL + "/top-list.json?_=" + self.timestamp
        r = requests.get(url)
        return r.json()

    def download_top_news(self):
        for news in self.top_news:
            [id_, dttm, title] = [
                news[a] for a in ("news_id", "news_prearranged_time", "title")
            ]
            fn = dttm.split(" ")[0] + "-" + title
            article = Article(id_)
            with open(fn + ".m3u8", "w") as f:
                f.write(article.m3u8)
            with open(fn + ".txt", "w") as f:
                f.write(article.text)
            time.sleep(0.5)


class Article(object):
    BASE_URL = "https://www3.nhk.or.jp/news/easy"
    # https://www3.nhk.or.jp/news/easy/k10012501481000/k10012501481000.html

    def __init__(self, id_):
        self.id_ = id_
        self.m3u8 = self.get_m3u8()
        self.text = self.get_text()

    def get_m3u8(self):
        url = f"https://nhks-vh.akamaihd.net/i/news/easy/{self.id_}.mp4/master.m3u8"
        r = requests.get(url)
        return r.text

    def get_raw_html(self):
        url = f"{self.BASE_URL}/{self.id_}/{self.id_}.html"
        r = requests.get(url)
        r.encoding = "UTF-8"
        return le.HTML(r.text)

    def get_text(self):
        html = self.get_raw_html()
        le.strip_elements(html, "rt")
        # //div[@id_='js-article-body']
        return "".join(html.xpath("//div[@id='js-article-body']//text()")).strip()


# remove_tags = tree.xpath('//div[last()]')

# if remove_tags:
#     remove_tag = remove_tags[0]
#     remove_tag.getparent().remove(remove_tag)
