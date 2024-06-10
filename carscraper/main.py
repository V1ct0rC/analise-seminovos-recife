import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from carscraper.spiders.car_autonunes import CarAutonunesSpider
from carscraper.spiders.car_azzurra import CarAzzurraSpider
from carscraper.spiders.car_disnove import CarDisnoveSpider
from carscraper.spiders.car_italiana import CarItalianaSpider
from carscraper.spiders.car_pedragon import CarPedragonSpider
from carscraper.spiders.car_usadosbr import CarUsadosBRSpider

# settings = get_project_settings()
# process = CrawlerProcess(settings)
# process.crawl(CarAutonunesSpider)
# process.crawl(CarAzzurraSpider)
# process.crawl(CarDisnoveSpider)
# process.crawl(CarItalianaSpider)
# process.crawl(CarPedragonSpider)
# process.crawl(CarUsadosBRSpider)
# process.start()

from scrapy.utils.reactor import install_reactor
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner

settings = get_project_settings()
runner = CrawlerRunner(settings)


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CarAutonunesSpider)
    yield runner.crawl(CarAzzurraSpider)
    yield runner.crawl(CarDisnoveSpider)
    yield runner.crawl(CarItalianaSpider)
    yield runner.crawl(CarPedragonSpider)
    yield runner.crawl(CarUsadosBRSpider)
    reactor.stop()

crawl()
reactor.run()