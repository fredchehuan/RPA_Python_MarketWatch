from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import json
import datetime as dt
import csv

x=0
req= Request("https://www.marketwatch.com/", headers={'User-Agent':'Mozilla/5.0'})

#TRATANDO ERROS HTTP
try:
    #html = urlopen("https://www.marketwatch.com/")
    html = urlopen(req).read()
    x=1
except HTTPError as erro:
    x=0
    print("Ocorreu um erro HTTP: {erro}")

#TRATANDO ERROS DE URL
try:
    #html = urlopen("https://www.marketwatch.com/")
    html = urlopen(req).read()
except URLError as erro:
    x=0
    print("Ocorreu um erro de URL: {erro}")

if (x==1) :
    #obj = BeautifulSoup(html.read(), "html.parser")
    obj = BeautifulSoup(html, "html.parser")

    #TRATANDO ERROS DE ATRIBUTOS NÃO ENCONTRADOS
    try:
        movers = obj.find("div",{"class":"element--movers"})
        #movers = movers.select("span.mover__symbol")

        #print("------Movers------")
        #print(movers)

        moversSimbol = list(i.get_text() for i in movers.select("span.mover__symbol"))
        print("------Movers SIMBOL------")
        print(moversSimbol)

        moversSimbol = list(i.get_text() for i in movers.find_all("bg-quote",{"field":"percentChange"}))
        print("------Movers SIMBOL------")
        print(moversSimbol)
        
        

        '''markets = obj.find("tbody",{"class":"markets__group"})
                
        itemSimbol = list(i.get_text() for i in markets.select("td.symbol a"))
        itemPrice = list(i.get_text() for i in markets.select("td.price bg-quote"))
        itemChange = list(i.get_text() for i in markets.select("td.change bg-quote"))
        itemPercent = list(i.get_text() for i in markets.select("td.percent bg-quote")) 
        
        #montando objetos
        item = list({'Simbol': itemSimbol[i],
                'Price': itemPrice[i],
                'Change': itemChange[i],
                'Percent': itemPercent[i]} for i in range(len(itemSimbol)))
        
        #montando dicionário para json
        item_dict = {str(dt.datetime.now()): item} 
        
        #escrevendo json
        json_item = json.dumps(item_dict)
        
        #escrevendo csv
        with open('{}.csv'.format(str(dt.datetime.now()).replace('.', '_').replace(':', '-')), 'w') as f:
            dict_writer = csv.DictWriter(f, item[0].keys())
            dict_writer.writeheader()
            dict_writer.writerows(item)
        
        print ("\n\n------PRINT Simbol------")
        print (itemSimbol)
        print ("\n\n------PRINT pricing------")
        print (itemPrice)
        print ("\n\n------PRINT Change------")
        print (itemChange)
        print ("\n\n------PRINT Percent------")
        print (itemPercent)
        print ("\n\n------PRINT Item------")
        print (json_item)'''

    except AttributeError as erro:
        print("Ocorreu um erro de busca em um atributo HTML: {erro}")
        print(erro)

        
        
#python teste.py