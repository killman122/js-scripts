import os

import requests
import random
import time
import urllib.parse
import urllib.request
import urllib.response

buy_cookie = 'email=wjr2483484885%40gmail.com;expire_in=1675344596;ip=4f2b7a6c84d064c8d8994f10258c21c5;key=9b3ea0b52e9f098930c088079d8878bbf1d2b5246f974;lang=zh-cn;mtauth=cb2f26958faaead71be68957f7c06712;PHPSESSID=vkbd3eqspsm5d2rt2n1s4ckoqt;pop=yes;uid=539;@email=2483483884%40qq.cpm;expire_in=1675343148;ip=5d3e19a20dd83cd638b7cfa78481aa8b;key=486c5d2350a803493f141f95bb52d6edd372732dff5de;lang=zh-cn;mtauth=cb2f26958faaead71be68957f7c06712;PHPSESSID=vkbd3eqspsm5d2rt2n1s4ckoqt;pop=yes;uid=513@email=2483484885%40qq.com;expire_in=1675343251;ip=757af5c55af43c2575c8258328625a9b;key=499150a745a4179733356551965da7e1019e4db19785c;lang=zh-cn;mtauth=cb2f26958faaead71be68957f7c06712;PHPSESSID=vkbd3eqspsm5d2rt2n1s4ckoqt;pop=yes;uid=536'
# if "buy_cookie" in os.environ and os.environ["buy_cookie"]:
#     buy_cookie = os.environ["buy_cookie"]
#     buy_cookie = str(buy_cookie)
#     print(buy_cookie)

buy_cookies = []
print(buy_cookie)


def get_time():
    now_time = str(int(time.time() * 1000))
    print('当前时间戳:', now_time)
    return now_time


# 随机UA函数
def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


# def buy():
#     try:
#         url='https://xianpoqiang.com/user/shop',
#         headers = {
#             ":authority": "xianpoqiang.com",
#             ":method": "POST",
#             ":path": "/user/buy",
#             ":scheme": "https",
#             "accept": "application/json, text/javascript, */*; q=0.01",
#             "accept-encoding": "gzip, deflate, br",
#             "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#             "cache-control": "no-cache",
#             "content-length": "42",
#             "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#             "cookie": "pop=yes; lang=zh-cn; mtauth=d92cf5cb9ac67a8337f6801656349d18; uid=539; email=wjr2483484885%40gmail.com; key=8e32601b7b9b430605a961feae8681414cd14c4ccd199; ip=aad42ecbd6d727955c9b3208f35a9dff; expire_in=1675374342",
#             "origin": "https://xianpoqiang.com",
#             "pragma": "no-cache",
#             "referer": "https://xianpoqiang.com/user/shop",
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
#             "x-requested-with": "XMLHttpRequest",
#         }
#         data = {
#             'coupon': '',
#             'shop': '1',
#             'autorenew': '0',
#             'disableothers': '1'
#         }
#         response = requests.post(url=url, data=data, headers=headers)
#         # data = urllib.parse.urlencode(data).encode()
#         print(data,type(data))
#         # request = urllib.request.Request(url=url, data=data, headers=headers)  # 如果要在请求头中加入请求体则要使用data=data在函数的参数内
#         # response = urllib.request.urlopen(request)
#         # res=urllib.request.Request(url,data=data,headers=headers)
#         print(response.text)
#         print(response.json())
#
#     except Exception as e:
#         print(e)

#
# buy()

def buy(cookie):
    try:
        sign_url = 'https://xianpoqiang.com/user/buy'
        sign_header = {
            "Host": "xianpoqiang.com",
            "content-length": "42",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://xianpoqiang.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://xianpoqiang.com/user/shop",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": cookie
        }
        data = {
            'coupon': '',
            'shop': '1',
            'autorenew': '0',
            'disableothers': '1'
        }
        result = requests.post(url=sign_url, data=data, headers=sign_header)
        result_json = result.json()
        print(result_json)
        if result_json['ret'] == 1:
            print('购买成功')
        else:
            print('未知错误')
    except Exception as e:
        print(e)


if buy_cookie:
    buy_cookies = buy_cookie.split('@')
    print(f'本序列共存在{len(buy_cookies)}个cookie')
    # print(buy_cookies)
    # for i in buy_cookies:
    #     print(f'正在输出cookie{i}')
    for i in range(len(buy_cookies)):
        print(f'正在输出第{i + 1}个cookie,值为{buy_cookies[i]}')
        buy(buy_cookies[i])
        time.sleep(10)

