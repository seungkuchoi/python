import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://wendys.tistory.com/174

print('Download corporate list from KRX...')
company_info_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
company_info_df.종목코드 = company_info_df.종목코드.map('{:06d}'.format)
# company_info_df = configDataFrame({'회사명':'name', '종목코드':'code'})

def configDataFrame(item, df=company_info_df):
    if type(item) is list:
        return df[item]
    elif type(item) is dict:
        company_code_df = df[item.keys()]
        return company_code_df.rename(columns=item)
    return df[item]

def getCompanyInfo(name, df=company_info_df):
    value = df.query("회사명=='{}'".format(name))
    # To Do: query 이후 row 반환되면 list일텐데 자료형 다루는 방법 고민
    if value.empty is True:
        raise ValueError
    return value

def getCompanySource(code):
    base_url = 'https://finance.naver.com/item/main.nhn?code='
    response = requests.get(base_url + code)
    return response.text

def num(text) -> int or float:
    num = text.replace(',','').replace('%','')
    if '.' in num:
        return float(num)
    return int(num)

class Company():
    def __init__(self, name):
        self.name = name
        try:
            company_info = getCompanyInfo(self.name) #xlxs type
        except ValueError:
            print('Invalid company name')
        else:
            self.code = company_info['종목코드'].to_string(index=False).strip()
            source = getCompanySource(self.code)
            self.bs_obj = BeautifulSoup(source, 'lxml')
        finally:
            self.info = self.parseInfo()
            self.price = self.parsePrice()
            self.consensus = self.parConsensus()

    def __str__(self):
        '''print(stock_info)'''
        return '{}'.format(self.name)

    def parseInfo(self, item=None):
        info = {'name':'', 'code':'', 'market':''}
        try:
            wrap_company = self.bs_obj.find('div', {'class':'wrap_company'})
            name = wrap_company.find('h2')

            description = wrap_company.find('div', {'class':'description'})
            code = description.find('span', {'class':'code'})
            market = description.find('img')['alt']

            info = {'name':name.text, 'code':code.text, 'market':market}
        finally:
            return info

    # 한번 이상 호출되면 parse 다른 곳으로 이동
    def parsePrice(self, item=None):
        price = {'close':0,'diff_prev':0,'rate_prev':0}
        try:
            price_info = self.bs_obj.find('div', {'class':'rate_info'})

            today = price_info.find('p', {'class':'no_today'})
            close = today.find('span', {'class':'blind'}) #종가

            yesterday = price_info.find('p', {'class':'no_exday'}).findAll('em')
            diff_prev = yesterday[0].find('span', {'class':'blind'}) #전일비
            rate_prev = yesterday[1].find('span', {'class':'blind'}) #전일비%
            
            up_down = '+'
            if yesterday[0].find('span', {'class':'ico down'}):
                up_down = '-'

            price = {'close':num(close.text),
                    'diff_prev':num(up_down + diff_prev.text),
                    'rate_prev':num(up_down + rate_prev.text)}
        finally:
            return price

    def parConsensus(self): #투자 정보
        consensus = {'invest_opinion':0, 'target_price':0}
        try:
            invest_info = self.bs_obj.find('div', {'class':'aside_invest_info'})
            table = invest_info.find('table', {'class':'rwidth'}).findAll('td')
            invest_opinion = num(table[0].findAll('em')[0].text)
            target_price = num(table[0].findAll('em')[1].text)

            consensus = {'invest_opinion':invest_opinion, 
                        'target_price':target_price}
        finally:
            return consensus
