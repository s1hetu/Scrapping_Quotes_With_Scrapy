import scrapy

from scrapping.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        for i in response.xpath("//div[@class='quote']"):
            title = i.xpath(".//span[@class='text']/text()").get()
            author = i.xpath(".//small[@class='author']/text()").get()
            tags = i.xpath(".//a[@class='tag']")
            tag_link = tags.xpath("@href").getall()
            tag_name = tags.xpath("text()").getall()
            quote_data = QuotesItem()
            quote_data['title'] = title
            quote_data['author'] = author
            quote_data['tag_links'] = tag_link
            quote_data['tag_names'] = tag_name
            yield quote_data

        """
        # with item loaders
        from scrapping.itemsloaders import QuotesLoaders
        quote_data = QuotesLoaders(item=QuotesItem(), selector=i)
        quote_data.add_css('title', title)
        quote_data.add_css('author', author)
        quote_data.add_css('tag_links', tag_link)
        quote_data.add_css('tag_names', tag_name)
        quote_data.add_css('price', len(tag_name))
        yield quote_data.load_item()
        """

        if next_page := response.xpath('//li[@class="next"]/a/@href').get():
            next_page_url = self.start_urls[0] + next_page
            yield response.follow(next_page_url, callback=self.parse)
