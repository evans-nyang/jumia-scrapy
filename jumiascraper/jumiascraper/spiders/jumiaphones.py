import datetime

import scrapy


class JamSpider(scrapy.Spider):
    name = "jam"
    start_urls = ["http://jumia.co.ke/mobile-phones//"]
    # store scraped items to a json file in dataset directory
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "../dataset/phones.json"}

    def parse(self, response):
        try:
            print("\nTrying to fetch our articles   ")
            articles = response.xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[@class='prd _fb col c-prd']")
            newdata = {}
            for i, art in enumerate(articles):
                if i < 250:
                    newdata.update({i: self.parse_result(art)})
            yield newdata

        except Exception as err:
            print("\nEncountered an exception during execution")
            raise err

        else:
            next_page = (
                response.xpath(
                    "/html/body/div[1]/main/div[2]/div[3]/section/div[2]/a[6]"
                )
                .xpath("@href")
                .get()
            )
            if next_page is not None:
                yield response.follow(next_page, self.parse)

    def parse_result(self, art) -> dict:
        data = {}
        core = art.xpath(".//a[@class='core']")
        data["crawled_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )
        data["name"] = self.__safe_parsing(core.xpath("@data-name").get())
        data["href"] = self.__safe_parsing(core.xpath("@href").get())
        data["data-id"] = self.__safe_parsing(core.xpath("@data-id").get())
        data["brand"] = self.__safe_parsing(core.xpath("@data-brand").get())
        data["name2"] = self.__safe_parsing(core.xpath(".//div[@class='info']/h3/text()").get())
        data["price"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='prc']/text()").get())
        data["old_price"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='s-prc-w']/div/text()").get())
        data["discount"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='s-prc-w']/div[@class='bdg _dsct _sm']/text()").get())
        data["votes"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='rev']/text()").get())
        data["stars"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='rev']/div[@class='stars _s']/text()").get())
        data["image_url"] = self.__safe_parsing(core.xpath(".//div[@class='img-c']/img[@class='img']/@data-src").get())
        data["official_store"] = self.__safe_parsing(core.xpath(".//div[@class='info']/div[@class='bdg _mall _xs']/text()").get())

        return data

    def __safe_parsing(self, parsing) -> str:
        try:
            if isinstance(parsing, str):
                return parsing
            elif isinstance(parsing, scrapy.Selector):
                return parsing.get()
        except Exception:
            return None
