from pep_parse.items import PepParseItem
import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps = response.css('#pep-content tbody tr')
        for pep in peps:
            data_strings = pep.css('td')
            pep_card_link = data_strings.css('a::attr(href)').get()
            data = {
                'number': data_strings[1].css('::text').get(),
                'name': data_strings[2].css('::text').get(),
            }
            yield response.follow(
                pep_card_link,
                callback=self.parse_pep,
                cb_kwargs=data
            )

    def parse_pep(self, response, **data):
        yield PepParseItem(
            **data,
            status=response.css('abbr::text').get()
        )
