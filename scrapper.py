import requests


url = "https://www.ouedkniss.com/appartement-vente-f4-chlef-tenes-algerie-d35916540"
resp = requests.get(url)

with open('results.txt', 'w')as file :
    file.write(resp.text)