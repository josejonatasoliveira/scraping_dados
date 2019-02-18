from bs4 import BeautifulSoup as bs
import requests
import pymongo
from config_data import DATABASE_NAME
import config_data as cfg

client = pymongo.MongoClient(cfg.CONECTION_STRING)
url = cfg.SITE_NAME


s = requests.Session()
r = s.get(url)
soup = bs(r.content,'html.parser')

site = soup.find('div',id='ipp-q2')
tabelas = site.find('tbody') # Conteudo das tabelas

cabecalho = site.find('thead')
head = cabecalho.find('tr',attrs={'tabela-linha-classificacao'}) #Cabeçalho das tabelas

db = client.DATABASE_NAME

    
for td in tabelas:
    th = td.find('th') #Nome das colunas da tabela do site
    if (',' in th.text):
        collection_name = th.text.split(',')[0].replace(' ','_')
    else:
        collection_name = th.text.replace(' ','_')
    lista = []
    
    for value in td.find_all('td'):
        lista.append(value.text)
        
    dados = {}
    
    n_cabecalho = []
    for th in head.find_all('th'):
        n_cabecalho.append(th.text)
        
    for i in range(1, len(n_cabecalho) - 1):
        print(n_cabecalho[i])
        dados[n_cabecalho[i]] = lista[i]
        
    collection = db[collection_name]
    collection.insert_one(dados)
    
    
