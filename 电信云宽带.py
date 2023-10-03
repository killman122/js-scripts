import time
from pprint import pprint
import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# print(f'现在的时间戳是{time.localtime()}')
# print(f'现在的时间戳转换为年月日的可利用格式为{time.strftime("%Y-%m-%d", time.localtime())}')
Cutten_time = time.strftime("%Y-%m-%d", time.localtime())
failed_list = [12, 18, 19, 20]
grade = ''

class DianXing():
    def __init__(self):
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXJyZW50VGltZU1pbGxpcyI6IjE2OTQ4NjE0OTk4NDciLCJleHAiOjE2OTYxNTc0OTksInVzZXJJZCI6IjM1NzU0NjEifQ.vwLUhTh5OpDZAvEzFgTRDixOFrjIr35zYNqd0h0TGAg',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36; superApp',
            'Origin': 'https://super.sh.189.cn',
            'X-Requested-With': 'com.shct.yi',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; _gscu_41114146=94861489465ikc14; _gscs_41114146=94861489kdfs9v14; _gscbrs_41114146=1; _gscu_1323353602=948614892mgiv414; _gscbrs_1323353602=1; _gscs_1323353602=94861489ximzs414|pv:2; TS01acc450=0191efafea5ceb125b48b8da6d6fdbcaf0d124dab1d169d2da27d826d14e11506f2b972766a5e68f401dc2ed1078c56ccc43e7919d',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
        }

    def CheckIn(self):
        url = 'https://super.sh.189.cn/app/user/integral/eventLabel/receive'
        # 向已经初始化的属性中添加新的值,也可以使用update的方法更新整个字典中的值
        self.headers['Host'] = 'super.sh.189.cn'
        headers = self.headers
        # print(self.headers)
        body = f'{{"activityCode":2,"eventCode":2,"day":"{Cutten_time}"}}'
        response = requests.post(url, data=body, headers=headers)
        # print(response.json())
        res = response.json().get('code')
        if res == 'SUCCESS':
            print('Success,签到成功')
        # print(res)

    #  在需要删除初始化属性中的某些参数时,我们可以使用pop()方法这个方法在字典中删除指定的键值,或者是使用del 字典名['键名']
    def Luck_lottery(self):
        url = 'https://l.sh.189.cn/calculate/lucky/draw'
        # self.headers = self.headers.pop('Authorization', None) # 当在pop方法调用后并赋值给左边变量,相当于,删除pop元素,并返回了删除的元素,所以是字符串类型的数据
        self.headers.pop('Authorization', None)  # 当在pop方法调用后并赋值给左边变量,相当于,删除pop元素,并返回了删除的元素,所以是字符串类型的数据
        self.headers.pop('Origin', None)
        self.headers.pop('Content-Type', None)
        self.headers['X-Requested-With'] = 'XMLHttpRequest'
        self.headers['Accept'] = '*/*'
        self.headers['Host'] = 'l.sh.189.cn'
        self.headers[
            'Cookie'] = '_gscu_860974136=94862193tjsdnw13; _gscbrs_860974136=1; _gscu_238178258=94913330rqze1g61; _gscbrs_238178258=1; svid=9C025C1EEEB0A79C3BA223E0CF53ED35; s_fid=753CBA622A773D88-108B92890381A771; lvid=9f688f38aec6dbd34c488e155f7f9ebc; nvid=1; s_cc=true; UM_distinctid=18aa0be78d12a-018c4acc04abcc-1d625971-51a6b-18aa0be78d226a; cna=f0bf9f3d61f640b29bdb46bfd476a168; SHOP-JSESSION-ID=YTRkYjc5OWMtMmI1Ny00YTU3LWIwMDAtOTk1ZTJkNDc4YTNh; Hm_lvt_15f3a5c5bd043f9dcee10253e2032754=1694926082; Hm_lpvt_15f3a5c5bd043f9dcee10253e2032754=1694926082; _gscu_146112875=94926082xasfcc84; _gscbrs_146112875=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_source%22%3A%22H5-VIP%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%22_latest_source%22%3A%22H5-VIP%22%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; JSESSIONID=516837DF01AB948D2B2276FB054AB37E; CNZZDATA1260456032=60220059-1694913952-%7C1695002357'
        # print(self.headers)
        headers = {
            'Host': 'l.sh.189.cn',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36; superApp',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': '_gscu_860974136=94862193tjsdnw13; _gscbrs_860974136=1; _gscu_238178258=94913330rqze1g61; _gscbrs_238178258=1; svid=9C025C1EEEB0A79C3BA223E0CF53ED35; s_fid=753CBA622A773D88-108B92890381A771; lvid=9f688f38aec6dbd34c488e155f7f9ebc; nvid=1; s_cc=true; UM_distinctid=18aa0be78d12a-018c4acc04abcc-1d625971-51a6b-18aa0be78d226a; cna=f0bf9f3d61f640b29bdb46bfd476a168; SHOP-JSESSION-ID=YTRkYjc5OWMtMmI1Ny00YTU3LWIwMDAtOTk1ZTJkNDc4YTNh; Hm_lvt_15f3a5c5bd043f9dcee10253e2032754=1694926082; Hm_lpvt_15f3a5c5bd043f9dcee10253e2032754=1694926082; _gscu_146112875=94926082xasfcc84; _gscbrs_146112875=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_source%22%3A%22H5-VIP%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%22_latest_source%22%3A%22H5-VIP%22%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; JSESSIONID=516837DF01AB948D2B2276FB054AB37E; CNZZDATA1260456032=60220059-1694913952-%7C1695002357'
        }
        parms = ''
        response = requests.get(url, headers=headers, params=parms)
        print(response.json())

    def TaskList(self):
        url = 'http://super.sh.189.cn/app/user/integral/eventLabel/cwTaskV2'
        self.headers.pop('Origin', None)
        headers = self.headers
        params = ''
        # self.headers.copy(headers)
        response = requests.get(url, headers=headers, params=params)
        # pprint(response.json()) # 格式化输出代码使用pprint,需要导入外部库,from pprint import pprint
        res = response.json()['data']
        # print(res)
        for i in res:
            # print(i)
            activityCode = i['activityCode']
            events = i['events']
            for event in events:
                eventCode = event['eventCode']
                bizLink = event['bizLink']
                bizType = event['bizType']
                bizId = event['bizId']
                taskRecordId = event.get('taskRecordId')
            print(f'activityCode是{activityCode},eventCode是{eventCode},bizLink是{bizLink}')
            dx.Browse_tasks(activityCode, eventCode, bizId, bizType, bizLink)
            time.sleep(1)
            dx.receiveV2(activityCode, eventCode,taskRecordId)

    def Browse_tasks(self, activityCode, eventCode, bizId, bizType, bizLink):
        url = 'https://super.sh.189.cn/app/user/integral/eventLabel/insertTaskEvent'
        self.headers[
            'Cookie'] = 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; _gscu_41114146=94861489465ikc14; _gscbrs_41114146=1; _gscu_1323353602=948614892mgiv414; _gscbrs_1323353602=1; _gscu_860974136=94862193tjsdnw13; _gscbrs_860974136=1; _gscs_41114146=t94911927couivv16; TS0112bd7c=0191efafeaaf26ceac7044d98c295649fa0280b259bd8e8426ec6b237326d0a76b8599adef06cb47a50febba38100e76a7ebdbdb38; _gscs_1323353602=t94911927qpftnv16|pv:5; _gscu_238178258=94913330rqze1g61; _gscbrs_238178258=1; _gscs_238178258=9491333044wqqn61|pv:1; svid=9C025C1EEEB0A79C3BA223E0CF53ED35; s_fid=753CBA622A773D88-108B92890381A771; lvid=9f688f38aec6dbd34c488e155f7f9ebc; nvid=1; s_cc=true; TS01acc450=0191efafea77b305e7a094101faf1748e8cf8e291c20235cbe45e909435656add29d4d0f205c302832032abda528b378aabee4f921; UM_distinctid=18aa0be78d12a-018c4acc04abcc-1d625971-51a6b-18aa0be78d226a; cna=f0bf9f3d61f640b29bdb46bfd476a168'
        headers = self.headers
        data = f'{{"activityCode": "{activityCode}", "eventCode": "{eventCode}"}}'  # 双花括号{{和}}会在字符串中转义为单个花括号{和}。因此，上述代码会生成形如{"activityCode": "some value", "eventCode": "some value"}的字符串
        response = requests.post(url, data=data, headers=headers)
        print(response.json())
        response = response.json()['success']
        if response == False:
            dx.GetH5Url(bizId=bizId, bizType=bizType, bizLink=bizLink)
            time.sleep(1)
        # 输出相关的结果后可以将失败的写在一个列表或者是文件中,方便下次直接读取比较,直接访问下一个函数

    def GetH5Url(self, bizId, bizType, bizLink):
        url = 'https://super.sh.189.cn/app/config/v4/getH5Url'
        self.headers['DSN'] = 'd55bd65c051f39078cd63b21c1647f2c|release'
        headers = self.headers
        data = f'{{"id":{bizId},"bizId":{bizId},"bizType":{bizType},"bizLink":"{bizLink}","source":"H5-VIP"}}'
        response = requests.post(url, data, headers=headers)
        print(response.json())

    def receiveV2(self,activityCode,eventCode,taskRecordId):
        url = 'https://super.sh.189.cn/app/user/integral/eventLabel/receiveV2'
        self.headers[
            'Cookie'] = 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; _gscu_41114146=94861489465ikc14; _gscbrs_41114146=1; _gscu_1323353602=948614892mgiv414; _gscbrs_1323353602=1; _gscu_860974136=94862193tjsdnw13; _gscbrs_860974136=1; TS0112bd7c=0191efafea8b574a087bac4963fa885231f9cc5376b96798bd6934b14da53db29f255097ff584b0594b5c45fb369f33aedc87853bb; _gscs_41114146=t94911927couivv16; _gscs_1323353602=t94911927qpftnv16|pv:2; TS01acc450=0191efafead84b9a9950b40ab187c96409b957920202aefced6b726fa49799ceda22c74e63c0b8f528301b88449c3de2c0b6b36ed0'
        headers = self.headers
        data = f'{{"activityCode":{activityCode},"eventCode":{eventCode},"taskRecordId":{taskRecordId}}}'
        response = requests.post(url, data, headers=headers)
        print(response.json())

        # send_message()


    def get_grade(self):
        url = 'https://super.sh.189.cn/app/user/integral/get'
        self.headers.pop('Content-Type', None)
        self.headers.pop('Origin', None)
        self.headers['Cookie'] = 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22MThhOWQ5ZGY2MmQyZC0wMTJjYmQxMTU4ZmM0NzEtMWQ2MjU5NzEtMzM0NDQzLTE4YTlkOWRmNjMxN2U%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%7D%2C%22%24device_id%22%3A%2218a9d9df62d2d-012cbd1158fc471-1d625971-334443-18a9d9df6317e%22%7D; _gscu_41114146=94861489465ikc14; _gscbrs_41114146=1; _gscu_1323353602=948614892mgiv414; _gscbrs_1323353602=1; _gscu_860974136=94862193tjsdnw13; _gscbrs_860974136=1; TS0112bd7c=0191efafea8b574a087bac4963fa885231f9cc5376b96798bd6934b14da53db29f255097ff584b0594b5c45fb369f33aedc87853bb; _gscs_41114146=t94911927couivv16; _gscs_1323353602=t94911927qpftnv16|pv:2; TS01acc450=0191efafead84b9a9950b40ab187c96409b957920202aefced6b726fa49799ceda22c74e63c0b8f528301b88449c3de2c0b6b36ed0'
        headers = self.headers
        params = ''
        response = requests.get(url, headers=headers, params=params)
        # print(response.json())
        name = response.json()['data']['name']
        Growth_value = response.json()['data']['periodVal']
        upper = response.json()['data']['upper']
        global grade
        grade = f'你当前的等级是{name},当前的成长值为{Growth_value},距离下一等级还剩{int(upper)-int(Growth_value)}'
        print(grade)




消息内容 = f'{grade}+'
mail_subject = ''
def send_message():
    username = "wjr2483484885@gmail.com"
    password = "mreqbrbcpsaeloma"
    mail_from = "wjr2483484885@gmail.com"
    mail_to = "2483484885@qq.com"
    mail_subject = "电信完成任务了"
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

if __name__ == '__main__':
    dx = DianXing()
    dx.get_grade()
    # print(dx.headers)
    # for key in dx.headers:
    #     print(key + ":" + dx.headers[key])
    # dx.CheckIn()
    # dx.Luck_lottery() # 经测试发现无法使用该方法由于ck更新过快,除非逆向出ck
    dx.TaskList()  #
    # send_message()
