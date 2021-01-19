from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find("li",class_="clearfix job-bx wht-shd-bx")
company = job.find('h3',class_="joblist-comp-name")
time = job.find('span', class_="sim-posted")
print(company.text.replace(" ","") + time.text.replace(" ",""))