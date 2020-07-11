import requests
import time
from lxml import etree as le
from copy import deepcopy
import os
import logging
import re

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
streamhandler = logging.StreamHandler()
logger.addHandler(streamhandler)


class NHKEasy(object):
    BASE_URL = "https://www3.nhk.or.jp/news/easy"


class Api(NHKEasy):
    def __init__(self):
        self.timestamp = str(time.time()).split(".")[0]
        self.top_news = self.get_top_news_list()

    def get_top_news_list(self):
        url = self.BASE_URL + "/top-list.json?_=" + self.timestamp
        r = requests.get(url)
        return r.json()

    def download_top_news(self, furigana=True, html_output=False, mp3=True, text=True):
        for news in self.top_news:
            [id_, dttm, title] = [
                news[a] for a in ("news_id", "news_prearranged_time", "title")
            ]
            logger.info("Downloading: " + title)
            fn = dttm.split(" ")[0] + "-" + title
            article = Article(id_)
            if text and not os.path.exists(fn + ".txt"):
                text = article.get_text(furigana, html_output)
                ext = ".html" if html_output else ".txt"
                with open(fn + ext, "w") as f:
                    f.write(text)
            if mp3 and not os.path.exists(fn + ".mp3"):
                article.download_mp3(fn + ".mp3")
            else:
                if not os.path.exists(fn + ".m3u8"):
                    m3u8 = article.get_m3u8()
                    with open(fn + ".m3u8", "w") as f:
                        f.write(m3u8)
            time.sleep(0.5)


class Article(NHKEasy):
    def __init__(self, id_):
        self.id_ = id_
        self.m3u8_url = (
            f"https://nhks-vh.akamaihd.net/i/news/easy/{self.id_}.mp4/master.m3u8"
        )

    def get_m3u8(self):
        r = requests.get(self.m3u8_url)
        return r.text

    def get_raw_html(self):
        url = f"{self.BASE_URL}/{self.id_}/{self.id_}.html"
        r = requests.get(url)
        r.encoding = "UTF-8"
        return r.text

    def get_text(self, furigana=True, html_output=False):
        article_body_xpath = "//div[@id='js-article-body']"
        extract_html = lambda html: le.tostring(
            html.xpath(f"{article_body_xpath}")[0]
        ).decode("utf-8")
        join_text = lambda html: "".join(
            html.xpath(f"{article_body_xpath}//text()")
        ).strip()

        raw_html = self.get_raw_html()
        html = le.HTML(raw_html)
        if furigana:
            if html_output:
                return extract_html(html)
            else:
                html = le.HTML(re.sub("<rt>(.+?)</rt>", r"（\1）", raw_html))
                return join_text(html)
        else:
            le.strip_elements(html, "rt")
            if html_output:
                return extract_html(html)
            else:
                return join_text(html)

    def download_mp3(self, fn):
        os.system(f"ffmpeg -i {self.m3u8_url} -acodec mp3 -ab 257k '{fn}'")
