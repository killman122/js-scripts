import ddddocr
import requests
from fake_useragent import UserAgent
useragent = UserAgent()
ua = useragent.edge
# print(useragent.edge)

headers = {
    "authority": "wpfx.org",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "user-agent": ua
}

url = "https://wpfx.org/core/code.php?7"
response = requests.get(url,headers=headers)
# with open("点选验证码.png","wb") as f:
#     f.write(response.content)

ocr = ddddocr.DdddOcr()
with open("点选验证码.png","rb") as f:
    img = f.read()
res = ocr.classification(img)
print(res)