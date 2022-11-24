module.exports = {
    "id": "dt",
    "name": "读特",
    "keys": ["dturl","dturl2","dturl3","dturl4","dturl5"],
    "author": "@tom",
    "settings": [{
      "id": "dtSuffix",
      "name": "当前账号",
      "val": "1",
      "type": "number",
      "desc": "当前抓取ck记录的账号序号，如：1、2、3、4"
    }, {
      "id": "dtCount",
      "name": "账号个数",
      "val": "1",
      "type": "number",
      "desc": "指定任务最多跑几个账号，根据抓取的账号数据个数来设值"
    }, {
      "id": "dtXH",
      "name": "循环获取ck",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtTXTX",
      "name": "txtx",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtSC",
      "name": "sc",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtnotifyttt",
      "name": "推送控制",
      "val": "1",
      "type": "number",
      "desc": "0关闭，1推送,默认12点以及23点推送"
    }, {
      "id": "dtnotifyInterval",
      "name": "通知控制",
      "val": "2",
      "type": "number",
      "desc": "0关闭，1为 所有通知，2为 12，23 点通知，3为 6，12，18，23 点通知"
    }, {
      "id": "dtMinutes",
      "name": "推送-通知 分钟控制",
      "val": "10",
      "type": "number",
      "desc": "推送以及通知控制在什么分钟段，可设置0-59,默认0到10"
    }],
    "repo": "https://raw.githubusercontent.com/xl2101200/-/main/dt.js",
    "icons": ["https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg", "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg"],
    "script": "https://raw.githubusercontent.com/xl2101200/-/main/dt.js",
    "icon": "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg",
    "favIcon": "mdi-star-outline",
    "favIconColor": "grey",
    "datas": [{
      "key": "dturl",
      "val": "https://plus.dutenews.com/api/v2/auth/logindute?app_version=6.3.1&clientid=1&device_id=0ddd2034-1e48-44d8-ac84-46247ab4ac18&ip=100.100.100.100&memberid=760532&mobile=15933580813&nickname=159***813&sign=43d5151da9750493bff296c8c48845f8&siteid=10001&system-name=android&type=android&time=1633852509617"
    }, {
      "key": "dturl2",
      "val": ""
    }, {
      "key": "dturl3",
      "val": ""
    }, {
      "key": "dturl4",
      "val": ""
    }, {
      "key": "dturl5",
      "val": ""
    }],
    "sessions": [],
    "isLoaded": true
  }
  