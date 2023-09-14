import requests
from bs4 import BeautifulSoup
import pandas


html_src = requests.get('https://mylottokenya.co.ke/results/2').text
soup = BeautifulSoup(html_src, 'lxml')
data_html = soup.find('div', class_ = 'container')
colmn = data_html.find("div").text
#winning_nums = data_html.find('td', class_ = 'Winning Numbers')
print(colmn)
