from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class QuotesLoaders(ItemLoader):
    default_output_processor = TakeFirst()
    tag_links_in = MapCompose(lambda x: f"https://quotes.toscrape.com/{x}")
