import scrapy
from utils import extract_number

class CarPedragonSpider(scrapy.Spider):
    name = 'Pedragon'
    start_urls = ["https://www.pedragonchevroletrecife.com.br/seminovos?condicao=seminovo"]

    def parse(self, response):    

        car_year_name = response.css(".inventory-title::text").extract()
        car_year = [year_name.split(' ')[0] for year_name in car_year_name]
        car_name = [year_name[5:] for year_name in car_year_name]
        
        car_price = [extract_number(price) for price in response.css(".sub-price::text").extract()]
        
        car_desc_km = response.css(".inventory-subtitle::text").extract()
        car_km = [extract_number(desc_km.split('|')[1]) for desc_km in car_desc_km]
        car_desc = [desc_km.split('|')[0] for desc_km in car_desc_km]
        
        car_specs = response.css(".inv-specs-value::text").extract()
        
        car_store = []
        car_engine = []
        car_gearbox = []
        car_fuel = []
        car_color = []
        
        for store, engine, gearbox, fuel, color in zip(car_specs[0::5], car_specs[1::5], car_specs[2::5], 
                                                    car_specs[3::5], car_specs[4::5]):
            car_store.append(store)
            car_engine.append(engine)
            car_gearbox.append(gearbox)
            car_fuel.append(fuel)
            car_color.append(color)
            
        row_data = zip(car_name, car_price, car_desc, car_store, car_engine, car_gearbox, car_fuel, car_color, car_km, car_year)
        
        for row in row_data:
            scraped_info = {
                "page": response.url,
                "car_name": row[0],
                "car_price": row[1],
                "car_km": row[8],
                "car_year": row[9],
                "car_desc": row[2],
                "car_store": row[3],
                "car_engine": row[4],
                "car_gearbox": row[5],
                "car_fuel": row[6],
                "car_color": row[7],
            }
            
            yield scraped_info