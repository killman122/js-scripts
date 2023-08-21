import time
import logging
import requests
import random
import json
from tqdm import tqdm
import re

UA = [
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/4g;Mozilla/5.0 (Linux; Android 9; Mi Note 3 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; GM1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; 16T Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.5;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.7;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045511 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;11.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79",
    "jdapp;android;10.1.6;10;;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045224 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; 16 X Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.0.0;network/wifi;Mozilla/5.0 (Linux; Android 8.0.0; HTC U-3w Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.0.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1", ]

ra = random.randrange(1, len(UA))
ua = UA[ra]
cookie = ' __jdc=122270672; unpl=; 3AB9D23F7A4B3C9B=7KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CY; pt_pin=jd_6f09619712870; pwdt_id=jd_6f09619712870; b_dw=450; b_dh=727; b_dpr=2; b_webp=1; b_avif=1; shshshfpa=748d8b8c-5c7f-98b3-7b44-420024780b40-1690014602; shshshfpx=748d8b8c-5c7f-98b3-7b44-420024780b40-1690014602; unionwsws=%7B%22devicefinger%22%3A%22eidAe910812231s50AAHX7TISqiyoLdFsaEuydAACOkxegtLT6k3nlGqNQDjzRLHXEALzWVOHTaE1zHIsm7q4l8%2BRT8jdH8eZt5lKAPH%2FbjiqZN6ioZP%22%7D; cid=8; shshshfpb=vIyz6v2PRHq3nZrINlTV8_w; qid_uid=55d6db86-75a7-4c9e-9694-0745373671c4; qid_fs=1690255761566; qid_ls=1690255761566; qid_ts=1690255761630; qid_vis=1; shshshfpv=JD012145b9LggPjgqk8C1690257837165029UlW4Do8-S0D6K-wEqKl-nIu5DQ4ckSKMUmutvHH3vZ_mwdXEqioeWV1Qsme6K20jEn5sUc8m6VY6X2X7BTNoA1cd5dxp~hDIhPcuZeqhMmvIhafxfowB4bCMxx-Hywv9Tk2qx7Es2R3u0O3c45LCRtCng_LBvQHfLcHw9rCVN-NDaEEtcQnjAY08JuzdBNJkDmFCMYIwMxuCynSNjPOQQMfpCDKS4PguJizCBpitUMxuygAWFXLw; joyya=1690257870.1690257876.35.1b9wmm0l3; pt_key=app_openAAJkw2UCADCM3qnKkGdHvYoqRxey0dCJKnfMTbb8hAOIRVnwFuSYzX-r1BqJTR2FUlLl9NayZGM; sid=28a04bb95bef41ca708e8957a00ecb8w; __jda=122270672.16900141923731588112069.1690014192.1690255720.1690526982.5; __jdv=122270672%7Cmyinliu%7Ct_2018512525_myinliu%7Ctuiguang%7C800002027_0_jdbdad-pinzhuan_0_0%7C1690014180000; 3AB9D23F7A4B3CSS=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJTNBP5YIAAAAADF47VOWBC3LP4IX; _gia_d=1; pre_session=z6YIqMoAOBV3fmiDJSWa8fHETx0A3QmB|5; pre_seq=3; __jdb=122270672.4.16900141923731588112069|5.1690526982; mba_sid=5.5; __jd_ref_cls=Babel_dev_expo_other_tab; mba_muid=16900141923731588112069.5.1690527026053'
url = 'https://api.m.jd.com/client.action'
# useid=500913411
page = 9  # max = 24
tab = [229, 222, 212, 225, 234, 227, 228, 224, 226]
tabid = 229  # 212 精选 221 手机 222 电脑 223 母婴 229 家电  224 食品 225 美妆 226 清洁 234 时尚   227 个护  228 更多
filter_words = [
    "幼儿园", "教程", "英语", "辅导", "培训",
    "孩子", "小学", "成人用品", "套套", "情趣",
    "自慰", "阳具", "飞机杯", "男士用品", "女士用品",
    "内衣", "高潮", "避孕", "乳腺", "肛塞", "肛门",
    "宝宝", "玩具", "芭比", "娃娃", "男用",
    "女用", "神油", "足力健", "老年", "老人",
    "宠物", "饲料", "丝袜", "黑丝", "磨脚",
    "脚皮", "除臭", "性感", "内裤", "跳蛋",
    "安全套", "龟头", "阴道", "阴部", "手机卡",
    "流量卡", "和田玉", "钢化膜", "手机壳", "习题", "试卷"
]
flag = False
max_retry = 4  # 最大重试次数
retry_count = 0


def get_use_produce(trialActivityId):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f"functionId=try_apply&body=%7B%22activityId%22%3A{trialActivityId}%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230722163612967%3B2320287912652665%3B35fa0%3Btk02wd34b1cfd41lMSsyeDN4MjZMcmlgqSXVDorV646Zfdld7JSohEwyBAwvAggdq7vWsNbWk2cSb0nCbjb8ZmcQR36V%3B218ee952d95d41175d9ec58c7faf50091c5a046fcc59d6eed159740ab73ccca2%3B3.1%3B1690014972967%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1118292c1aa6ac77296d66ecbb1cec87fa4befd5601b15feaa9269c1dd7edc3e5a901c3ae4c685815c98a5942f5e8e53d838c5079d02133495c2a27b41f9e3193&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJPS5NUEQAAAAACGRQHW7G7ISA2IX&joylog=d2ba4eae1ca1ab058d6b62d2fd8fa869%2A1690014972562~1kPvR8wZieAMDJtQlluRTAxMQ%3D%3D.XHRgXnVcdmFYfFpzbhAAAyUTOgpYIQEjO1xuGEJyQXMnXztcPC8nPBd0L1wVPwooXSs3MBAgKTkUYTEyE3BrQndfPA%3D%3D.2778b979~7%2C1~C5836DC459B23283447DE539A9D33D13F33E27D4~1ob1ho3~C~ShBAXxsLaxFUBR0FYx95axwAAXh5HwUdAgECGEYbbBwRRF1dEwpoElUFHwZ8HHkNHwAJfm4eCB8AAwAfRBMcEVQGHQZ9H3oKGAEKYQQYAxcBAAMcRxIdElcBHARiHnkJHwYLYnYeQR5NE20fElRCXxIJAR0SQUERChEFBQsBAgUGAQcIAAEAAQcICxIdEkVXVxIJFkdGRUZARl9XEh8SRFVQEgkSV1ZGRkdERlVSEB0QRFZXEwpoAwQcBggfAgUcCh4CHAZpHxBbWBYICB0SUEMRChNSAQYAA1MLUlYEBVIBAlFVUwhSBgQJCgcCCQpWBwFWBBEcEVpDEAsQeFtXREgTWQUIBxIfEkUSCAMFCQMEAgYIBQYHDwMcEVpYEgsSHh0ECQQKAQAFA1JQUwAMUw8IHVAEUQMGCAdSUwIEVwYFBAUFUQELVVcPBwlVBwICUwgDAVMHAgARHBFSQ1ATCBZEcEhKBUYBYGN4QgNfakB7fVxnYgttRhAYEFdHEgkSdF9eV19VEXlcUR0SHxZdU0cQDhAACQcLBxEcE0NQQhMKaQoDAB8ABgJsHhZAVhMKaBJgfRx%2BCgcHfhAeEVFdUEFdWFYWHhsGHgIeARIdEgICHwAcABEcEQ0LBQkFFh4bBAMKAwUDCQMBAwEDBAEEAx4FBQAHAAIACgkDAgYFAwgDERwTARBvHxJaW1IQCxBSVF9XVlVERxIdElJaEwoQRxEcEVdaEAsQQwYXAR4EEh8SUlZsRhMKEAICEh8WUVYTCBZAWF9UXF0OVANSUgRUUVcDUFECVVECBApQBFsHAlcCVVQJVlIIBwkQHhFdWRYJaQIeBR4IbBwRUl9fVhIJEgAGCwIDAQcMBQoDBAZMCHJ4RFdHB0ZpdWp8dHhKZgBfdmF2cEt5VQQMHmJ3ZUdSaGFxawNaAFdbfVxVdggDZnNvSXJncRx6YH1Af1ZUHX8BAUZsZHsCVk5CeH1jdnZ3Ylp0eFpgVXRxelh3d1h6dltxVXBWWwJ6WWl2Ymd1enR2RXlWVHEHf0ZWRXpqQQJyc0cbc3RXdHBoXQJXdAZTeFxnSmRgeFN%2BYlNVfnNpfXJWU3FzYFN6cVtBGldwa0BzYVdDcFpkSXdxYEd3VXpeeENmXWgBcX50YEMAc0QIfndbU1pyRVELc1R1AXFgWVlxU1ZBelgDWnRhQFdwV2NcfXR6bHJae0V9ZmgJc0oAf3VwQ0t8YGV1cHdbS3d3Y3h0U3tJeUoHH3xXDA0dAVMJBQUGCFFKSh4ATEpMe09jW3pxdUZXYGV3CVd6AlxXbAILYmpYaG95XHlzYmIEVWZ2BFN3YERiZnZ2fXRKW1N8AENic1t2ZXVLR2NlXmBFYmF9eXdGf3N3QWBlYWJceXRXQHFzR1Fge2JxbmJgeHhxRXBocXFfUnUAZnB1Vltjc2J1d3Vhc1J3YgJrckh2d3BiYHVwYmBxcXB2VXYFfVN0RVNhbHB9V3JhdntOAkgFBUpfUBIfFl5BVhAOEBsdEktTQRILEgMBTQBKU08IRQVWX1xEDVdbUhJO~1p0417c"
    res = requests.post(url=url, headers=headers, data=body)
    response = ''
    response = res.text
    # print(response)
    if response != '':
        text = json.loads(response)
        print(text["message"])
        if text["message"] == "您的申请次数已超100次上限，请明天申请！":
            exit()


def get_produce_list(i, tabid):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f'functionId=try_SpecFeedList&body=%7B%22tabId%22%3A%22{tabid}%22%2C%22page%22%3A1%2C%22version%22%3A2%2C%22source%22%3A%22default%22%2C%22client%22%3A%22app%22%2C%22tryIds%22%3A%5B%22500939846%22%2C%22500943489%22%5D%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230728145026142%3B6843322228159723%3B35fa0%3Btk02we9861d4d41lMyszeDN4MiszhQvRObdvAXrUQKJTPzXc5sUSaBl2KjUo_clTdjIrxmVEzS8Rb-iFUOIIgVCBYeAv%3B5f3373faff784675438493923850f8e11274bd3c5603ac28cd83dcb7e35d3db4%3B3.1%3B1690527026142%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f592a4617d22dea4e4bc55f043747e94f9ee3c7b742652b2171465210d93d5715aa8ff467b5da72f1d3be20d3f98e8d9fc7ad80505f94ebea7eec1cfc73edcacf189382f80f77d61fd05a94eb03b654dc4622e813704c1623c31906660ed54290b01c0b6b23a0a4fa1c4a3c90ded79e1a75c79a55e448e6bccb3bae6852dd1bd0eb238599e73d341edd45649b2016b0e32ac0730da5d2be56171b2cf7229604f85b7cfffa84beea2f4ef8964dcaa098bf7f&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJTNBP5YIAAAAADF47VOWBC3LP4IX'
    # body = f'functionId=try_SpecFeedList&body=%7b%22tabId%22%3a%22{tabid}%22%2c%22page%22%3a{i}%2c%22version%22%3a2%2c%22source%22%3a%22default%22%2c%22client%22%3a%22app%22%7d&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230723132731572%3B5478884256397707%3B35fa0%3Btk02wdd281c8b41lMyszeDErMXgxdKJIPpzo9blND4IDtyGzrnWVyBYyw10yY_XJn_5w8RF5UkT3E1Pn0HRlD8SlF2ld%3B8cfe7205cb005275f94745dbe5de80a070b3454e4e34e4648adc4cb6b2b5a88c%3B3.1%3B1690090051572%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1ddf9d9e7cb8ae68cd7ab7befafe4aadd487c2aaf1ed576afad9f6517dbcc06efdd69fecf5a00543844f5d2d19a83e3b7d2ef6f94f257a4eb58aeb0606fcd4c2a&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJQE3RXPIAAAAACMS5DJQIJ6COYEX'
    # body = f'functionId=try_SpecFeedList&body=%7B%22tabId%22%3A%22{tabid}%22%2C%22page%22%3A{i}%2C%22version%22%3A2%2C%22source%22%3A%22default%22%2C%22client%22%3A%22app%22%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230725115619555%3B8644878755661290%3B35fa0%3Btk02w9c991c0e41lMngyeDNPSGx1CtrASY4AHLCJle7qPCYPN2RDKGT-lvevnVzMgXa8gTFvKGYvHu3MRpcBL_xBEVmL%3B2f4b8aed3f02c867b3b161b564b49af3b696f0b32ce1654d0053f20bd12eb66d%3B3.1%3B1690257379555%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a139fe79080b69ad158cca0fe5bb7902be15c11e2fe74fc0aaefcbd28c99a73a55bbe5472f6be7ca2a636989200e7f35d2210d7344f784be8e1ea48620440bacbc&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJRMOGZNIAAAAADD3UMVQ33VJLSIX'
    # max_retry = 4  # 最大重试次数
    global retry_count

    while retry_count < max_retry:
        try:
            res = requests.post(url=url, headers=headers, data=body)
            res.raise_for_status()  # 如果请求失败，则抛出异常
            response = ''
            response = res.json()
            status = res.status_code
            # print(status,type(status))
            if status == 403:
                flag = False
            if status == 200:
                flag = True
            # print(response)
            # print(response['data']['feedList'],type(response['data']['feedList']))
            feedList = response['data']['feedList']
            feednum = 0
            for i in feedList:
                print(type(i['applyState']))
                if isinstance(i['applyState'], type(None)):
                    # print("value 是 NoneType 类型")
                    feednum += 1
            # print(feedList,len(feedList))
            with tqdm(total=feednum) as pbar:
                for i in feedList:
                    # print(i,type(i))
                    if float(i['jdPrice']) >= 50 and isinstance(i['applyState'], type(None)) and float(
                            i['trialPrice']) < 10:
                        print(i['skuTitle'] + i['trialPrice'])
                        word = i['skuTitle']
                        # 使用正则表达式逐个匹配word中的单词与filter_words中的元素
                        contains_keyword = any(re.search(re.escape(filter_word), word) for filter_word in filter_words)
                        if contains_keyword:
                            print("word包含filter_words中的关键字")
                        else:
                            # 似乎i['applyState'] == null 表示商品没有申请过
                            trialActivityId = i['trialActivityId']
                            # get_use_produce(trialActivityId)
                            time.sleep(5)
                            # 更新进度条
                            pbar.update(1)
            break  # 如果成功获取数据，则跳出重试循环
        except requests.exceptions.RequestException as e:
            retry_count += 1
            logging.error(f"请求失败，正在进行第 {retry_count} 次重试...")
            time.sleep(random.uniform(1, 5))  # 为避免频繁请求，添加随机延时

    if retry_count == max_retry:
        logging.error("请求失败达到最大重试次数，无法获取数据。")
        retry_count = 0


def yeshu():  # 换页数
    for i in range(1, 25):
        print(f'当前页数是{i}')
        get_produce_list(i, tabid)
        if flag == False and retry_count == max_retry:
            print('出现404停止换页,结束本菜单的商品申请')
            break


if __name__ == '__main__':  # 212 精选 221 手机 222 电脑 223 母婴 229 家电  224 食品 225 美妆 226 清洁 234 时尚   227 个护  228 更多
    for i in tab:  # 换菜单
        tabid = i
        if tabid == 229:
            print(f'当前的菜单是家电:{tabid}')
        elif tabid == 222:
            print(f'当前的菜单是电脑:{tabid}')
        elif tabid == 212:
            print(f'当前的菜单是精选:{tabid}')
        elif tabid == 221:
            print(f'当前的菜单是手机:{tabid}')
        elif tabid == 223:
            print(f'当前的菜单是母婴:{tabid}')
        elif tabid == 224:
            print(f'当前的菜单是食品饮料:{tabid}')
        elif tabid == 225:
            print(f'当前的菜单是美妆:{tabid}')
        elif tabid == 226:
            print(f'当前的菜单是清洁:{tabid}')
        elif tabid == 234:
            print(f'当前的菜单是时尚:{tabid}')
        elif tabid == 227:
            print(f'当前的菜单是个护:{tabid}')
        elif tabid == 228:
            print(f'当前的菜单是更多:{tabid}')
        yeshu()

'''
from fake_useragent import UserAgent
import time
import logging
import requests
import random
import json
from loguru import logger
from tqdm import tqdm


UA = [
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/4g;Mozilla/5.0 (Linux; Android 9; Mi Note 3 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; GM1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; 16T Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.5;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.7;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045511 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;11.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79",
    "jdapp;android;10.1.6;10;;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045224 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; 16 X Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.0.0;network/wifi;Mozilla/5.0 (Linux; Android 8.0.0; HTC U-3w Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.0.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1", ]

ra = random.randrange(1, len(UA))
ua = UA[ra]
cookie = '__jdc=122270672; __jdv=122270672%7Cmyinliu%7Ct_2018512525_myinliu%7Ctuiguang%7C800002027_0_jdbdad-pinzhuan_0_0%7C1690014180000; unpl=; 3AB9D23F7A4B3C9B=7KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CY; pt_pin=jd_6f09619712870; pwdt_id=jd_6f09619712870; b_dw=450; b_dh=727; b_dpr=2; b_webp=1; b_avif=1; shshshfpa=748d8b8c-5c7f-98b3-7b44-420024780b40-1690014602; shshshfpx=748d8b8c-5c7f-98b3-7b44-420024780b40-1690014602; unionwsws=%7B%22devicefinger%22%3A%22eidAe910812231s50AAHX7TISqiyoLdFsaEuydAACOkxegtLT6k3nlGqNQDjzRLHXEALzWVOHTaE1zHIsm7q4l8%2BRT8jdH8eZt5lKAPH%2FbjiqZN6ioZP%22%7D; cid=8; shshshfpb=vIyz6v2PRHq3nZrINlTV8_w; shshshfpv=JD012145b9tTJVVVVOkY16900144975570121HaK6f8ch5Y7Gm2ymjraTB5zPrbax6EQrZ1mjFK37qiE5Q0GdN8j75oDbR_2ll9D_GRHv-o1Ko4L0G-ovE6Lg1e5cj2t~hDIhPcuZeqhMmvIhafxfowB4bCMxx-Hywv9Tk2qx7Es2R3u0O3c45LCRtCng_LBvQHfLcHw9rCVN-NDaEEtcQnjAY08JuzdBNJkDmFCMYIwMxuCynSNjPOQQMfpCDKS4PguJizCBpitUMxuygAWFXLw; joyya=1690018373.1690018404.30.168jz6vl3; pt_key=app_openAAJkvLn5ADCmUsa0h8DFASfXFcRAH-SycZ9O5WLbK7-YY21guZlRfyh4kBcw57k7SrGuY9sY6D8; sid=2ec5d463b07367b5cbf02618b769182w; __jda=122270672.16900141923731588112069.1690014192.1690018237.1690089980.3; 3AB9D23F7A4B3CSS=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJQE3RXPIAAAAACMS5DJQIJ6COYEX; _gia_d=1; pre_session=S2Eej1BaUFf4bhhKPxT1b7tXuuEFl9vR|3; pre_seq=3; __jdb=122270672.4.16900141923731588112069|3.1690089980; mba_sid=3.5; __jd_ref_cls=Babel_dev_expo_sku_feeds; mba_muid=16900141923731588112069.3.1690090051624'
url = 'https://api.m.jd.com/client.action'
# useid=500913411
page = 8
tabid = 212 # 212 精选 221 手机 222 电脑 223 母婴 229 家电  224 食品 225 美妆 226 清洁 234 时尚   227 个护  228 更多

def get_use_produce(trialActivityId):
    headers = {
        'Host':'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f"functionId=try_apply&body=%7B%22activityId%22%3A{trialActivityId}%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230722163612967%3B2320287912652665%3B35fa0%3Btk02wd34b1cfd41lMSsyeDN4MjZMcmlgqSXVDorV646Zfdld7JSohEwyBAwvAggdq7vWsNbWk2cSb0nCbjb8ZmcQR36V%3B218ee952d95d41175d9ec58c7faf50091c5a046fcc59d6eed159740ab73ccca2%3B3.1%3B1690014972967%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1118292c1aa6ac77296d66ecbb1cec87fa4befd5601b15feaa9269c1dd7edc3e5a901c3ae4c685815c98a5942f5e8e53d838c5079d02133495c2a27b41f9e3193&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJPS5NUEQAAAAACGRQHW7G7ISA2IX&joylog=d2ba4eae1ca1ab058d6b62d2fd8fa869%2A1690014972562~1kPvR8wZieAMDJtQlluRTAxMQ%3D%3D.XHRgXnVcdmFYfFpzbhAAAyUTOgpYIQEjO1xuGEJyQXMnXztcPC8nPBd0L1wVPwooXSs3MBAgKTkUYTEyE3BrQndfPA%3D%3D.2778b979~7%2C1~C5836DC459B23283447DE539A9D33D13F33E27D4~1ob1ho3~C~ShBAXxsLaxFUBR0FYx95axwAAXh5HwUdAgECGEYbbBwRRF1dEwpoElUFHwZ8HHkNHwAJfm4eCB8AAwAfRBMcEVQGHQZ9H3oKGAEKYQQYAxcBAAMcRxIdElcBHARiHnkJHwYLYnYeQR5NE20fElRCXxIJAR0SQUERChEFBQsBAgUGAQcIAAEAAQcICxIdEkVXVxIJFkdGRUZARl9XEh8SRFVQEgkSV1ZGRkdERlVSEB0QRFZXEwpoAwQcBggfAgUcCh4CHAZpHxBbWBYICB0SUEMRChNSAQYAA1MLUlYEBVIBAlFVUwhSBgQJCgcCCQpWBwFWBBEcEVpDEAsQeFtXREgTWQUIBxIfEkUSCAMFCQMEAgYIBQYHDwMcEVpYEgsSHh0ECQQKAQAFA1JQUwAMUw8IHVAEUQMGCAdSUwIEVwYFBAUFUQELVVcPBwlVBwICUwgDAVMHAgARHBFSQ1ATCBZEcEhKBUYBYGN4QgNfakB7fVxnYgttRhAYEFdHEgkSdF9eV19VEXlcUR0SHxZdU0cQDhAACQcLBxEcE0NQQhMKaQoDAB8ABgJsHhZAVhMKaBJgfRx%2BCgcHfhAeEVFdUEFdWFYWHhsGHgIeARIdEgICHwAcABEcEQ0LBQkFFh4bBAMKAwUDCQMBAwEDBAEEAx4FBQAHAAIACgkDAgYFAwgDERwTARBvHxJaW1IQCxBSVF9XVlVERxIdElJaEwoQRxEcEVdaEAsQQwYXAR4EEh8SUlZsRhMKEAICEh8WUVYTCBZAWF9UXF0OVANSUgRUUVcDUFECVVECBApQBFsHAlcCVVQJVlIIBwkQHhFdWRYJaQIeBR4IbBwRUl9fVhIJEgAGCwIDAQcMBQoDBAZMCHJ4RFdHB0ZpdWp8dHhKZgBfdmF2cEt5VQQMHmJ3ZUdSaGFxawNaAFdbfVxVdggDZnNvSXJncRx6YH1Af1ZUHX8BAUZsZHsCVk5CeH1jdnZ3Ylp0eFpgVXRxelh3d1h6dltxVXBWWwJ6WWl2Ymd1enR2RXlWVHEHf0ZWRXpqQQJyc0cbc3RXdHBoXQJXdAZTeFxnSmRgeFN%2BYlNVfnNpfXJWU3FzYFN6cVtBGldwa0BzYVdDcFpkSXdxYEd3VXpeeENmXWgBcX50YEMAc0QIfndbU1pyRVELc1R1AXFgWVlxU1ZBelgDWnRhQFdwV2NcfXR6bHJae0V9ZmgJc0oAf3VwQ0t8YGV1cHdbS3d3Y3h0U3tJeUoHH3xXDA0dAVMJBQUGCFFKSh4ATEpMe09jW3pxdUZXYGV3CVd6AlxXbAILYmpYaG95XHlzYmIEVWZ2BFN3YERiZnZ2fXRKW1N8AENic1t2ZXVLR2NlXmBFYmF9eXdGf3N3QWBlYWJceXRXQHFzR1Fge2JxbmJgeHhxRXBocXFfUnUAZnB1Vltjc2J1d3Vhc1J3YgJrckh2d3BiYHVwYmBxcXB2VXYFfVN0RVNhbHB9V3JhdntOAkgFBUpfUBIfFl5BVhAOEBsdEktTQRILEgMBTQBKU08IRQVWX1xEDVdbUhJO~1p0417c"
    res = requests.post(url=url, headers=headers, data=body)
    response = ''
    response = res.text
    # print(response)
    if response is not '':
        text=json.loads(response)
        print(text["message"])

def get_produce_list():
    headers = {
        'Host':'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body=f'functionId=try_SpecFeedList&body=%7b%22tabId%22%3a%22{tabid}%22%2c%22page%22%3a{page}%2c%22version%22%3a2%2c%22source%22%3a%22default%22%2c%22client%22%3a%22app%22%7d&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230723132731572%3B5478884256397707%3B35fa0%3Btk02wdd281c8b41lMyszeDErMXgxdKJIPpzo9blND4IDtyGzrnWVyBYyw10yY_XJn_5w8RF5UkT3E1Pn0HRlD8SlF2ld%3B8cfe7205cb005275f94745dbe5de80a070b3454e4e34e4648adc4cb6b2b5a88c%3B3.1%3B1690090051572%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1ddf9d9e7cb8ae68cd7ab7befafe4aadd487c2aaf1ed576afad9f6517dbcc06efdd69fecf5a00543844f5d2d19a83e3b7d2ef6f94f257a4eb58aeb0606fcd4c2a&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJQE3RXPIAAAAACMS5DJQIJ6COYEX'
    res = requests.post(url=url, headers=headers, data=body)
    response = ''
    response = res.json()
    # print(response)
    # print(response['data']['feedList'],type(response['data']['feedList']))
    feedList=response['data']['feedList']
    # print(feedList,len(feedList))
    with tqdm(total=len(feedList)) as pbar:
        for i in feedList:
            # print(i,type(i))
            print(i['skuTitle'])
            trialActivityId = i['trialActivityId']
            get_use_produce(trialActivityId)
            time.sleep(5)
            # 更新进度条
            pbar.update(1)

get_produce_list()
'''
# get_use_produce()


"""
import time
import logging
import requests
import random
import json
from tqdm import tqdm
import re

UA = [
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/4g;Mozilla/5.0 (Linux; Android 9; Mi Note 3 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; GM1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; 16T Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.5;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.7;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045511 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;11.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79",
    "jdapp;android;10.1.6;10;;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045224 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; 16 X Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.0.0;network/wifi;Mozilla/5.0 (Linux; Android 8.0.0; HTC U-3w Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.0.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1", ]

ra = random.randrange(1, len(UA))
ua = UA[ra]
cookie = 'pt_pin=jd_6f09619712870; pwdt_id=jd_6f09619712870; qid_uid=2b9970ce-6168-40c0-a92d-d01b6571e94b; qid_fs=1687357509564; qid_ls=1687357509564; qid_ts=1687357509647; qid_vis=1; unpl=JF8EALFnNSttUBgGB0sCE0BASFpSW18IQh5WO2IHBFxeHgAEGwpMEhV7XlVdXxRKEB9vYxRVWlNIUA4bACsiEEpcVV9UAEIfAV9nAVIzWSVUDB5sdUJFSg5dVwgJGB5RaDQFB19oe1cFKwMrEhdNWVBWWglIEAZnbgZUXFFPVQEaBxIiEXtdXFptOHsTBWxhAVVcWUhkBCsDK18QTFtQWlUPShQEam8MV11ZQlAEHwMeGyBKbVc%7CJF8EAMBnNSttWEpRVkhQG0EWH1VdWw4JTR5WZzBWVg4LSVYAGQseEBV7XlVdXxRKFx9vZBRXX1NJUw4bBSsSFHtdVV9dAEISAmtmNWRUNkhcBRMEGRIRSjNUX1xmexQDX2Y1XFkKTlEAS1YbQENJCVcMXDhKJwpuVwVVXFtMUQ0YAhsWFkNfZF1cCEIWCmpiB1IzWSVWBBoAEhsZQlhTblw4SicCXyZrVFxdSFIFGAtWGhQZWFFbDVxLRVBtMwYGXGhKZAU; __jdc=122270672; cid=8; 3AB9D23F7A4B3C9B=4SJO52J4L4D5LN4QX6RZ6AG7L3YI2C3RXVEJ2NYAQMKFMFWWKBMQOA3TVRQBR754XAWP2GYHEBAZ3QYVRNYSOV6SL4; b_dw=393; b_dpr=2.75; b_webp=1; b_avif=1; shshshfpb=voH3gKJiKKpM167-KlR0ZhA; shshshfpa=a2341e94-71dd-83bd-c7be-44e2c61c9023-1655206084; shshshfpx=a2341e94-71dd-83bd-c7be-44e2c61c9023-1655206084; unionwsws=%7B%22devicefinger%22%3A%22eidA0e9a812345s3qdV1TEIMTSWruSpjHHKTaKnVdszADVKPO0sglebp06w6Tq7JTupmd0ZFw0im00jCXdxq0AZuSzr0tthYuy2pEiILiw%2B6BbWmn3pX%22%7D; retina=1; appCode=msc588d6d5; webp=1; visitkey=7675039636682208554; b_dh=775; __jdv=122270672%7Ckong%7Ct_1000170135%7Ctuiguang%7Cnotset%7C1688965852625; pt_key=app_openAAJkvKo0ADADud7w1rAzKLB0OvdJPxRH14MUq49gCbqzioHYzMD5EXJdKnJPMC1Hsw9bTuT5LVE; sid=f3350cee92b6b900340a9a130f13349w; shshshfpv=JD012145b92TxV3zkc87169015978615601uUeM_K_VmOLril7Mhfq4z0t9u5ATHkbbn5OiIRxNTa42tZdy_ApeDf8IBbJ2b1AnI3KK_GuYz8_Ns2KblilLdw0untfj2~ecNy8rXaBK8blgzp9hPTsL1YI_Pkll7E4lL3qm5A_6foXTkXOfR5ZpYyOMx2hxcspKtNwLy2gfybb7sEdXrlAVM9Sk_CsclZL2xD1XHI0BLWOMZZNB4GtGLrhNJzoi4tF7wjMutJd1a5Wzhrkbdf39Q; joyya=1690159888.1690159891.40.0bn8mtql3; __jda=122270672.16874291274121545096115.1687429127.1690165967.1690174332.46; 3AB9D23F7A4B3CSS=jdd034SJO52J4L4D5LN4QX6RZ6AG7L3YI2C3RXVEJ2NYAQMKFMFWWKBMQOA3TVRQBR754XAWP2GYHEBAZ3QYVRNYSOV6SL4AAAAMJQZJVFDQAAAAADGDLA557WCSN4EX; _gia_d=1; pre_session=AjcA6olf+ubw3e4nddzaaEShofZsUM7X|6441; pre_seq=3; __jdb=122270672.5.16874291274121545096115|46.1690174332; mba_sid=5400.5; shshshsID=e123d42b62d1f19a91fe776e05c7cd67_3_1690175796804; __jd_ref_cls=Babel_dev_expo_sku_feeds; mba_muid=16874291274121545096115.5400.1690175818459'
url = 'https://api.m.jd.com/client.action'
# useid=500913411
page = 9  # max = 24
tab = [229, 222, 212, 225, 234, 227, 228, 224, 226]
tabid = 229  # 212 精选 221 手机 222 电脑 223 母婴 229 家电  224 食品 225 美妆 226 清洁 234 时尚   227 个护  228 更多
filter_words = [
    "幼儿园", "教程", "英语", "辅导", "培训",
    "孩子", "小学", "成人用品", "套套", "情趣",
    "自慰", "阳具", "飞机杯", "男士用品", "女士用品",
    "内衣", "高潮", "避孕", "乳腺", "肛塞", "肛门",
    "宝宝", "玩具", "芭比", "娃娃", "男用",
    "女用", "神油", "足力健", "老年", "老人",
    "宠物", "饲料", "丝袜", "黑丝", "磨脚",
    "脚皮", "除臭", "性感", "内裤", "跳蛋",
    "安全套", "龟头", "阴道", "阴部", "手机卡",
    "流量卡", "和田玉", "钢化膜", "手机壳", "习题", "试卷"
]
flag = False
max_retry = 4  # 最大重试次数
retry_count = 0


def get_use_produce(trialActivityId):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f"functionId=try_apply&body=%7B%22activityId%22%3A{trialActivityId}%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230722163612967%3B2320287912652665%3B35fa0%3Btk02wd34b1cfd41lMSsyeDN4MjZMcmlgqSXVDorV646Zfdld7JSohEwyBAwvAggdq7vWsNbWk2cSb0nCbjb8ZmcQR36V%3B218ee952d95d41175d9ec58c7faf50091c5a046fcc59d6eed159740ab73ccca2%3B3.1%3B1690014972967%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1118292c1aa6ac77296d66ecbb1cec87fa4befd5601b15feaa9269c1dd7edc3e5a901c3ae4c685815c98a5942f5e8e53d838c5079d02133495c2a27b41f9e3193&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJPS5NUEQAAAAACGRQHW7G7ISA2IX&joylog=d2ba4eae1ca1ab058d6b62d2fd8fa869%2A1690014972562~1kPvR8wZieAMDJtQlluRTAxMQ%3D%3D.XHRgXnVcdmFYfFpzbhAAAyUTOgpYIQEjO1xuGEJyQXMnXztcPC8nPBd0L1wVPwooXSs3MBAgKTkUYTEyE3BrQndfPA%3D%3D.2778b979~7%2C1~C5836DC459B23283447DE539A9D33D13F33E27D4~1ob1ho3~C~ShBAXxsLaxFUBR0FYx95axwAAXh5HwUdAgECGEYbbBwRRF1dEwpoElUFHwZ8HHkNHwAJfm4eCB8AAwAfRBMcEVQGHQZ9H3oKGAEKYQQYAxcBAAMcRxIdElcBHARiHnkJHwYLYnYeQR5NE20fElRCXxIJAR0SQUERChEFBQsBAgUGAQcIAAEAAQcICxIdEkVXVxIJFkdGRUZARl9XEh8SRFVQEgkSV1ZGRkdERlVSEB0QRFZXEwpoAwQcBggfAgUcCh4CHAZpHxBbWBYICB0SUEMRChNSAQYAA1MLUlYEBVIBAlFVUwhSBgQJCgcCCQpWBwFWBBEcEVpDEAsQeFtXREgTWQUIBxIfEkUSCAMFCQMEAgYIBQYHDwMcEVpYEgsSHh0ECQQKAQAFA1JQUwAMUw8IHVAEUQMGCAdSUwIEVwYFBAUFUQELVVcPBwlVBwICUwgDAVMHAgARHBFSQ1ATCBZEcEhKBUYBYGN4QgNfakB7fVxnYgttRhAYEFdHEgkSdF9eV19VEXlcUR0SHxZdU0cQDhAACQcLBxEcE0NQQhMKaQoDAB8ABgJsHhZAVhMKaBJgfRx%2BCgcHfhAeEVFdUEFdWFYWHhsGHgIeARIdEgICHwAcABEcEQ0LBQkFFh4bBAMKAwUDCQMBAwEDBAEEAx4FBQAHAAIACgkDAgYFAwgDERwTARBvHxJaW1IQCxBSVF9XVlVERxIdElJaEwoQRxEcEVdaEAsQQwYXAR4EEh8SUlZsRhMKEAICEh8WUVYTCBZAWF9UXF0OVANSUgRUUVcDUFECVVECBApQBFsHAlcCVVQJVlIIBwkQHhFdWRYJaQIeBR4IbBwRUl9fVhIJEgAGCwIDAQcMBQoDBAZMCHJ4RFdHB0ZpdWp8dHhKZgBfdmF2cEt5VQQMHmJ3ZUdSaGFxawNaAFdbfVxVdggDZnNvSXJncRx6YH1Af1ZUHX8BAUZsZHsCVk5CeH1jdnZ3Ylp0eFpgVXRxelh3d1h6dltxVXBWWwJ6WWl2Ymd1enR2RXlWVHEHf0ZWRXpqQQJyc0cbc3RXdHBoXQJXdAZTeFxnSmRgeFN%2BYlNVfnNpfXJWU3FzYFN6cVtBGldwa0BzYVdDcFpkSXdxYEd3VXpeeENmXWgBcX50YEMAc0QIfndbU1pyRVELc1R1AXFgWVlxU1ZBelgDWnRhQFdwV2NcfXR6bHJae0V9ZmgJc0oAf3VwQ0t8YGV1cHdbS3d3Y3h0U3tJeUoHH3xXDA0dAVMJBQUGCFFKSh4ATEpMe09jW3pxdUZXYGV3CVd6AlxXbAILYmpYaG95XHlzYmIEVWZ2BFN3YERiZnZ2fXRKW1N8AENic1t2ZXVLR2NlXmBFYmF9eXdGf3N3QWBlYWJceXRXQHFzR1Fge2JxbmJgeHhxRXBocXFfUnUAZnB1Vltjc2J1d3Vhc1J3YgJrckh2d3BiYHVwYmBxcXB2VXYFfVN0RVNhbHB9V3JhdntOAkgFBUpfUBIfFl5BVhAOEBsdEktTQRILEgMBTQBKU08IRQVWX1xEDVdbUhJO~1p0417c"
    res = requests.post(url=url, headers=headers, data=body)
    response = ''
    response = res.text
    # print(response)
    if response != '':
        text = json.loads(response)
        print(text["message"])
        if text["message"] == "您的申请次数已超100次上限，请明天申请！":
            exit()


def get_produce_list(i, tabid):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f'functionId=try_SpecFeedList&body=%7b%22tabId%22%3a%22{tabid}%22%2c%22page%22%3a{i}%2c%22version%22%3a2%2c%22source%22%3a%22default%22%2c%22client%22%3a%22app%22%7d&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230723132731572%3B5478884256397707%3B35fa0%3Btk02wdd281c8b41lMyszeDErMXgxdKJIPpzo9blND4IDtyGzrnWVyBYyw10yY_XJn_5w8RF5UkT3E1Pn0HRlD8SlF2ld%3B8cfe7205cb005275f94745dbe5de80a070b3454e4e34e4648adc4cb6b2b5a88c%3B3.1%3B1690090051572%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1ddf9d9e7cb8ae68cd7ab7befafe4aadd487c2aaf1ed576afad9f6517dbcc06efdd69fecf5a00543844f5d2d19a83e3b7d2ef6f94f257a4eb58aeb0606fcd4c2a&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJQE3RXPIAAAAACMS5DJQIJ6COYEX'
    # max_retry = 4  # 最大重试次数
    global retry_count

    while retry_count < max_retry:
        try:
            res = requests.post(url=url, headers=headers, data=body)
            res.raise_for_status()  # 如果请求失败，则抛出异常
            response = ''
            response = res.json()
            status = res.status_code
            # print(status,type(status))
            if status == 403:
                flag = False
            if status == 200:
                flag = True
            # print(response)
            # print(response['data']['feedList'],type(response['data']['feedList']))
            feedList = response['data']['feedList']
            feednum = 0
            for i in feedList:
                # print(type(i['applyState']))
                if isinstance(i['applyState'], type(None)):
                    # print("value 是 NoneType 类型")
                    feednum += 1
            # print(feedList,len(feedList))
            with tqdm(total=feednum) as pbar:
                for i in feedList:
                    # print(i,type(i))
                    if float(i['jdPrice']) >= 50 and isinstance(i['applyState'], type(None)) and float(
                            i['trialPrice']) < 10:
                        print(i['skuTitle'] + i['trialPrice'])
                        word = i['skuTitle']
                        # 使用正则表达式逐个匹配word中的单词与filter_words中的元素
                        contains_keyword = any(re.search(re.escape(filter_word), word) for filter_word in filter_words)
                        if contains_keyword:
                            print("word包含filter_words中的关键字")
                        else:
                            # 似乎i['applyState'] == null 表示商品没有申请过
                            trialActivityId = i['trialActivityId']
                            get_use_produce(trialActivityId)
                            time.sleep(5)
                            # 更新进度条
                            pbar.update(1)
            break  # 如果成功获取数据，则跳出重试循环
        except requests.exceptions.RequestException as e:
            retry_count += 1
            logging.error(f"请求失败，正在进行第 {retry_count} 次重试...")
            time.sleep(random.uniform(1, 5))  # 为避免频繁请求，添加随机延时

    if retry_count == max_retry:
        logging.error("请求失败达到最大重试次数，无法获取数据。")
        retry_count = 0


def yeshu():  # 换页数
    for i in range(1, 25):
        print(f'当前页数是{i}')
        get_produce_list(i, tabid)
        if flag == False and retry_count == max_retry:
            break


if __name__ == '__main__':
    for i in tab:  # 换菜单
        tabid = i
        print(tabid)
        yeshu()
"""

"""
from fake_useragent import UserAgent
import time
import logging
import requests
import random
import json
from tqdm import tqdm
import re

UA = [
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/4g;Mozilla/5.0 (Linux; Android 9; Mi Note 3 Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; GM1910 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; 16T Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.6;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.5;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.7;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;13.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045511 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;11.4;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79",
    "jdapp;android;10.1.6;10;;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; M2006J10C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045224 Mobile Safari/537.36",
    "jdapp;android;10.1.6;9;network/wifi;Mozilla/5.0 (Linux; Android 9; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; 16 X Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;android;10.1.6;8.0.0;network/wifi;Mozilla/5.0 (Linux; Android 8.0.0; HTC U-3w Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044942 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.0.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; LYA-AL00 Build/HUAWEILYA-AL00L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045230 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.2;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;8.1.0;network/wifi;Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045131 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.3;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;iPhone;10.1.6;14.3;network/4g;Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "jdapp;android;10.1.6;11;network/wifi;Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36",
    "jdapp;android;10.1.6;10;network/wifi;Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36",
    "jdapp;iPhone;10.1.6;14.1;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1", ]

ra = random.randrange(1, len(UA))
ua = UA[ra]
cookie = 'pt_pin=jd_6f09619712870; pwdt_id=jd_6f09619712870; qid_uid=2b9970ce-6168-40c0-a92d-d01b6571e94b; qid_fs=1687357509564; qid_ls=1687357509564; qid_ts=1687357509647; qid_vis=1; unpl=JF8EALFnNSttUBgGB0sCE0BASFpSW18IQh5WO2IHBFxeHgAEGwpMEhV7XlVdXxRKEB9vYxRVWlNIUA4bACsiEEpcVV9UAEIfAV9nAVIzWSVUDB5sdUJFSg5dVwgJGB5RaDQFB19oe1cFKwMrEhdNWVBWWglIEAZnbgZUXFFPVQEaBxIiEXtdXFptOHsTBWxhAVVcWUhkBCsDK18QTFtQWlUPShQEam8MV11ZQlAEHwMeGyBKbVc%7CJF8EAMBnNSttWEpRVkhQG0EWH1VdWw4JTR5WZzBWVg4LSVYAGQseEBV7XlVdXxRKFx9vZBRXX1NJUw4bBSsSFHtdVV9dAEISAmtmNWRUNkhcBRMEGRIRSjNUX1xmexQDX2Y1XFkKTlEAS1YbQENJCVcMXDhKJwpuVwVVXFtMUQ0YAhsWFkNfZF1cCEIWCmpiB1IzWSVWBBoAEhsZQlhTblw4SicCXyZrVFxdSFIFGAtWGhQZWFFbDVxLRVBtMwYGXGhKZAU; __jdc=122270672; cid=8; 3AB9D23F7A4B3C9B=4SJO52J4L4D5LN4QX6RZ6AG7L3YI2C3RXVEJ2NYAQMKFMFWWKBMQOA3TVRQBR754XAWP2GYHEBAZ3QYVRNYSOV6SL4; b_dw=393; b_dpr=2.75; b_webp=1; b_avif=1; shshshfpb=voH3gKJiKKpM167-KlR0ZhA; shshshfpa=a2341e94-71dd-83bd-c7be-44e2c61c9023-1655206084; shshshfpx=a2341e94-71dd-83bd-c7be-44e2c61c9023-1655206084; unionwsws=%7B%22devicefinger%22%3A%22eidA0e9a812345s3qdV1TEIMTSWruSpjHHKTaKnVdszADVKPO0sglebp06w6Tq7JTupmd0ZFw0im00jCXdxq0AZuSzr0tthYuy2pEiILiw%2B6BbWmn3pX%22%7D; retina=1; appCode=msc588d6d5; webp=1; visitkey=7675039636682208554; b_dh=775; __jdv=122270672%7Ckong%7Ct_1000170135%7Ctuiguang%7Cnotset%7C1688965852625; pt_key=app_openAAJkvKo0ADADud7w1rAzKLB0OvdJPxRH14MUq49gCbqzioHYzMD5EXJdKnJPMC1Hsw9bTuT5LVE; sid=f3350cee92b6b900340a9a130f13349w; shshshfpv=JD012145b92TxV3zkc87169015978615601uUeM_K_VmOLril7Mhfq4z0t9u5ATHkbbn5OiIRxNTa42tZdy_ApeDf8IBbJ2b1AnI3KK_GuYz8_Ns2KblilLdw0untfj2~ecNy8rXaBK8blgzp9hPTsL1YI_Pkll7E4lL3qm5A_6foXTkXOfR5ZpYyOMx2hxcspKtNwLy2gfybb7sEdXrlAVM9Sk_CsclZL2xD1XHI0BLWOMZZNB4GtGLrhNJzoi4tF7wjMutJd1a5Wzhrkbdf39Q; joyya=1690159888.1690159891.40.0bn8mtql3; __jda=122270672.16874291274121545096115.1687429127.1690165967.1690174332.46; 3AB9D23F7A4B3CSS=jdd034SJO52J4L4D5LN4QX6RZ6AG7L3YI2C3RXVEJ2NYAQMKFMFWWKBMQOA3TVRQBR754XAWP2GYHEBAZ3QYVRNYSOV6SL4AAAAMJQZJVFDQAAAAADGDLA557WCSN4EX; _gia_d=1; pre_session=AjcA6olf+ubw3e4nddzaaEShofZsUM7X|6441; pre_seq=3; __jdb=122270672.5.16874291274121545096115|46.1690174332; mba_sid=5400.5; shshshsID=e123d42b62d1f19a91fe776e05c7cd67_3_1690175796804; __jd_ref_cls=Babel_dev_expo_sku_feeds; mba_muid=16874291274121545096115.5400.1690175818459'
url = 'https://api.m.jd.com/client.action'
# useid=500913411
page = 9  # max = 24
tab = [229, 222, 212, 225, 234, 227, 228, 224, 226]
tabid = 229  # 212 精选 221 手机 222 电脑 223 母婴 229 家电  224 食品 225 美妆 226 清洁 234 时尚   227 个护  228 更多
filter_words = [
    "幼儿园", "教程", "英语", "辅导", "培训",
    "孩子", "小学", "成人用品", "套套", "情趣",
    "自慰", "阳具", "飞机杯", "男士用品", "女士用品",
    "内衣", "高潮", "避孕", "乳腺", "肛塞", "肛门",
    "宝宝", "玩具", "芭比", "娃娃", "男用",
    "女用", "神油", "足力健", "老年", "老人",
    "宠物", "饲料", "丝袜", "黑丝", "磨脚",
    "脚皮", "除臭", "性感", "内裤", "跳蛋",
    "安全套", "龟头", "阴道", "阴部", "手机卡",
    "流量卡", "和田玉", "钢化膜", "手机壳", "习题", "试卷"
]
flag = True


def get_use_produce(trialActivityId):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f"functionId=try_apply&body=%7B%22activityId%22%3A{trialActivityId}%7D&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230722163612967%3B2320287912652665%3B35fa0%3Btk02wd34b1cfd41lMSsyeDN4MjZMcmlgqSXVDorV646Zfdld7JSohEwyBAwvAggdq7vWsNbWk2cSb0nCbjb8ZmcQR36V%3B218ee952d95d41175d9ec58c7faf50091c5a046fcc59d6eed159740ab73ccca2%3B3.1%3B1690014972967%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1118292c1aa6ac77296d66ecbb1cec87fa4befd5601b15feaa9269c1dd7edc3e5a901c3ae4c685815c98a5942f5e8e53d838c5079d02133495c2a27b41f9e3193&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJPS5NUEQAAAAACGRQHW7G7ISA2IX&joylog=d2ba4eae1ca1ab058d6b62d2fd8fa869%2A1690014972562~1kPvR8wZieAMDJtQlluRTAxMQ%3D%3D.XHRgXnVcdmFYfFpzbhAAAyUTOgpYIQEjO1xuGEJyQXMnXztcPC8nPBd0L1wVPwooXSs3MBAgKTkUYTEyE3BrQndfPA%3D%3D.2778b979~7%2C1~C5836DC459B23283447DE539A9D33D13F33E27D4~1ob1ho3~C~ShBAXxsLaxFUBR0FYx95axwAAXh5HwUdAgECGEYbbBwRRF1dEwpoElUFHwZ8HHkNHwAJfm4eCB8AAwAfRBMcEVQGHQZ9H3oKGAEKYQQYAxcBAAMcRxIdElcBHARiHnkJHwYLYnYeQR5NE20fElRCXxIJAR0SQUERChEFBQsBAgUGAQcIAAEAAQcICxIdEkVXVxIJFkdGRUZARl9XEh8SRFVQEgkSV1ZGRkdERlVSEB0QRFZXEwpoAwQcBggfAgUcCh4CHAZpHxBbWBYICB0SUEMRChNSAQYAA1MLUlYEBVIBAlFVUwhSBgQJCgcCCQpWBwFWBBEcEVpDEAsQeFtXREgTWQUIBxIfEkUSCAMFCQMEAgYIBQYHDwMcEVpYEgsSHh0ECQQKAQAFA1JQUwAMUw8IHVAEUQMGCAdSUwIEVwYFBAUFUQELVVcPBwlVBwICUwgDAVMHAgARHBFSQ1ATCBZEcEhKBUYBYGN4QgNfakB7fVxnYgttRhAYEFdHEgkSdF9eV19VEXlcUR0SHxZdU0cQDhAACQcLBxEcE0NQQhMKaQoDAB8ABgJsHhZAVhMKaBJgfRx%2BCgcHfhAeEVFdUEFdWFYWHhsGHgIeARIdEgICHwAcABEcEQ0LBQkFFh4bBAMKAwUDCQMBAwEDBAEEAx4FBQAHAAIACgkDAgYFAwgDERwTARBvHxJaW1IQCxBSVF9XVlVERxIdElJaEwoQRxEcEVdaEAsQQwYXAR4EEh8SUlZsRhMKEAICEh8WUVYTCBZAWF9UXF0OVANSUgRUUVcDUFECVVECBApQBFsHAlcCVVQJVlIIBwkQHhFdWRYJaQIeBR4IbBwRUl9fVhIJEgAGCwIDAQcMBQoDBAZMCHJ4RFdHB0ZpdWp8dHhKZgBfdmF2cEt5VQQMHmJ3ZUdSaGFxawNaAFdbfVxVdggDZnNvSXJncRx6YH1Af1ZUHX8BAUZsZHsCVk5CeH1jdnZ3Ylp0eFpgVXRxelh3d1h6dltxVXBWWwJ6WWl2Ymd1enR2RXlWVHEHf0ZWRXpqQQJyc0cbc3RXdHBoXQJXdAZTeFxnSmRgeFN%2BYlNVfnNpfXJWU3FzYFN6cVtBGldwa0BzYVdDcFpkSXdxYEd3VXpeeENmXWgBcX50YEMAc0QIfndbU1pyRVELc1R1AXFgWVlxU1ZBelgDWnRhQFdwV2NcfXR6bHJae0V9ZmgJc0oAf3VwQ0t8YGV1cHdbS3d3Y3h0U3tJeUoHH3xXDA0dAVMJBQUGCFFKSh4ATEpMe09jW3pxdUZXYGV3CVd6AlxXbAILYmpYaG95XHlzYmIEVWZ2BFN3YERiZnZ2fXRKW1N8AENic1t2ZXVLR2NlXmBFYmF9eXdGf3N3QWBlYWJceXRXQHFzR1Fge2JxbmJgeHhxRXBocXFfUnUAZnB1Vltjc2J1d3Vhc1J3YgJrckh2d3BiYHVwYmBxcXB2VXYFfVN0RVNhbHB9V3JhdntOAkgFBUpfUBIfFl5BVhAOEBsdEktTQRILEgMBTQBKU08IRQVWX1xEDVdbUhJO~1p0417c"
    res = requests.post(url=url, headers=headers, data=body)
    response = ''
    response = res.text
    # print(response)
    if response != '':
        text = json.loads(response)
        print(text["message"])
        if text["message"] == "您的申请次数已超100次上限，请明天申请！":
            exit()


def get_produce_list(i, tabid):
    headers = {
        'Host': 'api.m.jd.com',
        'X-Rp-Client': 'h5_1.0.0',
        'User-Agent': ua,
        'X-Referer-Page': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html',
        'Origin': 'https://prodev.m.jd.com',
        'X-Requested-With': 'com.jingdong.app.mall',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://prodev.m.jd.com/mall/active/3C751WNneAUaZ8Lw8xYN7cbSE8gm/index.html?ids=500929513%2C500921840&tttparams=sp7IeoeyJhZGRyZXNzSWQiOiIiLCJkTGF0IjowLCJkTG5nIjowLCJnTGF0IjoiMzkuOTIxNDY5IiwiZ0xuZyI6IjExNi40NDMxMDciLCJncHNfYXJlYSI6IjBfMF8wXzAiLCJsYXQiOjAsImxuZyI6MCwibW9kZWwiOiJTTS1OOTc2TiIsInBvc0xhdCI6IiIsInBvc0xuZyI6IiIsInByc3RhdGUiOiIwIiwidWVtcHMiOiIwLTAtMi6J9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive'
    }
    body = f'functionId=try_SpecFeedList&body=%7b%22tabId%22%3a%22{tabid}%22%2c%22page%22%3a{i}%2c%22version%22%3a2%2c%22source%22%3a%22default%22%2c%22client%22%3a%22app%22%7d&appid=newtry&area=&uuid=5393638323036373-1626262383166393&h5st=20230723132731572%3B5478884256397707%3B35fa0%3Btk02wdd281c8b41lMyszeDErMXgxdKJIPpzo9blND4IDtyGzrnWVyBYyw10yY_XJn_5w8RF5UkT3E1Pn0HRlD8SlF2ld%3B8cfe7205cb005275f94745dbe5de80a070b3454e4e34e4648adc4cb6b2b5a88c%3B3.1%3B1690090051572%3B62f4d401ae05799f14989d31956d3c5fee3e2da7aa7dc48dbe23f7d544868e73b3134c0f96c662d0b48cc21f30ce07740f9baed25879b82236c0ea86956af40707315cb6dba436a4f766f2a883092f9672f2a8df3bb7362af3111c8cc065779d585f5aed88a325608a97d4573a651f595b2ca3797daaa505fea2289bfbee03a1ddf9d9e7cb8ae68cd7ab7befafe4aadd487c2aaf1ed576afad9f6517dbcc06efdd69fecf5a00543844f5d2d19a83e3b7d2ef6f94f257a4eb58aeb0606fcd4c2a&x-api-eid-token=jdd037KDWGMMJTMGJ5BOBQB34LFLGDYVYN7TYZJ5VE2GILP7MPKU2N6RSPXQJNAL66R7XO42LLGZGJMXUR5FCOK5NLVV4CYAAAAMJQE3RXPIAAAAACMS5DJQIJ6COYEX'
    max_retry = 4  # 最大重试次数
    retry_count = 0

    while retry_count < max_retry:
        try:
            res = requests.post(url=url, headers=headers, data=body)
            res.raise_for_status()  # 如果请求失败，则抛出异常
            response = ''
            response = res.json()
            status = res.status_code
            # print(status,type(status))
            if status == 403:
                flag = False
            if status == 200:
                flag = True
            # print(response)
            # print(response['data']['feedList'],type(response['data']['feedList']))
            feedList = response['data']['feedList']
            feednum = 0
            for i in feedList:
                # print(type(i['applyState']))
                if isinstance(i['applyState'], type(None)):
                    # print("value 是 NoneType 类型")
                    feednum += 1
            # print(feedList,len(feedList))
            with tqdm(total=feednum) as pbar:
                for i in feedList:
                    # print(i,type(i))
                    if float(i['jdPrice']) >= 50 and isinstance(i['applyState'], type(None)) and float(
                            i['trialPrice']) < 10:
                        print(i['skuTitle']+i['trialPrice'])
                        word = i['skuTitle']
                        # 使用正则表达式逐个匹配word中的单词与filter_words中的元素
                        contains_keyword = any(re.search(re.escape(filter_word), word) for filter_word in filter_words)
                        if contains_keyword:
                            print("word包含filter_words中的关键字")
                        else:
                            # 似乎i['applyState'] == null 表示商品没有申请过
                            trialActivityId = i['trialActivityId']
                            get_use_produce(trialActivityId)
                            time.sleep(5)
                            # 更新进度条
                            pbar.update(1)
            break  # 如果成功获取数据，则跳出重试循环
        except requests.exceptions.RequestException as e:
            retry_count += 1
            logging.error(f"请求失败，正在进行第 {retry_count} 次重试...")
            time.sleep(random.uniform(1, 3))  # 为避免频繁请求，添加随机延时

    if retry_count == max_retry:
        logging.error("请求失败达到最大重试次数，无法获取数据。")



def yeshu():  # 换页数
    for i in range(1, 25):
        get_produce_list(i, tabid)
        if flag == False:
            break



if __name__ == '__main__':
    for i in tab:  # 换菜单
        tabid = i
        yeshu()

"""
