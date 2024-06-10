import scrapy
from utils import extract_number, extract_engine_size

class CarUsadosBRSpider(scrapy.Spider):
    name = 'UsadosBR'
    start_urls = [
        "https://www.usadosbr.com/carros/pe/recife",
        "https://www.usadosbr.com/carros/pe/recife?pagina=2",
        "https://www.usadosbr.com/carros/pe/recife?pagina=3",
        "https://www.usadosbr.com/carros/pe/recife?pagina=4",
        "https://www.usadosbr.com/carros/pe/recife?pagina=5",
        "https://www.usadosbr.com/carros/pe/recife?pagina=6",
        "https://www.usadosbr.com/carros/pe/recife?pagina=7",
        "https://www.usadosbr.com/carros/pe/recife?pagina=8",
        "https://www.usadosbr.com/carros/pe/recife?pagina=9",
        "https://www.usadosbr.com/carros/pe/recife?pagina=10",
        "https://www.usadosbr.com/carros/pe/recife?pagina=11",
        "https://www.usadosbr.com/carros/pe/recife?pagina=12",
        "https://www.usadosbr.com/carros/pe/recife?pagina=13",
        "https://www.usadosbr.com/carros/pe/recife?pagina=14",
        "https://www.usadosbr.com/carros/pe/recife?pagina=15",
        "https://www.usadosbr.com/carros/pe/recife?pagina=16",
        "https://www.usadosbr.com/carros/pe/recife?pagina=17",
        "https://www.usadosbr.com/carros/pe/recife?pagina=18",
        "https://www.usadosbr.com/carros/pe/recife?pagina=19",
        "https://www.usadosbr.com/carros/pe/recife?pagina=20",
        "https://www.usadosbr.com/carros/pe/recife?pagina=21",
        "https://www.usadosbr.com/carros/pe/recife?pagina=22",
        "https://www.usadosbr.com/carros/pe/recife?pagina=23",
        "https://www.usadosbr.com/carros/pe/recife?pagina=24",
        "https://www.usadosbr.com/carros/pe/recife?pagina=25",
        "https://www.usadosbr.com/carros/pe/recife?pagina=26",
        "https://www.usadosbr.com/carros/pe/recife?pagina=27",
        "https://www.usadosbr.com/carros/pe/recife?pagina=28",
        "https://www.usadosbr.com/carros/pe/recife?pagina=29",
        "https://www.usadosbr.com/carros/pe/recife?pagina=30",
        "https://www.usadosbr.com/carros/pe/recife?pagina=31",
        "https://www.usadosbr.com/carros/pe/recife?pagina=32",
        "https://www.usadosbr.com/carros/pe/recife?pagina=33",
        "https://www.usadosbr.com/carros/pe/recife?pagina=34",
        "https://www.usadosbr.com/carros/pe/recife?pagina=35",
        "https://www.usadosbr.com/carros/pe/recife?pagina=36",
        "https://www.usadosbr.com/carros/pe/recife?pagina=37",
        "https://www.usadosbr.com/carros/pe/recife?pagina=38",
        "https://www.usadosbr.com/carros/pe/recife?pagina=39"
        ]

    def parse(self, response):  
        car_price = [extract_number(price) for price in response.css(".css-1e6famu::text").extract() ]
        
        car_brand = response.css(".css-8i3pvs::text").extract()
        
        car_name = [f'{brand} {name}' for brand, name in zip(car_brand, response.css(".css-jnq6z6::text").extract())]
        
        car_desc_engine_gearbox = response.css(".css-kufh1x::text").extract()
        car_engine = [extract_engine_size(desc_engine_gearbox) for desc_engine_gearbox in car_desc_engine_gearbox]
        car_gearbox = ['Manual' if 'Manual' in desc_engine_gearbox else 'Automatico' for desc_engine_gearbox in car_desc_engine_gearbox]
        car_desc = car_desc_engine_gearbox
        
        car_year_km_fuel = response.css(".css-ljtdvh p::text").extract()
        car_year = []
        car_km = []
        car_fuel = []
        for year, km, fuel in zip(car_year_km_fuel[0::3], car_year_km_fuel[1::3], car_year_km_fuel[2::3]):
            car_year.append(year[5:])
            car_km.append(extract_number(km))
            fuel = "Flex" if "Á/G" in fuel else fuel
            car_fuel.append(fuel)
        
        row_data = zip(car_name, car_price, car_year, car_km, car_fuel, car_engine, car_gearbox, car_desc)
        
        for row in row_data:
            scraped_info = {
                "page": response.url,
                "car_brand": row[0].partition(" ")[0].title(),
                "car_name": row[0].partition(" ")[2].title(),
                "car_price": row[1],
                "car_km": row[3],
                "car_year": row[2],
                "car_desc": row[7],
                "car_store": None,
                "car_engine": row[5],
                "car_gearbox": row[6],
                "car_fuel": row[4],
                "car_color": None,
            }
            
            yield scraped_info