# 通过抓包观察可以发现,所有的商品通过id值来获取,从第一个id值到最后一个id为止
import time

import requests
from fake_useragent import UserAgent
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

token = '126c2e9648f244ba91ac33a03a6e1bde'
ua = UserAgent().random
消息内容 = ''
mail_subject = ''
lastspu = 40
lastmoney = 30

def send_message():
    username = "wjr2483484885@gmail.com"
    password = "mreqbrbcpsaeloma"
    mail_from = "wjr2483484885@gmail.com"
    mail_to = "2483484885@qq.com"
    mail_subject = "得物商品上新"
    mail_body = 消息内容

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(mail_body, 'plain'))
    try:
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()
    except Exception as e:
        print(f'错误: 由于 {str(e)} 无法发送电子邮件。')


# print(ua)
# 有时需要在请求中添加转义字符,可能请求体中的像是字典,实际上是一个字符串
def 推送():
    global token
    data = {
        "token": token,
        "title": "得物商品到货了!!!!!",
        "content": 消息内容,
        # "topic":"test"
    }
    headers = {
        'USER-AGENT': ua
    }

    url = "http://www.pushplus.plus/send/"
    res = requests.post(url=url, data=data, headers=headers)
    # print(res.json())


def 得物商品查询(lastSpuId):
    url = 'https://app.dewu.com/hacking-newbie/v1/high-value/allowance-module?sign=f483f265e919adbd19aa29758394d28d'
    headers = {
        'Host': 'app.dewu.com',
        'Connection': 'keep-alive',
        'ua': 'duapp/5.22.3(android;11)',
        'appid': 'h5',
        'SK': '9JgSKkxfRab52YsrdOjH54LecF84HNlf5diZf1Bar21LuO2dT61f7BMr3jx71zpgBz2FenzLWbqdN4ucytOKTa9FJr1u',
        'shumeiId': '202206201105599577aec2d8302d653009c385871e64ef01dab1c9dbe482cd',
        'deviceTrait': 'Redmi+Note+8+Pro',
        'x-auth-token': "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTI2NzAyMzgsImV4cCI6MTcyNDIwNjIzOCwiaXNzIjoiZGY2NmU1MDhmM2JjZmZkMyIsInN1YiI6ImRmNjZlNTA4ZjNiY2ZmZDMiLCJ1dWlkIjoiZGY2NmU1MDhmM2JjZmZkMyIsInVzZXJJZCI6MTk0MDQzNzM0NywidXNlck5hbWUiOiLlvpfniallci1aMUs3QzNQOCIsImlzR3Vlc3QiOmZhbHNlfQ.M93ItnDyqyJCj5nNzG2iLXeF05wf7N7LchYcnrNCJ39l01R_ozckCezs_EHuM0SmrIyV_GGxu7fGJR8QFAyEWuEPihgFdzSwClGUR79wuAYx5D1EedQb57bKtOg6erPYsq2whYHyXmsJ2PhPqLWc-rELrutPC_tn-Bf9jpyt0NTtAtAEj9iybbwYeFloW_0GbzXKRxc6MpJImo6UkceGPylWFmxqqPTS5Mhj6eicGsW3-tOyEXPbGBiuWa152x2qWnKYOhPgc6gc9c60al00R31OqZ-aP9qvZNltAB6GxVeT-GrIaD_9L6Ikb-mm9GOUxs7A-8wEEce9I5GSNodhwA",
        'uuid': 'df66e508f3bcffd3',
        'channel': 'du',
        'duToken': 'd41d8cd9|1940437347|1692622428|89247580441d037d',
        'appVersion': '5.22.3',
        'emu': '0',
        'cookieToken': 'd41d8cd9|1940437347|1692622428|89247580441d037d',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36/duapp/5.22.3(android;11)',
        'isRoot': '0',
        'imei': '',
        'platform': 'h5',
        'isProxy': '0',
        'Accept': '*/*',
        'Origin': 'https://m.dewu.com',
        'X-Requested-With': 'com.shizhuang.duapp',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.dewu.com/h5-newbie/super-deal-product',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'duToken=d41d8cd9|1940437347|1692622428|89247580441d037d',
        'Content-Type': 'application/json'
    }
    # data = "{\"pageSize\":40,\"brandSpuId\":null}"
    # payload = str({"pageSize":42,"brandSpuId":'null',"lastSpuId":lastSpuId})
    payload = "{\"pageSize\":9,\"brandSpuId\":null,\"lastSpuId\":" + str(lastSpuId) + "}"
    # payload = json.dumps({"pageSize": 42, "brandSpuId": 'null', "lastSpuId": lastSpuId})
    res = requests.post(url=url, data=payload, headers=headers)
    # print(res.json())
    res_json = res.json()
    if res_json["data"] != None:
        list0 = res_json["data"]["spuList"]
        for i in list0:
            if i['discountPrice'] <= 4000 and i['status'] == 11:
                # print(i)
                global 消息内容, lastspu
                global mail_subject
                global lastmoney
                if i['discountPrice'] < lastmoney:
                    lastmoney = i['discountPrice']
                    lastspu = i['spuId']
                消息内容 += i['spuName'] + '价格=' + str(int(i['discountPrice']) / 100) + '\n'
                if i['discountPrice'] == 0:
                    得物商品提交(i['spuId'])
                    mail_subject = '免单出现,注意抢购'
        print(消息内容)
        lastSpuId = list0[-1]['spuId']
        print(f'输出最后一个id用作最后的商品查询{lastSpuId}')
        得物商品查询(lastSpuId)
    else:
        得物商品提交(lastspu)
        send_message()  # 当res_json["data"] 是 None时,执行send_message函数并结束此函数


