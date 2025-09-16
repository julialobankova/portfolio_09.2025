import pandas as pd
import requests
from bs4 import BeautifulSoup
from params import columns, name_file
import os
import stat
import shutil

def transform_currency_toy_store(data):
    try:
        if len(data) == 2 and data[1] == '₽':
            return data[0]
        elif len(data) == 3 and data[2] == '₽':
            if data[1].startswith('₽'):
                return data[1][1:]
            elif data[0] == 'от' and data[2] == '₽':
                data[1]
            else:
                return data[0] + data[1]
        elif len(data) == 4 and data[0] == 'от' and data[3] == '₽':
            return data[1] + data[2]
        elif len(data) == 3 and data[0] == 'от' and data[2] == '₽':
            return data[1]
    except Exception as e:
        print(f'Ошибка при трансформации цены товара {e}')


def save_to_csv(columns, name_file, data):
    try:
        if data:
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(f'{name_file}', index=False, encoding='utf-8')
            os.chmod(name_file, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
            shutil.chown(name_file, user='postgres', group='postgres')
    except Exception as e:
        print(f'Ошибка при сохранение результата парсинга в csv {e}')
        
        

def pars_save_to_csv(columns, name_file):      
  try:
      url = 'https://www.toys-land.ru/catalog/igry-i-igrushki/?show=100000'
      response = requests.get(url)
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
  
      names = soup.find_all(class_='name')
      brands = soup.find_all(class_='firm')
      articles = soup.find_all(class_='art')
      price = soup.find_all(class_='price')
      if names:
          result_pars = [
              (
                  name.get_text(strip=True),
                  brand.get_text(strip=True).split(':')[1] if ':' in brand.get_text(strip=True) else brand.get_text(
                      strip=True),
                  article.get_text(strip=True).split(':')[1] if ':' in article.get_text(strip=True) else article.get_text(
                      strip=True),
                  transform_currency_toy_store(price.get_text(strip=True).split())
              )
              for name, brand, article, price in zip(names, brands, articles, price)
          ]
  
      save_to_csv(columns, name_file, result_pars)
  
  
  except Exception as e:
      print(f'Ошибка при парсинге {e}')



       
def copy_command(user,db_name,host,port,your_table,name_file,delimiter,file_format,mean_header):
  try:
      copy = f"psql -U {user} -d {db_name} -h {host} -p {port} -c \"\COPY {your_table} FROM '{name_file}' WITH (FORMAT '{file_format}', DELIMITER '{delimiter}', HEADER {mean_header});\""
      return copy
  except Exception as e:
      print(f'Ошибка COPY {e}')  
