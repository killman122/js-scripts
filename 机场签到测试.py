# import requests
# import time
# from fake_useragent import UserAgent
# import logging
#
# url = 'https://xianpoqiang.com/user/checkin'
# ua = UserAgent()
# # print(ua.edge,type(ua.edge))
# import json
#
# start = time.time()
#
# # 你的代码
#
#
# date = ""
# headers = {
#     "Host": "xianpoqiang.com",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Accept-Encoding": "gzip, deflate",
#     "Cookie": "email=wjr2483484885%40gmail.com;expire_in=1690430250;ip=086b5fd130bfd710c806a7b63e3ebdf7;key=5e9cb80a1eb3ebcc3ba4b5f66e3dcbe4fcc1514ecfd99;lang=zh-cn;mtauth=26901254d4f784e4db4ad316bc502c7d;uid=539;",
#     "Origin": "https://xianpoqiang.com",
#     "Referer": "https://xianpoqiang.com/user",
#     "User-Agent": ua.edge,
#     "x-requested-with": "XMLHttpRequest",
# }
# res = requests.post(url=url, data=date, headers=headers)
# response = res.json()
# print(response,type(response))
# end = time.time()
# logging.info("Total execution time: %s", end - start)
# if response['ret']==0:
#     print("签到成功,你已经签到过")
#

import requests
import time
from fake_useragent import UserAgent
from loguru import logger
from tqdm import tqdm

url = 'https://xianpoqiang.com/user/checkin'
ua = UserAgent()
# print(ua.edge,type(ua.edge))
import json

start = time.time()

logger.info('Starting checkin...')
date = ""
headers = {
    "Host": "xianpoqiang.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "email=wjr2483484885%40gmail.com;expire_in=1690430250;ip=086b5fd130bfd710c806a7b63e3ebdf7;key=5e9cb80a1eb3ebcc3ba4b5f66e3dcbe4fcc1514ecfd99;lang=zh-cn;mtauth=26901254d4f784e4db4ad316bc502c7d;uid=539;",
    "Origin": "https://xianpoqiang.com",
    "Referer": "https://xianpoqiang.com/user",
    "User-Agent": ua.edge,
    "x-requested-with": "XMLHttpRequest",
}
# 使用tqdm模块来显示进度条
with tqdm(total=100) as pbar:
    for i in range(3):
        # 发送请求
        res = requests.post(url=url, data=date, headers=headers)
        # 获取响应
        response = res.json()
        # 打印响应
        logger.info(response)
        if response['ret'] == 0:
            logger.info('签到成功,你已经签到过')
        # 更新进度条
        pbar.update(1)

end = time.time()
logger.info('Checkin finished.')
logger.info('Total execution time: %s', end - start)


