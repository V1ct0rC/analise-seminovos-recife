import scrapy
import re

class CarSpider(scrapy.Spider):
    name = "car_spider"
    start_urls = [
        "https://www.pedragonchevroletrecife.com.br/seminovos?condicao=seminovo",
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
        "https://grupoautonunes.com/estoque/?zero_km=0&txt_busca=&page=21",
        "https://www.italianaseminovos.com.br/estoque?page=1",
        "https://www.italianaseminovos.com.br/estoque?page=2",
        "https://www.italianaseminovos.com.br/estoque?page=3",
        "https://www.italianaseminovos.com.br/estoque?page=4",
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
        "https://azzurraseminovos.com.br/busca/pagina/210",
        "https://www.disnove.com.br/seminovos/",
        "https://www.disnove.com.br/seminovos/9",
        "https://www.disnove.com.br/seminovos/18",
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
        "https://www.usadosbr.com/carros/pe/recife?pagina=39",
        # TODO: Add the URLs of the websites you want to scrape
        # TODO: There should be a better way to do this
    ]
    
    
    def extract_number(self, price_text):
        """
        Extracts and converts a price string to a float.
        
        Args:
        price_text (str): The price string to be processed, e.g., "Preço R$ 73.480,00".
        
        Returns:
        float: The price as a float, e.g., 73480.00.
        """
        # Remove all non-numeric characters except for ',' and '.'
        cleaned_price = re.sub(r'[^\d,]', '', price_text)
        
        # Replace the comma with a period to convert to a float
        cleaned_price = cleaned_price.replace('.', '').replace(',', '.')
        
        # Convert the cleaned string to a float
        price_float = float(cleaned_price)
        
        return price_float
    
    
    def extract_engine_size(self, car_description):
        """
        Extracts the engine size from a car description string.
        
        Args:
        car_description (str): The car description string, e.g., "TRACKER LT 1.4 Turbo 16V Flex 4x".
        
        Returns:
        str: The engine size, e.g., "1.4". Returns None if no match is found.
        """
        # Define the regular expression pattern to match engine sizes like "1.0", "1.4", etc.
        pattern = r'\b\d\.\d\b'
        
        # Search for the pattern in the car description
        match = re.search(pattern, car_description)
        
        # If a match is found, return the matched string; otherwise, return None
        return match.group() if match else None
    
    
    def parse(self, response):
        print("procesing:"+response.url)
        
        # PEDRAGON
        if 'pedragon' in response.url:
            car_year_name = response.css(".inventory-title::text").extract()
            car_year = [year_name.split(' ')[0] for year_name in car_year_name]
            car_name = [year_name[5:] for year_name in car_year_name]
            
            car_price = [self.extract_number(price) for price in response.css(".sub-price::text").extract()]
            
            car_desc_km = response.css(".inventory-subtitle::text").extract()
            car_km = [self.extract_number(desc_km.split('|')[1]) for desc_km in car_desc_km]
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
        
        # AUTONUNES
        if 'autonunes' in response.url:
            car_price = [self.extract_number(price) for price in response.css(".valor::text").re(r'\s*(\S.*\S)\s*')]
            
            car_name = response.css("span.nome-do-carro strong::text").extract()
            
            car_engine_desc_gearbox = response.css(".versao.px-3.mt-3.mb-1::text").re(r'\s*(\S.*\S)\s*')
            car_engine = [engine_desc[:3] if "ELÉTRICO" not in engine_desc else None for engine_desc in car_engine_desc_gearbox]
            car_desc = [engine_desc[4:] if "ELÉTRICO" not in engine_desc else engine_desc for engine_desc in car_engine_desc_gearbox]
            car_gearbox = ['Manual' if 'MANUAL' in engine_desc else 'Automatico' for engine_desc in car_engine_desc_gearbox]
            
            car_specs = response.css('.car-icon::text').re(r'\s*(\S.*\S)\s*')
            
            car_year = []
            car_km = []
            car_fuel = []
            
            for year, km, fuel in zip(car_specs[0::3], car_specs[1::3], car_specs[2::3]):
                car_year.append(year[5:])
                car_km.append(self.extract_number(km))
                car_fuel.append(fuel)
                
            row_data = zip(car_name, car_price, car_desc, car_year, car_km, car_fuel, car_engine, car_gearbox)
            
            for row in row_data:
                scraped_info = {
                    "page": response.url,
                    "car_name": row[0],
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
        
        # ITALIANA
        if 'italiana' in response.url:
            car_price = [self.extract_number(price) for price in response.css(".text-primary.font-weight-bold::text").extract()]
            
            car_brand = response.css(".text-muted.text-uppercase.font-size-12::text").extract()
            
            car_name_engine_desc_gearbox = response.css(".text-uppercase.font-weight-bold.font-size-14.text-center.mb-2::text").extract()
            car_name = [f'{car_brand[i]} {name_engine_desc_gearbox.split(" ")[0]}' for i, name_engine_desc_gearbox in enumerate(car_name_engine_desc_gearbox)]
            car_engine = [name_engine_desc_gearbox.split(" ")[1] for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
            car_desc = [' '.join(name_engine_desc_gearbox.split(" ")[2:]) for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
            car_gearbox = ['Manual' if 'MANUAL' in name_engine_desc_gearbox else 'Automatico' for name_engine_desc_gearbox in car_name_engine_desc_gearbox]
            
            car_specs = response.css(".mb-0.font-size-12.text-muted::text").re(r'\s*(\S.*\S)\s*')
            
            car_year = []
            car_km = []
            for km, year in zip(car_specs[0::2], car_specs[1::2]):
                car_year.append(year[5:])
                car_km.append(self.extract_number(km))
                
            row_data = zip(car_name, car_price, car_desc, car_year, car_km, car_engine, car_gearbox)
            
            for row in row_data:
                scraped_info = {
                    "page": response.url,
                    "car_name": row[0],
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
                
        #AZZURRA
        if 'azzurra' in response.url:
            car_price = [self.extract_number(price) for price in response.css('span.valor::text').extract()]
            
            car_brand_name_desc_engine = response.css('.pos-relative.title::text').re(r'\s*(\S.*\S)\s*')
            car_name = [' '.join(brand_name_desc_engine.split(' ')[0:2]) for brand_name_desc_engine in car_brand_name_desc_engine]
            car_desc = [' '.join(brand_name_desc_engine.split(' ')[2:]) for brand_name_desc_engine in car_brand_name_desc_engine]
            car_engine = [self.extract_engine_size(brand_name_desc_engine) for brand_name_desc_engine in car_brand_name_desc_engine]
            
            car_specs = response.css(".specs::text").re(r'\s*(\S.*\S)\s*')
            
            car_year = response.css('p.m-0.date::text').extract()
            car_km = [self.extract_number(km) for km in response.css('p.m-0.km::text').extract()]
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
                
        # DISNOVE
        if 'disnove' in response.url:
            car_price = [self.extract_number(price) for price in response.css(".color-blue-light.font-weight-bold.font-24.text-center.mb-2::text").extract()]
            
            car_brand = response.css('.font-12.color-dark.text-uppercase.p-0.m-0::text').extract()
            
            car_name_engine_desc_gearbox = response.css('.font-18.color-navy.text-uppercase.p-0.m-0::text').extract()
            car_name = [f'{brand} {name_desc.split(" ")[0]}' for brand, name_desc in zip(car_brand, car_name_engine_desc_gearbox)]
            car_desc = [' '.join(name_desc.split(" ")[1:]) for name_desc in car_name_engine_desc_gearbox]
            car_engine = [self.extract_engine_size(name_desc) for name_desc in car_name_engine_desc_gearbox]
            car_gearbox = ['Manual' if 'MANUAL' in name_desc else 'Automatico' for name_desc in car_name_engine_desc_gearbox]
            
            car_year_fuel_km_color = response.css(".font-14.color-dark.p-0.m-0.pt-2::text").extract()
            
            car_year = []
            car_fuel = []
            car_km = []
            car_color = []
            
            for year, fuel, km, color in zip(car_year_fuel_km_color[0::4], car_year_fuel_km_color[1::4], car_year_fuel_km_color[2::4], car_year_fuel_km_color[3::4]):
                car_year.append(year)
                car_fuel.append(fuel)
                car_km.append(self.extract_number(km))
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
        
        # USADOSBR
        if 'usadosbr' in response.url:
            car_price = [self.extract_number(price) for price in response.css(".css-1e6famu::text").extract() ]
            
            car_brand = response.css(".css-8i3pvs::text").extract()
            
            car_name = [f'{brand} {name}' for brand, name in zip(car_brand, response.css(".css-jnq6z6::text").extract())]
            
            car_desc_engine_gearbox = response.css(".css-kufh1x::text").extract()
            car_engine = [self.extract_engine_size(desc_engine_gearbox) for desc_engine_gearbox in car_desc_engine_gearbox]
            car_gearbox = ['Manual' if 'Manual' in desc_engine_gearbox else 'Automatico' for desc_engine_gearbox in car_desc_engine_gearbox]
            car_desc = car_desc_engine_gearbox
            
            car_year_km_fuel = response.css(".css-ljtdvh p::text").extract()
            car_year = []
            car_km = []
            car_fuel = []
            for year, km, fuel in zip(car_year_km_fuel[0::3], car_year_km_fuel[1::3], car_year_km_fuel[2::3]):
                car_year.append(year[5:])
                car_km.append(self.extract_number(km))
                fuel = "Flex" if "Á/G" in fuel else fuel
                car_fuel.append(fuel)
            
            row_data = zip(car_name, car_price, car_year, car_km, car_fuel, car_engine, car_gearbox, car_desc)
            
            for row in row_data:
                scraped_info = {
                    "page": response.url,
                    "car_name": row[0],
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