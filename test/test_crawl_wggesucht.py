import unittest
from flathunter.crawl_wggesucht import CrawlWgGesucht

class WgGesuchtCrawlerTest(unittest.TestCase):

    TEST_URL = 'https://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.1.0.html?offer_filter=1&city_id=8&noDeact=1&categories%5B%5D=2&rent_types%5B%5D=2&sMin=70&rMax=1500&rmMin=2&fur=2&sin=2&exc=2&img_only=1'

    def setUp(self):
        self.crawler = CrawlWgGesucht()

    def test(self):
        soup = self.crawler.get_page(self.TEST_URL, 1)
        self.assertIsNotNone(soup, "Should get a soup from the URL")
        entries = self.crawler.extract_data(soup)
        self.assertIsNotNone(entries, "Should parse entries from search URL")
        self.assertTrue(len(entries) > 0, "Should have at least one entry")
        self.assertTrue(entries[0]['id'] > 0, "Id should be parsed")
        self.assertTrue(entries[0]['url'].startswith("https://www.wg-gesucht.de/wohnungen"), u"URL should be an apartment link")
        for attr in [ 'title', 'price', 'size', 'rooms', 'address' ]:
            self.assertIsNotNone(entries[0][attr], attr + " should be set")