def 得物商品监控():
    url = 'https://app.dewu.com/hacking-newbie/v1/high-value/allowance-module?sign=f483f265e919adbd19aa29758394d28d'
    headers = {
        'Host': 'app.dewu.com',
        'Connection': 'keep-alive',
        'ua': 'duapp/5.22.3(android;11)',
        'appid': 'h5',
        'SK': '9JgSKkxfRab52YsrdOjH54LecF84HNlf5diZf1Bar21LuO2dT61f7BMr3jx71zpgBz2FenzLWbqdN4ucytOKTa9FJr1u',
        'shumeiId': '202206201105599577aec2d8302d653009c385871e64ef01dab1c9dbe482cd',
        'deviceTrait': 'Redmi+Note+8+Pro',
        'x-auth-token': "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTI2NzAyMzgsImV4cCI6MTcyNDIwNjIzOCwiaXNzIjoiZGY2NmU1MDhmM2JjZmZkMyIsInN1YiI6ImRmNjZlNTA4ZjNiY2ZmZDMiLCJ1dWlkIjoiZGY2NmU1MDhmM2JjZmZkMyIsInVzZXJJZCI6MTk0MDQzNzM0NywidXNlck5hbWUiOiLlvpfniallci1aMUs3QzNQOCIsImlzR3Vlc3QiOmZhbHNlfQ.M93ItnDyqyJCj5nNzG2iLXeF05wf7N7LchYcnrNCJ39l01R_ozckCezs_EHuM0SmrIyV_GGxu7fGJR8QFAyEWuEPihgFdzSwClGUR79wuAYx5D1EedQb57bKtOg6erPYsq2whYHyXmsJ2PhPqLWc-rELrutPC_tn-Bf9jpyt0NTtAtAEj9iybbwYeFloW_0GbzXKRxc6MpJImo6UkceGPylWFmxqqPTS5Mhj6eicGsW3-tOyEXPbGBiuWa152x2qWnKYOhPgc6gc9c60al00R31OqZ-aP9qvZNltAB6GxVeT-GrIaD_9L6Ikb-mm9GOUxs7A-8wEEce9I5GSNodhwA",
        'uuid': 'df66e508f3bcffd3',
        'channel': 'du',
        'duToken': 'd41d8cd9|1940437347|1692622428|89247580441d037d',
        'appVersion': '5.22.3',
        'emu': '0',
        'cookieToken': 'd41d8cd9|1940437347|1692622428|89247580441d037d',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36/duapp/5.22.3(android;11)',
        'isRoot': '0',
        'imei': '',
        'platform': 'h5',
        'isProxy': '0',
        'Accept': '*/*',
        'Origin': 'https://m.dewu.com',
        'X-Requested-With': 'com.shizhuang.duapp',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.dewu.com/h5-newbie/super-deal-product',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'duToken=d41d8cd9|1940437347|1692622428|89247580441d037d',
        'Content-Type': 'application/json'
    }
    data = "{\"pageSize\":40,\"brandSpuId\":null}"
    # payload = "{\"pageSize\":52,\"lastSpuId\":5479197}"
    res = requests.post(url=url, data=data, headers=headers)
    # print(res.json())
    res_json = res.json()
    list0 = res_json["data"]["spuList"]
    for i in list0:
        if i['discountPrice'] <= 4000 and i['status'] == 11:
            # print(i)
            global 消息内容
            global mail_subject
            global lastspu
            global lastmoney
            if i['discountPrice'] < lastmoney:
                lastmoney = i['discountPrice']
                lastspu = i['spuId']
            消息内容 += i['spuName'] + '价格=' + str(int(i['discountPrice']) / 100) + '\n' + '\r'
            if i['discountPrice'] == 0:
                得物商品提交(i['spuId'])
                mail_subject = '免单出现,注意抢购'
    # print(消息内容)
    # print(list0[-1])
    lastSpuId = list0[-1]['spuId']
    print(f'输出最后一个id用作最后的商品查询{lastSpuId}')
    得物商品查询(lastSpuId)
    # 推送()
    # send_message()

    # for i in list0:
    #     if i['discountPrice'] <= 4000 and i['status'] == 11:
    #         # print(i)
    #         global 消息内容
    #         消息内容 = i['spuName'] + '价格=' + str(int(i['discountPrice']) / 100) + '\n'
    #         消息内容 += 消息内容
    #         print(消息内容)
