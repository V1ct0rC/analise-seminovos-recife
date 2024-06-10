import scrapy
from utils import extract_number, extract_engine_size

class CarItalianaSpider(scrapy.Spider):
    name = 'Italiana'
    start_urls = [
        "https://www.italianaseminovos.com.br/estoque?page=1",
        "https://www.italianaseminovos.com.br/estoque?page=2",
        "https://www.italianaseminovos.com.br/estoque?page=3",
        "https://www.italianaseminovos.com.br/estoque?page=4"
        ]

    def parse(self, response):
        car_price = [extract_number(price) for price in response.css(".text-primary.font-weight-bold::text").extract()]
        
        car_brand = response.css(".text-muted.text-uppercase.font-size-12::text").extract()
        
        car_name_engine_desc_gearbox = response.css(".text-uppercase.font-weight-bold.font-size-14.text-center.mb-2::text").extract()
        car_name = [f'{car_brand[i]} {name_engine_desc_gearbox.split(" ")[0]}' for i, name_engine_desc_gearbox in enumerate(car_name_engine_desc_gearbox)]
        car_engine = [extract_engine_size(name_engine_desc_gearbox) for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
        car_desc = [name_engine_desc_gearbox for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
        car_gearbox = ['Manual' if 'MANUAL' in name_engine_desc_gearbox else 'Automatico' for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
        
        car_specs = response.css(".mb-0.font-size-12.text-muted::text").re(r'\s*(\S.*\S)\s*')
        
        car_year = []
        car_km = []
        for km, year in zip(car_specs[0::2], car_specs[1::2]):
            car_year.append(year[5:])
            car_km.append(extract_number(km))
            
        row_data = zip(car_name, car_price, car_desc, car_year, car_km, car_engine, car_gearbox)
        
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
                "car_engine": row[5],
                "car_gearbox": row[6],
                "car_fuel": None,
                "car_color": None,
            }
            
            yield scraped_info