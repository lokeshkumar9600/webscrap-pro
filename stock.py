from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable 
from datetime import date
today = date.today()
d1= today.strftime("%d-%m-%Y")
columns = ["StockName","CompanyName","Price","Change","%Change"] 
myTable = PrettyTable() 
file =open(f"stockgain/topGainers{d1}.txt",'w')
stks = []
cpy_name =[]
p =[]
change =[]
pchange =[]
main_html = requests.get("https://in.finance.yahoo.com/gainers").text
soup = BeautifulSoup(main_html,"lxml")
main_gain = soup.find_all("tr",class_="simpTblRow")
for j in main_gain:
    stks.append(j.td.a.text)
    price = j.find_all("td",class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)")
    p.append(price[0].text)
    change.append(price[1].text)
    pchange.append(price[2].text)
    cpy_nam = j.find_all("td",class_="Va(m) Ta(start) Px(10px) Fz(s)")
    for x in cpy_nam:
        cpy_name.append(x.text)
myTable.add_column(columns[0],stks) 
myTable.add_column(columns[1],cpy_name) 
myTable.add_column(columns[2],p) 
myTable.add_column(columns[3],change)
myTable.add_column(columns[4],pchange) 
file.write(str(myTable))
file.close()




