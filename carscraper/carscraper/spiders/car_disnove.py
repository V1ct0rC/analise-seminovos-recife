import scrapy
from utils import extract_number, extract_engine_size

class CarDisnoveSpider(scrapy.Spider):
    name = 'Disnove'
    start_urls = [
        "https://www.disnove.com.br/seminovos/",
        "https://www.disnove.com.br/seminovos/9",
        "https://www.disnove.com.br/seminovos/18"
        ]

    def parse(self, response):            
        car_price = [extract_number(price) for price in response.css(".color-blue-light.font-weight-bold.font-24.text-center.mb-2::text").extract()]
        
        car_brand = response.css('.font-12.color-dark.text-uppercase.p-0.m-0::text').extract()
        
        car_name_engine_desc_gearbox = response.css('.font-18.color-navy.text-uppercase.p-0.m-0::text').extract()
        car_name = [f'{brand} {name_desc.split(" ")[0]}' for brand, name_desc in zip(car_brand, car_name_engine_desc_gearbox)]
        car_desc = [' '.join(name_desc.split(" ")[1:]) for name_desc in car_name_engine_desc_gearbox]
        car_engine = [extract_engine_size(name_desc) for name_desc in car_name_engine_desc_gearbox]
        car_gearbox = ['Manual' if 'MANUAL' in name_desc else 'Automatico' for name_desc in car_name_engine_desc_gearbox]
        
        car_year_fuel_km_color = response.css(".font-14.color-dark.p-0.m-0.pt-2::text").extract()
        
        car_year = []
        car_fuel = []
        car_km = []
        car_color = []
        
        for year, fuel, km, color in zip(car_year_fuel_km_color[0::4], car_year_fuel_km_color[1::4], car_year_fuel_km_color[2::4], car_year_fuel_km_color[3::4]):
            car_year.append(year)
            car_fuel.append(fuel)
            car_km.append(extract_number(km))
            car_color.append(color)
            
        row_data = zip(car_name, car_price, car_year, car_km, car_fuel, car_color, car_desc, car_engine, car_gearbox)
        
        for row in row_data:
            scraped_info = {
                "page": response.url,
                "car_name": row[0],
                "car_price": row[1],
                "car_km": row[3],
                "car_year": row[2],
                "car_desc": row[6],
                "car_store": None,
                "car_engine": row[7],
                "car_gearbox": row[8],
                "car_fuel": row[4],
                "car_color": row[5],
            }
            
            yield scraped_info