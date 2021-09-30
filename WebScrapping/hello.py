from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3',class_='joblist-comp-name').text.replace('     ','')
    print(company_name,end='')
    skill = job.find('span',class_='srp-skills').text
    print(skill)
    link = job.find('a',class_='waves-effect waves-light btn')
    print(link.get('href'))

