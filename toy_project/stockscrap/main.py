# day1 get information from web site

import pandas as pd
from bs4 import BeautifulSoup

# https://wendys.tistory.com/174

print('Download corperate list from KRX...')
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
#code_df = code_df[['회사명', '종목코드']]
code_df = code_df.rename(columns={'회사명':'name', '종목코드':'code'})
code_df.code = code_df.code.map('{:06d}'.format)

def getCompanyCode(company_name):
    code = code_df.query("name=='{}'".format(company_name))['code'].to_string(index=False)
    return code.strip()

print(getCompanyCode('LG전자'))
print(getCompanyCode('알테오젠'))
