import requests
import threading
import logging
from loguru import logger

# 注意在请求的参数args中的参数需要抓取网页进行获取,将网页中的args进行搜索,删除strengthenKey,和下面的参数进行拼接
# args = "key=24A3221FDCD05340181FFBDD9F95E81A93710689C4AD2A5F4708D1102143874186BCB97280F660645087AC74837ACE15_bingo,roleId=62B8463C23BFCA12876A56FB49467670BFA35B5A229AF7D735148B1D36D0CA4AFFA2C0B1E3260F8E65EC54B9377BEFBD2C59C318D873652C79E4E6D6BC5A94DE6D42C5A353D20D81193C8CD109F6A2F3801A0096041B7B845AACE4E87CD2FFEC4B5F66E49168F1B4BC5C80EB75A8330B48B1A479EEF2A9187A238E3879B82DDCBF6B54A98E2967E18CFA63093601C75CACB41E6E94AAB47AEFF1DC03AEFA88F4_bingo"
args = "key=523635429EE0CDDA5567F984A9CB7D7BA106042150A912B373814728C47746ED45F6B2E40A3534940F4B9289963EFDE4_bingo,roleId=7EB4B12020FCC350C2F996BFFB28A5753B8C75BB207E71E1330BF801A618220257043EF82603F3D86322F47F3D205DF90B834FE73C76039604ACE5025A484AB1463920955CDE4F6ABF95AF89713984F789DFFE32A777262CCFF42AC64251922B692EE29C9178417A49431478B3256AD22BA10DB9F50E9CE27E2D8A1110296134_bingo"
# logging.basicConfig(filename='秒杀抢购券.log', filemode='w',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# "key=24A3221FDCD05340181FFBDD9F95E81A93710689C4AD2A5F4708D1102143874186BCB97280F660645087AC74837ACE15_bingo,roleId=62B8463C23BFCA12876A56FB49467670BFA35B5A229AF7D735148B1D36D0CA4AFFA2C0B1E3260F8E65EC54B9377BEFBD2C59C318D873652C79E4E6D6BC5A94DE6D42C5A353D20D81193C8CD109F6A2F3801A0096041B7B845AACE4E87CD2FFEC4B5F66E49168F1B4BC5C80EB75A8330B48B1A479EEF2A9187A238E3879B82DDCBF6B54A98E2967E18CFA63093601C75CACB41E6E94AAB47AEFF1DC03AEFA88F4_bingo"


def get_local_params():
    url = "http://127.0.0.1:5889/log"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': '127.0.0.1:5889',
        'Connection': 'keep-alive'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    # log = response.json()["log"]
    # random = response.json()["random"]
    return response.json()["log"], response.json()["random"]


# print(log+random)

def send_request():
    log, random = get_local_params()
    headers = {
        "Host": "api.m.jd.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5307 MMWEBSDK/20230604 MMWEBID/4829 MicroMessenger/8.0.38.2400(0x28002656) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "X-Requested-With": "com.tencent.mm",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "pt_key=AAJlMVltADCXG011s0cfa450HwF5wRauKGiwfg97nNIQ-z55m_zr3NbR9DHJF95LnQF1UYoY4qE; pt_pin=jd_6f09619712870"
    }
    body = {"activityId": "7ooZUnJ6JSgpdyqUNzqJVsmAd5U", "from": "H5node", "scene": "1",
            "args": f"{args}",
            "log": f'{log}',
            "random": f"{random}"}
    jd_url = f"https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body={body}&client=wh5&clientVersion=1.0.0"
    response = requests.get(url=jd_url, headers=headers)
    print(response.json())
    # logging.info(response.json())
    logger.info(response.json())

# logger = logging.Logger("日志")
try:
    for i in range(100):
        send_request()
except:
    pass

# logging.info(send_request())


# for i in range(1):
#     thread = threading.Thread(target=send_request, args=(args,))
#     thread.start()
