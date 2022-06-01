import requests
from bs4 import BeautifulSoup
import random
from test import lst
headers={'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}



def requst(headers):

    for i in range (1,41):
        # time.sleep(random.randint(1,3))
        url = f'https://avto-russia.ru/pdd_cdc1d1/bilet{i}.html'
        html = requests.get(url=url,headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        link = soup.find_all('div', style='padding:5px; font-weight: bold;')



        for j in link:
            result = j.text[:1]
            with open('text2.txt', 'a', encoding='utf-8') as file:
                file.write(result.lower())



        with open('text2.txt', 'a', encoding='utf-8') as f:
            f.write(' ')
            for q in lst[i-1]:
                if not str(q).startswith('Билет'):
                    f.write(f'{q}')
            f.write(f' Билет № {i} \n')

if __name__ == '__main__':
    requst(headers=headers)





