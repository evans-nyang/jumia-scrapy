import datetime

from ..items import JumiascraperItem

import scrapy


class JamSpider(scrapy.Spider):
    name = "jumiascraper"
    start_urls = ["https://jumia.co.ke"]
    allowed_domains = ["jumia.co.ke"]
    count = 1

    def parse(self, response):
        url = f"{self.start_urls[0]}/mobile-phones"
        # settings = get_project_settings()
        yield scrapy.Request(url=url, callback=self.parse_items)
    
    def parse_items(self, response):
        items = JumiascraperItem()
        try:
            print("\nTrying to fetch our articles...")
            articles = response.xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[@class='prd _fb col c-prd']")
            newdata = {}
            for i, art in enumerate(articles):
                if i < 250:
                    newdata.update({i: self.parse_result(art)})
            items["inform"] = newdata
            yield items

            next_page = (
                response.xpath(
                    "/html/body/div[1]/main/div[2]/div[3]/section/div[2]/a[6]"
                )
                .xpath("@href")
                .get()
            )
            if next_page is not None and self.count < 51:
                url = f"{self.start_urls[0]}{next_page}"
                self.count += 1
                print(f"\nGoing to next page {self.count}\n")
                yield scrapy.Request(url=url, callback=self.parse_items)

        except Exception as err:
            print("\nEncountered an exception during execution")
            raise err

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
