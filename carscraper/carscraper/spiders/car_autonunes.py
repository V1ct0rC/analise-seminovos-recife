import scrapy
from utils import extract_number, extract_engine_size

class CarAutonunesSpider(scrapy.Spider):
    name = 'Autonunes'
    start_urls = [
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=1",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=2",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=3",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=4",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=5",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=6",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=7",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=8",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=9",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=10",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=11",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=12",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=13",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=14",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=15",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=16",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=17",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=18",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=19",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=20",
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=21"
    ]

    def parse(self, response):
        car_price = [extract_number(price) for price in response.css(".valor::text").re(r'\s*(\S.*\S)\s*')]
            
        car_name = response.css("span.nome-do-carro strong::text").extract()
        
        car_engine_desc_gearbox = response.css(".versao.px-3.mt-3.mb-1::text").re(r'\s*(\S.*\S)\s*')
        car_engine = [extract_engine_size(engine_desc) for engine_desc in car_engine_desc_gearbox]
        car_desc = [engine_desc for engine_desc in car_engine_desc_gearbox]
        car_gearbox = ['Manual' if 'MANUAL' in engine_desc else 'Automatico' for engine_desc in car_engine_desc_gearbox]
        
        car_specs = response.css('.car-icon::text').re(r'\s*(\S.*\S)\s*')
        
        car_year = []
        car_km = []
        car_fuel = []
        
        for year, km, fuel in zip(car_specs[0::3], car_specs[1::3], car_specs[2::3]):
            car_year.append(year[5:])
            car_km.append(extract_number(km))
            car_fuel.append(fuel.title())
            
        row_data = zip(car_name, car_price, car_desc, car_year, car_km, car_fuel, car_engine, car_gearbox)
        
        for row in row_data:
            scraped_info = {
                "page": response.url,
                "car_brand": row[0].partition(" ")[0].title(),
                "car_name": row[0].partition(" ")[2].title(),
                "car_price": row[1],
                "car_km": row[4],
                "car_year": row[3],
                "car_desc": row[2],
                "car_store": None,
                "car_engine": row[6],
                "car_gearbox": row[7],
                "car_fuel": row[5],
                "car_color": None,
            }
            
            yield scraped_info