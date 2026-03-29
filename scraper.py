import requests as req
from bs4 import BeautifulSoup
import time

url = "https://www.booli.se/sok/slutpriser?areaIds=393&objectType=L%C3%A4genhet"

headers = {

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0'  

}

res = req.get(url, headers = headers)

if(res.status_code == 200):
    soup = BeautifulSoup(res.text, 'html.parser') 
    print("samir badran")
else:
    print("viktor", res.status_code)