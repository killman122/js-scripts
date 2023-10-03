import httpx, json

deeplx_api = "https://api.deeplx.org/translate"
# deeplx_api = "http://146.56.166.74:8080"

data = {
    "text": "Hello World",  # 将要翻译的文本写在text中
    "source_lang": "EN",  # 源语言
    "target_lang": "ZH"  # 目标语言
}

proxy = "http://127.0.0.1:10809"


# 使用httpx和使用request的区别在于,httpx不需要使用proxies参数,而是直接使用proxies = {"http": "http://

post_data = json.dumps(data)
# r = httpx.post(proxies=proxy, url=deeplx_api, data=post_data, verify=False).text
r = httpx.post(proxies=proxy, url=deeplx_api, json=data, verify=False).text # 在这里可以直接使用json.dumps(data)将json类型的数据传入到请求中,使用data参数,或者是直接使用json参数填写将字典类型的数据转换为json类型的数据
print(r)

