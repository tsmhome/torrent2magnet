import re, requests, traceback
import bencode
import hashlib
from urllib.parse import quote
from bs4 import BeautifulSoup

url = input('請輸入網址： ')
r = requests.get(url) 
soup = BeautifulSoup(r.text, 'lxml')

def torrent_file_to_magnet(torrent_file):
    data =  r.content
    metadata = bencode.bdecode(data)
    name = metadata['info']['name']
    dn = quote(name)
    info_bts = bencode.bencode(metadata['info'])
    info_hash = hashlib.sha1(info_bts).hexdigest()
    return f'magnet:?xt=urn:btih:{info_hash}&dn={dn}'

if url.find('.torrent') > 0:
    fname = url[url.rfind('/')+1:]
    print(torrent_file_to_magnet(fname))
elif len(soup.find_all(class_="attachlist")) == 1:
    for link in soup.find_all(class_="attachlist")[0].find_all('a'):
        dl_link = "https://www.btbtt12.com/" + link.get('href').replace("dialog","download")
        r = requests.get(dl_link)
        d = r.headers['content-disposition']
        fname = re.findall('filename="(.+)"', d)
        print(torrent_file_to_magnet(fname))
else:
    table = int(input("頁面找到 "+str(len(soup.find_all(class_="attachlist")))+" 個表格，輸入你要下載的表格數值："))-1
    for link in soup.find_all(class_="attachlist")[int(table)].find_all('a'):
        dl_link = "https://www.btbtt12.com/" + link.get('href').replace("dialog","download")
        r = requests.get(dl_link)
        d = r.headers['content-disposition']
        fname = re.findall('filename="(.+)"', d)
        print(torrent_file_to_magnet(fname))