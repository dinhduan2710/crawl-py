import requests
import numpy as np
from bs4 import BeautifulSoup
with open('data.csv', 'w', encoding='utf-8') as w:
    w.write('TO,NV,SU,DI,VL,HH,SH,NN,GD\n')
    for idx in range(27000001, 27999999):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
        url = 'https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/{}.html'.format(idx)
        page = requests.get(url,headers)
        if page.status_code == 404:
            print("[GET] {}/27999999".format(idx))
            soup = BeautifulSoup(page.text, "html.parser")
            parent = soup.find_all("div", {"class": "resultSearch__right"})
            elements = soup.find_all("td")
            n = 2
            elements = [elements[i:i+n] for i in range(0, len(elements), n)]

            subjects = {'Toán': '', 'Văn': '', 'Sử': '', 'Địa': '', 'Lí': '',
                        'Hoá': '', 'Sinh': '', 'Ngoại ngữ': '', 'GDCD': ''}
            for element in elements:
                for key, value in subjects.items():
                    if element[0].text == key:
                        subjects[key] = element[1].text
            line = ','.join([v for v in subjects.values()])
            w.write(line + '\n')
        else:
            print("[INFO] {}/27999999: no data".format(idx))
