from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://mushmula.ru/'
responce = requests.get(url)

#print(responce.status_code)

soup = BeautifulSoup(responce.text, "html.parser")


names = soup.find_all('header', class_='b-item__header')
descriptions = soup.find_all('div', class_='b-item__description')
costs = soup.find_all('div', class_='b-item__price')


filtered_names = []
filtered_descriptions = []
filtered_costs = []
filtered_summary = []

for name, description, cost in zip(names, descriptions, costs):
    title = name.find('h2', class_='b-item__title').text.strip() 
    cost = cost.find('span', class_='b-item__price-value').text.strip()
    desc = description.find('span', class_='b-item__description-info').text.strip()
    if title is not None or desc is not None or cost is not None:
        filtered_summary.append((title, desc, cost))

df = pd.DataFrame(filtered_summary, columns=['Name', 'Description', 'Cost'])
df.to_csv('FileData.csv', index=False, encoding='utf-8')

md = df['Cost'].mode() #Считаем моду по цене
dp = (df['Cost'].astype(float)).var() #Считаем дисперсию по цене
stok = (df['Cost'].astype(float)).std() #Считаем стандартное отклонение



url_salade = 'https://mushmula.ru/menu/salaty/'
responce_salade = requests.get(url_salade)
salade_soup = BeautifulSoup(responce_salade.text, "html.parser")

names_salade = salade_soup.find_all('header', class_='b-item__header')
descriptions_salade = salade_soup.find_all('div', class_='b-item__description')
costs_salade = salade_soup.find_all('div', class_='b-item__price')

filtered_names_salade = []
filtered_descriptions_salade = []
filtered_costs_salade = []
filtered_summary_salade = []

for name_salade, description_salade, cost_salade in zip(names_salade, descriptions_salade, costs_salade):
    title_salades = name_salade.find('h2', class_='b-item__title').text.strip() 
    cost_salades = cost_salade.find('span', class_='b-item__price-value').text.strip()
    desc_salades = description_salade.find('span', class_='b-item__description-info').text.strip()
    if title_salades is not None or desc_salades is not None or cost_salades is not None:
        filtered_summary_salade.append((title_salades, desc_salades, cost_salades))

df_salade = pd.DataFrame(filtered_summary_salade, columns=['Name', 'Description', 'Cost'])
df_salade.to_csv('SaladeData.csv', index=False, encoding='utf-8')
#df_salade['Cost'].hist(bins = 15)




url_desert = 'https://mushmula.ru/menu/deserty/'
responce_desert = requests.get(url_desert)
desert_soup = BeautifulSoup(responce_desert.text, "html.parser")

names_desert = desert_soup.find_all('header', class_='b-item__header')
descriptions_desert = desert_soup.find_all('div', class_='b-item__description')
costs_desert = desert_soup.find_all('div', class_='b-item__price')

filtered_names_desert = []
filtered_descriptions_desert = []
filtered_costs_desert = []
filtered_summary_desert = []

for name_desert, description_desert, cost_desert in zip(names_desert, descriptions_desert, costs_desert):
    title_deserts = name_desert.find('h2', class_='b-item__title').text.strip() 
    cost_deserts = cost_desert.find('span', class_='b-item__price-value').text.strip()
    desc_deserts = description_desert.find('span', class_='b-item__description-info').text.strip()
    if title_deserts is not None or costs_desert is not None or desc_deserts is not None:
        filtered_summary_desert.append((title_deserts, desc_deserts, cost_deserts))

df_desert = pd.DataFrame(filtered_summary_desert, columns=['Name', 'Description', 'Cost'])
df_desert.to_csv('DesertData.csv', index=False, encoding='utf-8')
#df_desert['Cost'].hist(bins = 15)
print(df_desert)
#plt.show()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = df_salade['Cost'].hist(bins = 15, alpha = 0.5, label ='Цены салатов')
df_desert['Cost'].hist(bins = 15, alpha = 0.5, ax=ax, label ='Цены десертов')
plt.legend()
plt.title("Распределение цены салатов/десертов")
plt.show()
