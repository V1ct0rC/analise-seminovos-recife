import scrapy
from utils import extract_number, extract_engine_size

class CarAzzurraSpider(scrapy.Spider):
    name = 'Azzurra'
    start_urls = [
        "https://azzurraseminovos.com.br/busca/pagina/",
        "https://azzurraseminovos.com.br/busca/pagina/15",
        "https://azzurraseminovos.com.br/busca/pagina/30",
        "https://azzurraseminovos.com.br/busca/pagina/45",
        "https://azzurraseminovos.com.br/busca/pagina/60",
        "https://azzurraseminovos.com.br/busca/pagina/75",
        "https://azzurraseminovos.com.br/busca/pagina/90",
        "https://azzurraseminovos.com.br/busca/pagina/105",
        "https://azzurraseminovos.com.br/busca/pagina/120",
        "https://azzurraseminovos.com.br/busca/pagina/135",
        "https://azzurraseminovos.com.br/busca/pagina/150",
        "https://azzurraseminovos.com.br/busca/pagina/165",
        "https://azzurraseminovos.com.br/busca/pagina/180",
        "https://azzurraseminovos.com.br/busca/pagina/195",
        "https://azzurraseminovos.com.br/busca/pagina/210"
        ]

    def parse(self, response):
        car_price = [extract_number(price) for price in response.css('span.valor::text').extract()]
        
        car_brand_name_desc_engine = response.css('.pos-relative.title::text').re(r'\s*(\S.*\S)\s*')
        car_name = [' '.join(brand_name_desc_engine.split(' ')[0:2]) for brand_name_desc_engine in car_brand_name_desc_engine]
        car_desc = [' '.join(brand_name_desc_engine.split(' ')[2:]) for brand_name_desc_engine in car_brand_name_desc_engine]
        car_engine = [extract_engine_size(brand_name_desc_engine) for brand_name_desc_engine in car_brand_name_desc_engine]
        
        car_specs = response.css(".specs::text").re(r'\s*(\S.*\S)\s*')
        
        car_year = response.css('p.m-0.date::text').extract()
        car_km = [extract_number(km) for km in response.css('p.m-0.km::text').extract()]
        car_fuel_gearbox_color = response.css('.col-xs-4.col-xl-4.px-0 p.m-0.cambio.font-10::text').extract()
        
        car_fuel = []
        car_gearbox = []
        car_color = []
        
        for fuel, gearbox, color in zip(car_fuel_gearbox_color[0::3], car_fuel_gearbox_color[1::3], car_fuel_gearbox_color[2::3]):
            gearbox = 'Manual' if 'MANUAL' in gearbox else 'Automatico'
            fuel = "Flex" if "FLEX" in fuel else fuel
            car_fuel.append(fuel)
            car_gearbox.append(gearbox)
            car_color.append(color.title())
            
        row_data = zip(car_name, car_price, car_year, car_km, car_fuel, car_gearbox, car_desc, car_engine, car_color)
        
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
                "car_gearbox": row[5],
                "car_fuel": row[4],
                "car_color": row[8],
            }
            
            yield scraped_info	