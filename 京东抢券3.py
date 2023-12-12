from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import requests
import threading
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

args = "key=CBFF3A3A136766FC84037252EA01B99E4E433A99A78BF343DF4C8395E00B0C49B697B5FD581762D86685A4205A59D303_bingo,roleId=8940D9D93C9E4EE01D94B89B2D1AA369F6E20394868DCC856566E129C3DCAE2E06B12984EED4CFFD5F9E9174067B7AB084DE639A9FF7DFC99B7219C39AE86ECCC9B4434FB5E74F4AFD5C0AC5F4CC07F61C36B346FBDE1472A36B7FE91866AA6F94CDAA783275289B19B7196CDBF8FE344F0993DB2803671128E6EAFFE7EFC26D514F8840090017BECFEC6FD36F21060C4D588F6DC1DFFB089637671F124852E0_bingo"


def get_local_params():
    url = "http://127.0.0.1:5889/log"
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': '127.0.0.1:5889',
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers)
    return response.json()["log"], response.json()["random"]


def send_request():
    log, random = get_local_params()
    headers = {
        "Host": "api.m.jd.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5307 MMWEBSDK/20230604 MMWEBID/4829 MicroMessenger/8.0.38.2400(0x28002656) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "X-Requested-With": "com.tencent.mm",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "pt_key=AAJlMVltADCXG011s0cfa450HwF5wRauKGiwfg97nNIQ-z55m_zr3NbR9DHJF95LnQF1UYoY4qE; pt_pin=jd_6f09619712870;"
    }
    body = {
        "activityId": "7ooZUnJ6JSgpdyqUNzqJVsmAd5U",
        "from": "H5node",
        "scene": "1",
        "args": f"{args}",
        "log": f'{log}',
        "random": f"{random}"
    }
    jd_url = f"https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body={body}&client=wh5&clientVersion=1.0.0"
    response = requests.get(url=jd_url, headers=headers)
    logging.info(response.json())


scheduler = BlockingScheduler()


@scheduler.scheduled_job(CronTrigger(hour='*', minute='59', second='58'))
def scheduled_job():
    for _ in range(100):
        try:
            send_request()
        except Exception as e:
            logging.error(e)


scheduler.start()

# import requests
# import threading
# import logging
# import schedule
# import time
# # 注意在请求的参数args中的参数需要抓取网页进行获取,将网页中的args进行搜索,删除strengthenKey,和下面的参数进行拼接
# # args = "key=24A3221FDCD05340181FFBDD9F95E81A93710689C4AD2A5F4708D1102143874186BCB97280F660645087AC74837ACE15_bingo,roleId=62B8463C23BFCA12876A56FB49467670BFA35B5A229AF7D735148B1D36D0CA4AFFA2C0B1E3260F8E65EC54B9377BEFBD2C59C318D873652C79E4E6D6BC5A94DE6D42C5A353D20D81193C8CD109F6A2F3801A0096041B7B845AACE4E87CD2FFEC4B5F66E49168F1B4BC5C80EB75A8330B48B1A479EEF2A9187A238E3879B82DDCBF6B54A98E2967E18CFA63093601C75CACB41E6E94AAB47AEFF1DC03AEFA88F4_bingo"
# args = "key=CBFF3A3A136766FC84037252EA01B99E4E433A99A78BF343DF4C8395E00B0C49B697B5FD581762D86685A4205A59D303_bingo,roleId=8940D9D93C9E4EE01D94B89B2D1AA369F6E20394868DCC856566E129C3DCAE2E06B12984EED4CFFD5F9E9174067B7AB084DE639A9FF7DFC99B7219C39AE86ECCC9B4434FB5E74F4AFD5C0AC5F4CC07F61C36B346FBDE1472A36B7FE91866AA6F94CDAA783275289B19B7196CDBF8FE344F0993DB2803671128E6EAFFE7EFC26D514F8840090017BECFEC6FD36F21060C4D588F6DC1DFFB089637671F124852E0_bingo"
# # logging.basicConfig(filename='秒杀抢购券.log', filemode='w',
# #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#
# # "key=24A3221FDCD05340181FFBDD9F95E81A93710689C4AD2A5F4708D1102143874186BCB97280F660645087AC74837ACE15_bingo,roleId=62B8463C23BFCA12876A56FB49467670BFA35B5A229AF7D735148B1D36D0CA4AFFA2C0B1E3260F8E65EC54B9377BEFBD2C59C318D873652C79E4E6D6BC5A94DE6D42C5A353D20D81193C8CD109F6A2F3801A0096041B7B845AACE4E87CD2FFEC4B5F66E49168F1B4BC5C80EB75A8330B48B1A479EEF2A9187A238E3879B82DDCBF6B54A98E2967E18CFA63093601C75CACB41E6E94AAB47AEFF1DC03AEFA88F4_bingo"
#
# def job_that_executes_once():
#     for i in range(100):
#         try:
#             send_request()
#         except:
#             pass
#     return schedule.CancelJob
#
#
# def run_threaded(job_func):
#     job_thread = threading.Thread(target=job_func)
#     job_thread.start()
#
# # 按照自定义的时间执行
# schedule.every().hour.at(":59:58").do(run_threaded, job_that_executes_once)
#
# def get_local_params():
#     url = "http://127.0.0.1:5889/log"
#
#     payload = {}
#     headers = {
#         'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
#         'Accept': '*/*',
#         'Host': '127.0.0.1:5889',
#         'Connection': 'keep-alive'
#     }
#     response = requests.request("GET", url, headers=headers, data=payload)
#     # print(response.json())
#     # log = response.json()["log"]
#     # random = response.json()["random"]
#     return response.json()["log"], response.json()["random"]
#
#
# # print(log+random)
#
# def send_request():
#     log, random = get_local_params()
#     headers = {
#         "Host": "api.m.jd.com",
#         "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5307 MMWEBSDK/20230604 MMWEBID/4829 MicroMessenger/8.0.38.2400(0x28002656) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "X-Requested-With": "com.tencent.mm",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Cookie": "pt_key=AAJlMVltADCXG011s0cfa450HwF5wRauKGiwfg97nNIQ-z55m_zr3NbR9DHJF95LnQF1UYoY4qE; pt_pin=jd_6f09619712870"
#     }
#     body = {"activityId": "7ooZUnJ6JSgpdyqUNzqJVsmAd5U", "from": "H5node", "scene": "1",
#             "args": f"{args}",
#             "log": f'{log}',
#             "random": f"{random}"}
#     jd_url = f"https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body={body}&client=wh5&clientVersion=1.0.0"
#     response = requests.get(url=jd_url, headers=headers)
#     # print(response.json())
#     logging.info(response.json())
#
#
# # logger = logging.Logger("日志")
# try:
#     for i in range(100):
#         send_request()
# except:
#     pass
#
# # logging.info(send_request())
#
#
# # for i in range(1):
# #     thread = threading.Thread(target=send_request, args=(args,))
# #     thread.start()