import time
from datetime import datetime, timedelta
import pytz

# Define what task to perform when desired time is reached
def perform_task():
    print("10:00 AM arrived in Beijing! Performing task...")
    # Add your task here

# Define function to wait until 10:00 AM Beijing time
def wait_until_specific_time(target_hour=10, target_min=0):
    # Get Beijing Timezone
    beijing = pytz.timezone('Asia/Shanghai')

    while True:
        # Get current Beijing Time
        current_time = datetime.now(beijing)

        # Check if current time is already past desired time
        if current_time.hour > target_hour or (current_time.hour == target_hour and current_time.minute == target_min-1 and current_time.second > 58):
            # Calculate time until next day's desired time
            tomorrow = current_time + timedelta(days=1)
            target_time = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day,
                                   hour=target_hour, minute=target_min, tzinfo=beijing)
        else:
            # Calculate time until today's desired time
            target_time = datetime(year=current_time.year, month=current_time.month, day=current_time.day,
                                   hour=target_hour, minute=target_min, tzinfo=beijing)

        # Calculate the seconds left until target time
        seconds_until_target = (target_time - current_time).total_seconds()
        print(f"Seconds until {target_hour}:{target_min}: {seconds_until_target}")

        # Wait until target time
        if seconds_until_target > 0:
            time.sleep(seconds_until_target)
            perform_task()
        else:
            # If target time was in the past (negative time difference), start over
            continue

# wait_until_specific_time()

def 得物商品提交(spuId):
    url = 'https://app.dewu.com/hacking-newbie/v1/high-value/receive?sign=766da56bb9005a708cc9275b3e02df20'
    headers = {
        'Host': 'app.dewu.com',
        'Connection': 'keep-alive',
        'ua': 'duapp/5.22.3(android;11)',
        'appid': 'h5',
        'SK': '9JgSKkxfRab52YsrdOjH54LecF84HNlf5diZf1Bar21LuO2dT61f7BMr3jx71zpgBz2FenzLWbqdN4ucytOKTa9FJr1u',
        'shumeiId': '202206201105599577aec2d8302d653009c385871e64ef01dab1c9dbe482cd',
        'deviceTrait': 'Redmi+Note+8+Pro',
        'x-auth-token': "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTczMzU0MzEsImV4cCI6MTcyODg3MTQzMSwiaXNzIjoiNGU2OTJhNDBkY2JlNTJkNSIsInN1YiI6IjRlNjkyYTQwZGNiZTUyZDUiLCJ1dWlkIjoiNGU2OTJhNDBkY2JlNTJkNSIsInVzZXJJZCI6MTk4MTY2MjE0NCwidXNlck5hbWUiOiLlvpfniallci01UTFCMUIySyIsImlzR3Vlc3QiOmZhbHNlfQ.HSz7_zdkPPOscLuSOs3reSGMgEXflIZP_SjB_KRZsYQAbU1R_IiXu8VxG44cNEwB3diytg4gG_R2TY3yEpfYvDBzP3Oh-RfpfI0Ijr4lVn_uNIJom0vcWjghCLUvvyL051gt5RidMh-zvlymDk4hjXCWfQbAfZKyitb-ityqYdnEnO5tajWZXFNcOOZELXEmHPk6341UEoMturT4sjrTMYBlSnTkgbgxRfl5Ak69tfEL47g_Hgn7cj_woN_AuRk3fuq8g6vsGT9PBG_tEvbX33hYbaXuue3Sb3KkVsHNvuIb9VZndqwf28H9aj4SAX2jBNarrF_kSAsBrIA3TMRa0A",
        'uuid': '4e692a40dcbe52d5',
        'channel': 'du',
        'duToken': 'd41d8cd9|1981662144|1695922785|e99c7bcb1398f302',
        'appVersion': '5.22.3',
        'emu': '0',
        'cookieToken': 'd41d8cd9|1981662144|1695922785|e99c7bcb1398f302',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36/duapp/5.22.3(android;11)',
        'isRoot': '0',
        'imei': '',
        'platform': 'h5',
        'isProxy': '0',
        'Accept': '*/*',
        'Origin': 'https://m.dewu.com',
        'X-Requested-With': 'com.shizhuang.duapp',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.dewu.com/h5-newbie/super-deal-product',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'duToken=d41d8cd9|1981662144|1695922785|e99c7bcb1398f302',
        'Content-Type': 'application/json'
    }
    data = {"spuId": spuId}
    res = requests.post(url=url, headers=headers,json=data)
    print(res.json())

for i in range(80):
    得物商品提交(6185146)
    time.sleep(0.03)
# 推送()
# 得物商品监控()
