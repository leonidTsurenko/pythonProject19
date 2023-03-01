import requests

'''list_currency = []
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for elem in response_parse:
    if elem.startswith("$"):
        for elem2 in elem.split("</span>"):
            if elem2.startswith("$") and elem2[1].isdigit():
                list_currency.append(float(elem2.replace('$','').replace(',', '')))
                #print(elem2)

print(list_currency)
print(3 * list_currency[0])'''

from bs4 import BeautifulSoup

'''response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_text = soup.find_all("a", {"href" : "/currencies/bitcoin/markets/"})
    res = soup_text[0].find("span")
    print(res.text)'''

dic_curr = {}

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    cur_kod = soup.find_all("td", {"data-label": "Код літерний"})
    cur_val = soup.find_all("td", {"data-label": "Офіційний курс"})
    for i in range(len(cur_kod)):
        dic_curr[cur_kod[i].text] = cur_val[i].ext

print(dic_curr)
print(dic_curr['USD'])