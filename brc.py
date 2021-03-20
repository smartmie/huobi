import requests
import time
import datetime
import pandas as pd

def get_name():
    url = "https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=CNY"

    payload={}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': '',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
    'Cookie': '__cfduid=d294bb9c039122d0ebfda5d68ea38a6021616166742'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return_list = []
    for i in response.json()['data']:
        return_list.append([i['id'],
        i['symbol'],
        i['circulating_supply'],
        i['quote']['CNY']['price'],
        i['quote']['CNY']['percent_change_24h'],
        i['quote']['CNY']['percent_change_7d'],
        i['quote']['CNY']['volume_24h']])
        print(i['id'],
        i['symbol'],
        i['circulating_supply'],
        i['quote']['CNY']['price'],
        i['quote']['CNY']['percent_change_24h'],
        i['quote']['CNY']['percent_change_7d'],
        i['quote']['CNY']['volume_24h'])

    #     pass
    return return_list

def create_time(apart=30):
    tem = datetime.datetime.today()
    time_e = "{0}-{1}-{2}-{3}-{4}-{5}".format(tem.year, tem.month, tem.day, "8", "0", "0") 
    time_e = datetime.datetime.strptime(time_e,'%Y-%m-%d-%H-%M-%S')
    time_s = time_e + datetime.timedelta(-apart)
    # print(type(time_e))
    # return time.mktime(time_s), time.mktime(time_e)
    return round(datetime.datetime.timestamp(time_s)), round(datetime.datetime.timestamp(time_e))
    pass

def get_trading(start_time,end_time,id=1):
    
    url = "https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?id={id}&convert=CNY&time_start={start_time}&time_end={end_time}".format(id=id,start_time=start_time,end_time=end_time)
    re = requests.session()
    html_response = re.get(url)
    # print(html_response.text)
    print(html_response.json()['data'])
    return_list = []
    for i in reversed(html_response.json()['data']['quotes']):
        print( i['time_open'],i['time_close'],i['time_high'],i['time_low'],i['quote']['CNY']['open'],i['quote']['CNY']['high'],i['quote']['CNY']['low'],i['quote']['CNY']['close'],i['quote']['CNY']['volume'],i['quote']['CNY']['market_cap'])
        return_list.append([i['time_open'],
        i['quote']['CNY']['open'],
        i['time_high'],
        i['quote']['CNY']['high'],
        i['time_low'],
        i['quote']['CNY']['low'],
        i['time_close'],
        i['quote']['CNY']['close'],
        i['quote']['CNY']['volume'],
        i['quote']['CNY']['market_cap']])
        # pass
    return return_list
    pass

def out_excel():
    # f = pd.DataFrame("id":,"symbol":,"circulating_supply":,"percent_change_24h":)
    pass

if __name__ == '__main__':
    t1,t2 = create_time()
    print(t1,t2)
    print(get_trading(t1,t2))
    # get_name()
#name
#symbol
#circulating_supply

#quote usd 
#percent_change_24h
#percent_change_7d
#market_cap
