#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
import sys

url = "http://data.fixer.io/api/latest?access_key=3c68051bdc3e029df1818d7d6223867b&format=1"
print("EURO DÖVİZ ÇEVİRİCİ")

birinci_doviz = "GBP"
ikinci_döviz = input("Çevirilecek döviz cinsini giriniz: ")
miktar = float(input("Tutar:"))


response = requests.get(url + birinci_doviz)

json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_döviz] * miktar)
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin")
    sys.stderr.flush()


# In[ ]:




