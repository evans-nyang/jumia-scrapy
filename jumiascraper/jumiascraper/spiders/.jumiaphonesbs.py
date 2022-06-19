import datetime
import re

import html5lib
import scrapy
from bs4 import BeautifulSoup as bs
from bs4 import Tag

from ..items import JumiascraperItem


class JumiaphonesSpider(scrapy.Spider):
    name = "jumiaphones"
    start_urls = ["http://jumia.co.ke/mobile-phones//"]

    # store scraped items to a json file in dataset directory
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "../dataset/phones.json"}

    def parse(self, response):
        items = JumiascraperItem()

        try:
            print("\nTrying to fetch phones in our container...")
            section = response.xpath(
                "//section[@class='card -fh']/div[@class='-paxs row _no-g _4cl-3cm-shs']"
            )
            soup = bs(section.extract_first(), "html5lib")
            articles = soup.find_all("article", {"class": "prd _fb col c-prd"})
            newdict = {}
            # newlist = []
            for i, art in enumerate(articles):
                if i < 200:
                    newdict.update({i: self.parse_result_page(art)})
                    # newlist.append(self.parse_result_page(art))
            # print(newlist)
            yield newdict

        except Exception as err:
            print(f"\nEncounterd an exception during execution: \n{err}")
            raise err

        # else:
        #     next_page = response.css("a.pg:nth-child(6)::attr(href)").get()
        #     # next_page = response.xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[2]/a[6]").xpath("@href")
        #     if next_page is not None:
        #         yield response.follow(next_page, self.parse)

    def parse_result_page(self, art: bs) -> dict:
        data = {}
        core = art.find("a", {"class": "core"})
        data["crawled_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )
        data["name"] = self.__safe_parsing(core.get("data-name"))
        data["href"] = self.__safe_parsing(core.get("href"))
        data["data-id"] = self.__safe_parsing(core.get("data-id"))
        data["brand"] = self.__safe_parsing(core.get("data-brand"))
        data["name2"] = self.__safe_parsing(core.find("h3", {"class": "name"}))
        data["price"] = self.__safe_parsing(core.find("div", {"class": "prc"}))
        data["old_price"] = self.__safe_parsing(
            core.find("div", {"class": "s-prc-w"}).find("div", {"class": "old"})
        )
        data["discount"] = self.__safe_parsing(
            core.find("div", {"class": "s-prc-w"}).find(
                "div", {"class": "bdg _dsct _sm"}
            )
        )
        data["votes"] = self.__safe_parsing(
            core.find("div", {"class": "rev"}).find(text=re.compile(r"\(*\)"))
        )
        data["stars"] = self.__safe_parsing(
            core.find("div", {"class": "rev"}).find("div", {"class": "stars _s"})
        )
        data["image_url"] = self.__safe_parsing(
            core.find("div", {"class": "img-c"})
            .find("img", {"class": "img"})
            .get("data-src")
        )

        data["official_store"] = self.__safe_parsing(
            core.find("div", {"class": "bdg _mall _xs"})
        )

        print()
        return data

    def __safe_parsing(self, parsing) -> str:
        try:
            if isinstance(parsing, str):
                return parsing
            elif isinstance(parsing, Tag):
                return parsing.get_text()
        except Exception:
            return None
