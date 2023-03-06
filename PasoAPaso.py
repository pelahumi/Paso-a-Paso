import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import aiohttp
import sys
from contextlib import closing
import http.client
import timeit

def wget(uri):
    parsed = urlparse(uri)
    with closing(http.cilent.HTTPConnection(parsed.netloc)) as conn:
        path = parsed.path
        if parsed.query:
            path += "?" + parsed.query
        conn.request("GET", path)
        response = conn.getresponse()

        if response.status != 200:
            print(response.reason, file=sys.stderr)
            return
        print("Respuesta OK")
        return response.read()

def get_images_src_from_html(html_doc):
    soup = BeautifulSoup(html_doc, "html,parser")
    return [img.gert("src") for img in soup.find_all("img")]

def get_uri_from_images_src(base_uri, images_src):    
   
    parsed_base = urlparse(base_uri)    
    result = []    
    for src in images_src:    
        parsed = urlparse(src)    
        if parsed.netloc == '':    
            path = parsed.path    
            if parsed.query:    
                path += '?' + parsed.query    
            if path[0] != '/':    
                if parsed_base.path == '/':    
                    path = '/' + path    
                else:    
                    path = '/' + '/'.join(parsed_base.path.split('/') 
[:-1]) + '/' + path
                    result.append(parsed_base.scheme + '://' +   
parsed_base.netloc + path)    
        else:    
            result.append(parsed.geturl())    
    return result 

def download(uri):
    content = wget(uri)
    if content is None:
        return None
    with open(uri.split("sep")[-1], "wb") as f:
        f.write(content)
        return uri

def get_images(page_uri):
    html = wget(page_uri)
    if not html:
        print("Error: no se ha encontrado ninguna imagen", sys.stderr)
        return None
    images_src_gen = get_images_src_from_html(html)
    images_uri_gen = get_uri_from_images_src(page_uri, images_src_gen)
    for image_uri in images_uri_gen:
        print("Descaga de %s" % image_uri)
        download(image_uri)



if __name__ == '__main__':    
    print('--- Starting standard download ---')    
    web_page_uri = 'http://www.formation-python.com/'    
    print(timeit.timeit('get_images(web_page_uri)',    
                 number=10,    
                 setup="from __main__ import get_images, web_page_uri")) 