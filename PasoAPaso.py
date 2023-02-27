import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

url = "https://www.carrefour.es/?q=lavadora&scroll=VC4A-12690645"
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, "html.parser")

fichaProductos = soup.find_all("div", class_="ebx-result-figure__img")
i = 0
for element in fichaProductos:
    imagenProducto = element.find("img", class_="ebx-result-figure__img").get("src")
    print(imagenProducto)
    img = requests.get("https:"+imagenProducto)
    i = i + 1
    nombreImagen = "bosch"+ str(i)+".jpg"
    print(nombreImagen)

