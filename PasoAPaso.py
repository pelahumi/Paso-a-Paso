import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_images_src_from_html(html_doc):       
    soup = BeautifulSoup(html_doc, "html.parser")    
    return (img.get('src') for img in soup.find_all('img')) 


