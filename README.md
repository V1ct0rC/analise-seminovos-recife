# Ciencia de Dados: Projeto 1
Primeiro projeto da cadeira de Introdução à Ciência de Dados (Tópicos Avançados em Gerenciamento de Dados e Informação)

<p align="justify">
Nesse proejto iremos realizar uma análise de dad os sobre um dataset de carros seminovos da cidade de Recife - PE. O dataset foi montado a partir de dados coletados por webscraping de diversos sites de vendas. O dataset contém informações sobre o preço, ano, quilometragem, marca, modelo, tipo de combustível, tipo de câmbio e cor dos veículos. O objetivo desse projeto é realizar uma análise exploratória dos dados, respondendo a algumas perguntas sobre o dataset e gerando visualizações que possam ajudar a entender melhor o dataset.

### Equipe:
Pedro Henrique Almeida Girão Peixinho (phagp) <br>
Victor Gabriel de Carvalho (vgc3)

### Tópicos Avançados em Gerenciamento de Dados e Informação IF697 - 2024.1 - Centro de Informáica UFPE

---

Para rodar o crawler, primeiro esteja na pasta inicial do projeto e ative o venv:
```
venv\Scripts\activate 
```
Com o ambiente virtual ativado, instale as bibliotecas necessárias:
```
pip install -r requirements.txt 
```
Agora, mude para o diretório do crawler e rode o arquivo base:
```
cd .\carscraper\ 

python main.py
```
As amostras obditas estarão no arquivo `cars.csv`.

---

## Dados Coletados

<p align="justify">
O dataset é composto por 1124 amostras com 12 features cada:

- **page**: URL da página de onde foi tirada a amostra.
- **car_brand**: Marca do veículo.
- **car_name**: Nome do veículo
- **car_price**: Preço do carro no momento da coleta.
- **car_km**: Quilometragem total do carro.
- **car_year**: Ano do modelo.
- **car_desc**: Descrição e informações gerais do veíclulo.
- **car_store**: Loja onde o carro está localizado.
- **car_engine**: Tamanho/Tipo do motor.
- **car_gearbox**: Tipo de embreagem.
- **car_fuel**: Tipo de combustível.
- **car_color**: Cor do automível.

## Pipeline do Projeto 1

1. **Coleta de Dados**: Coleta de dados de carros seminovos em sites de vendas.

2. **Pré-processamento dos Dados**
<br> Definição de tipos 
<br> Tratamento de dados ausentes
<br> Normalização e discretização
<br> Limpeza de dados (univariado, bivariado e multivariado)

3. **Estatísticas Descritivas com Visualizações**: Serão feitas juntamente com as outras etapas, para facilitar o entendimento dos dados.

4. **Testes de Hipótese**: Ao final, serão feitos testes de hipótese para responder a algumas perguntas sobre o dataset.

## Pipeline do Projeto 2

**Video explicando a implementação**<br>
https://drive.google.com/drive/folders/1eQBtHTzJ5Mjf3-6vFv9lFg_szz6_c5Se?usp=sharing