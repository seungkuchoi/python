import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://wendys.tistory.com/174

print('Download corporate list from KRX...')
company_info_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
company_info_df.종목코드 = company_info_df.종목코드.map('{:06d}'.format)
# company_info_df = configDataFrame({'회사명':'name', '종목코드':'code'})

def configDataFrame(item):
    if type(item) is list:
        return company_info_df[item]
    elif type(item) is dict:
        company_code_df = company_info_df[item.keys()]
        return company_code_df.rename(columns=item)
    return company_info_df[item]

def getCompanyInfo(name, column, df=company_info_df):
    value = df.query("회사명=='{}'".format(name))[column]
    # To Do: query 이후 row 반환되면 list일텐데 자료형 다루는 방법 고민
    return value.to_string(index=False).strip()

def getCompanySource(code):
    base_url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&cID=&MenuYn=Y&gicode=A'
    response = requests.get(base_url + code)
    return response.text

class Company():
    def __init__(self, name):
        code = getCompanyInfo(name, '종목코드')
        source = getCompanySource(code)
        self.bs_obj = BeautifulSoup(source, 'lxml')

    def __str__(self):
        '''print(company)'''
        company_info = self.bs_obj.find('div', {'class':'ul_corpinfo'})
        name = company_info.find('h1').text
        code = company_info.find('h2').text
        return 'name: {}, code: {}'.format(name, code)

    def getPrice(self):
        price = self.bs_obj.find('span', {'id':'svdMainChartTxt11'})
        return price.text
