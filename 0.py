import requests

url = "http://hd.opposhop.cn/api/cn/oapi/marketing/task/receiveAward?taskId=1697139908512325632&activityId=1697136306548908032"

payload={}
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}
headers = {
    'Host': 'hd.opposhop.cn',
    'Connection': 'keep-alive',
    's_channel': 'h5_m',
    'utm_campaign': 'direct',
    'utm_term': 'direct',
    'ut': 'direct',
    'uc': 'qiandao',
    'isNeedRiskHandle': 'true',
    'constToken': 'DtFfpd6iSBZBVkQQAFKRnXYGMdX+jfe8@bj',
    'getLoginStatus': 'false',
    'x-euler-const': '10302120::1fc84a6975c4d83944315c65b7d489ca1b70ff516595133a695a46f98c9e6ab1::1693580915383::9ed43f0de8024b2f87f2291d439f5998::Vmc0N2chUGO6xkbpVnI4FGchNmNoQjO61kbhkGRtczI21ENDoDT69Wa6xWYs8SL1AjKgxEbpVnO4BybBRmbyl2IkEDOxByZSRWatBSbOR3IlgDUgJHIvJEa1xWLkJ1MQEUMuAjNwIzLwAjMxsTdgY3IpFEcwxGVlV2Sil2L0UzNz4yNzAiSoh0TUwUIsxGapU2RgV2aj82IpZFclNnbp42Nv4CIwNEco9mZt8SMxETMu4CN1YTLzEjNxBibNJ2bpUGUgF2YmJXLpUzNz4yNzBiVYV0LCUzMyUzTg1URXJURTsEMvAjMyAzM2QDTg1URXJURJ8CO0IDI51EYpJ3TvVWczV2ZuV2LygzMu4COz4CNyADKwBDM4gjMwIDN2YTIpdFQlh2dh9Cch0mN2BCZXlWa44WTgVmV0lHZw9SSXZUIJxEbhdmY1dWLlp3XoN0IOFESC9Sch0mN2BCat5WUpJHZvJ3bh9Se3lDOjIDZ1EGYxdTYiATM2UmO6AjO6AjO6EjO6EjO6EjO6AjO6cjY5MjZ4IjN5ImNzQTZ1NDOhJTYjhjZjUGN2EGZ0UDT3',
    'sa_distinct_id': 'TmYxczJQZzRBeHhxbGpJZWVhaEYyQT09',
    'um': 'fulizhuanqu',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5235 MMWEBSDK/20230604 MMWEBID/4829 MicroMessenger/8.0.38.2400(0x28002656) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx9c825da1a7ba062e',
    'x-euler-headers': 'appid;appkey;s_channel;s_version;sa_distinct_id;source_type;uc;um;us;ut;utm_campaign;utm_medium;utm_source;utm_term',
    'Accept': 'application/json, text/plain, */*',
    'source_type': '504',
    'utm_medium': 'direct',
    'appId': '',
    's_version': '',
    'us': 'minishouye',
    'utm_source': 'hdshare',
    'appKey': '',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://hd.opposhop.cn/bp/81ff2238516c3ca7?Personalized=1&_now_=1693580840342&appId=wx9c825da1a7ba062e&nightModelEnable=true&openId=o1yCe4qQqADxBAljpLEXzAjul8CE&uc=qiandao&um=fulizhuanqu&us=minishouye&utm_source=hdshare',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'ut=direct; utm_medium=direct; utm_campaign=direct; utm_term=direct; otrack_jssdk_store=eyJkZXZpY2VJZCI6IjYwOWE4NTExLTRlYTQtNGU3Mi04MmFlLTQ0YTU3YTgzZWM1MiIsInVzZXJJZCI6IiIsImN1c3RvbUF0dHJzIjp7InByb3BzIjp7fSwiaWRlbnRpdGllcyI6eyIkaWRlbnRpdHlfY29va2llX2lkIjoiNjA5YTg1MTEtNGVhNC00ZTcyLTgyYWUtNDRhNTdhODNlYzUyIiwiJGlkZW50aXR5X2Fub255bW91c19pZCI6IjYwOWE4NTExLTRlYTQtNGU3Mi04MmFlLTQ0YTU3YTgzZWM1MiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjYwOWE4NTExLTRlYTQtNGU3Mi04MmFlLTQ0YTU3YTgzZWM1MiJ9LCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4yNC42In0sImg1YXBwIjp7fX19; source_type=503; s_channel=program_wx; sa_distinct_id=TmYxczJQZzRBeHhxbGpJZWVhaEYyQT09; _ga_neftid=y5yMFYDjc0NBAhUREBaRyWSo5AR5McT1; newopkey=sbZaOFLH5M-3znsu2a5GYM_2wNyfrjubSd9TJw4UZ0Wv6G8AxnOAtIS_iezL9uZnwe47PlVY0u0; NEWOPPOSID=eyJpdiI6IlVUMmd6OGt2a0p3WDZUTS8xSVpCTkE9PSIsInZhbHVlIjoiQmd0NEhaNzZxMXIrU0RiZ2M2akhjWDhYNTdlaFk4N3dwdjVkYkNsK3dwSXpLaWJGZlpQZU9XL1dWUitWMUdnNFhLNm85RUQwam9KaVJJWXMzL3ZGL3pCT3B2MktjS3dlOGpUNmlCKzNFL0huTG53ODlrbzE1aURoNkpVdStCQ0oiLCJtYWMiOiIxOWVlMDc1MDlmNmQwN2Y5NWY1ZDE2ZjQ4ZDg2MzkzYTQ3MTViZjM3MGRlNzdiZjI3YjYwYWM3OGI5YTNjNWM2In0; acw_tc=2760823716935806882867088ee598bd05ea34ca4a5ba09d39b6c607765755; um=fulizhuanqu; utm_source=hdshare; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22TmYxczJQZzRBeHhxbGpJZWVhaEYyQT09%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22hdshare%22%2C%22%24latest_utm_medium%22%3A%22direct%22%2C%22%24latest_utm_campaign%22%3A%22direct%22%2C%22%24latest_utm_term%22%3A%22direct%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhNDk1MGFjNjY4LTA5ZWM5ZDlhNzE1YjNiOC01OTdiNzM2OS0zMzQ0NDMtMThhNDk1MGFjNjgxZTYiLCIkaWRlbnRpdHlfYW5vbnltb3VzX2lkIjoiVG1ZeGN6SlFaelJCZUhoeGJHcEpaV1ZoYUVZeVFUMDkifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218a4950ac668-09ec9d9a715b3b8-597b7369-334443-18a4950ac681e6%22%7D; us=minishouye; uc=qiandao; _ga_nefsid=DtFfpd6iSBZBVkQQAFKRnXYGMdX%2Bjfe8%40bj%2C1693584391016; obus-track_117500_session=HMaQAs5v,1693580688128,1693580911608'
}

response = requests.request("GET", url, headers=headers, data=payload,proxies=proxies,verify=False)

print(response.text)