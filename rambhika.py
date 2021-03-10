import requests,bs4
res = requests.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1")
soup = bs4.BeautifulSoup(res.content,features="html.parser")
el = soup.findAll(attrs={"class": "product"})
li = []
for div in el:
    price = div.find('span',attrs={'class':"price"}).text
    title = div.find('span',attrs={'class':"price"}).text
    brand = div.find('a',attrs={"class":"catalog-item-brand"}).text
    out_of_stock = div.find('span',attrs={"class":"out-of-stock"}).text
    if out_of_stock == "Out of Stock":
        out_of_stock = True

    else:
        out_of_stock = False
    li.append({"Price":price,
               "title":title,
               "out_of_stock":out_of_stock,
               "brand":brand})

print(li)
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
ua = UserAgent()
proxies = []
def main():
    proxies_req = Request('https://www.sslproxies.org/' )
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
        'ip':   row.find_all('td')[0].string,
        'port': row.find_all('td')[1].string
  })
  
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]
  
    for n in range(1, 100):
        req = Request('https://www.freeproxylists.net/')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

        if n % 10 == 0:
            proxy_index = random_proxy()
            proxy = proxies[proxy_index]
        try:
          my_ip = urlopen(req).read().decode('utf8')
          print('#' + str(n) + ': ' + my_ip)
        except: 
          del proxies[proxy_index]
          print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
          proxy_index = random_proxy()
          proxy = proxies[proxy_index]
def random_proxy():
  return random.randint(0, len(proxies) - 1)

if __name__ == '__main__':
  main()   

  

