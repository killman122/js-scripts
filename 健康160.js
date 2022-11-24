// const { link } = require("fs")
// const { title } = require("process")

const $=new Env('健康160')
let cookie='user_key=0720d3233b08a12953a50cd9b2e1e7afwFfjlFXl20221207184516&cid=16'||process.env.jk160//user_key=0017338a6dc7374dd2ffb5d7af8f3e91SRrdDVXS20221206185848&cid=16
let cookies=[]
let cookie1='__jsluid_s=fa20b42307e331e5286927060cb6bb04; NYKJSHADOW_v2=eyJrZXkiOiJjZGtkcGtxMGpmb3JvZnV0MWJzMGwxbGdxciIsInZhbCI6ImU0MGU1NDdlYTc1MDc1YjU5Nzg5YWQ2MjcxZmQ0YmM0IiwidG0iOjE2Njc4MTY2NTl9; last_city_id_v2=MzEzOQ==; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22263373259%22%2C%22first_id%22%3A%22184519e951f316-078b0fcd6e9e064-7523047f-329160-184519e952051b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fweixin.91160.com%2Fh5%2Fregister%2Fmain%2Findex.html%22%7D%2C%22%24device_id%22%3A%22184519e951f316-078b0fcd6e9e064-7523047f-329160-184519e952051b%22%7D; channel_id_v2=MTY=; location_city_id_v2=MzEzOQ==; ip_city_id_v2=MzEzOQ==; ip_city_name_v2=5LmM6bKB5pyo6b2Q5biC; user_id_v2=MjYzMzczMjU5; user_agent_v2=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMDUuMC4xMzQzLjUz; isLogined_v2=MQ==; useTokenTime_v2=dHJ1ZQ==; newToken_v2=NGQ5MTQzY2MzYzliM2VkMmExMzBhMDhkMTZlNjIyZGJ3cHhuZ0ZlcDIwMjIxMjA4MDgyNzQ1; client_uid_v2=leCwdHXnDBPgJItTYNI70TOcdsn0HxNtkqbnjDotmFZTh/8XPYjJhQDOCvpPXJn5; client_id_v2=M2Y3M2QwNjQ5MjUwYzQ0YmY0OTYzZDFhMGZmMTYxZGY=; account_user_user_id=263373259; Hm_lpvt_d4fe452b4b4d3072dfda2f68e7a19668_v2=RKvMwWIncDcfvi7beL2IIQ%3D%3D; Hm_lvt_d4fe452b4b4d3072dfda2f68e7a19668_v2=RKvMwWIncDcfvi7beL2IIQ%3D%3D; cur_city_id_v2=MzEzOA==; cur_area_id_v2=MzE1Mw==; lbs_city_id_v2=MzEzOA==; lbs_city_name_v2=5paw55aG; lbs_county_id_v2=MzE1Mw==; lbs_county_name_v2=; pos_source_v2=Z2FvZGU=; longitude_v2=ODYuMDgzMzUy; latitude_v2=NDQuMzA2MTQ=; advert=%7B%22client_id%22%3A%223f73d0649250c44bf4963d1a0ff161df%22%2C%22location_city_id%22%3A3139%7D'||process.env.cookie1
let asstoken='accessToken=0720d3233b08a12953a50cd9b2e1e7afwFfjlFXl20221207184516&userId=263373259'||process.env.jk160token
let asstokens=[]
let debug=0
let data=[]
let data1=[]
let point_sorts=[1,2,3,4]
let data2=[]
let data3=[]
let data4=[]
let time=new Date().getTime()
console.log(`当前的十三位的时间戳是${time}`)
let coments=['好','对','是']
let coment=coments[Math.floor(Math.random()*coments.length)]//随机评论
// console.log(coment)
// let point_sort=point_sorts[Math.floor(Math.random()*point_sorts.length)]随机领取积分球
// console.log(point_sort)

!(async ()=>{
    if(cookie){
        cookies=cookie.split('@')
        $.log(`总共有${cookies.length}个cookie`)
        asstokens=asstoken.split('@')
        $.log(`总共有${asstokens.length}个asstoken`)

        for(let index=0;index<cookies.length;index++){
            let num=index+1
            $.log(`======现在正在分割user_key和cid,正在获取数据类型======`)
            data=cookies[index].split('&')
            $.log(`这是分割完的json对象数据user_key和cid\n${data},数据类型为${typeof (data)}`)//将object中的对象变为数组
            console.log(`这是分割完整的数据中的user_key保存在data[0]${data[0]}`)
            console.log(`这是分割完整的数据中的cid保存在data[1]${data[1]}`)
            data2=data[index].split('=')
            $.log(`!!!!!!!!!!!这是测试连续分割字符串中的数据量!!!!!${data2}\n`)
            $.log(`这是测试连续分割字符串出现的输出的前缀userkey在data2[0]中${data2[0]}`)
            $.log(`这是测试连续分割字符串出现的输出的前缀userkey的数据值在data2[1]${data2[1]}`)
            // console.log(data,typeof(data))
            $.log(`======现在正在分割ascstoken和userId======`)
            data1=asstokens[index].split('&')
            console.log(`这是分割完的json对象数据asstoken和userId\n${data1},数据类型为${typeof (data1)}`)
            console.log(`这是分割完整的数据中的accessToken保存在data1[0]${data1[0]}`)
            console.log(`这是分割完整的数据中的userId保存在data1[1]${data1[1]}`)
            data4=data1[1].split('=')
            $.log(`这是测试分割出user_id在${data4}`)
            data3=data1[index].split('=')
            $.log(`!!!!!!!!!!!这是测试连续分割字符串中的数据量!!!!!${data3}\n`)
            $.log(`这是测试连续分割字符串出现的输出的前缀accessToken在data3[0]中${data3[0]}`)
            $.log(`这是测试连续分割字符串出现的输出的前缀accessToken的数据值在data3[1]${data3[1]}`)
            // console.log(asstokens[0])
            // console.log(data1,typeof (data1))
            $.log(`=========开始第${num}个账户任务========\n\n`)
            cookie=cookies[index]
            $.log(`当前任务是查询签到状态+++`)//is_signed:1代表签到成功,反之如果为0代表签到不成功
            await CheckSignIn()
            await $.wait(2000)
            $.log(`=====当前正在执行的是签到任务====`)
            await SignIn()//这里是post请求的签到接口,正在执行签到任务
            await $.wait(2000)
            $.log(`开始查询任务列表...\n`)
            await $.wait(2000)
            $.log(`正在查询任务列表,目前仅支持点赞功能~~~`)
            await SearchTask()
            await $.wait(1000)
            $.log(`====当前正在执行的是随机领取气泡球====`)
            await $.wait(2000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            await  CollectBall()
            await $.wait(1000)
            $.log(`气泡球任务执行完成\n`)

        }
    }else {
        $.log(`\n请先获取cookie填入后在运行\n`)
    }
})()

function CheckSignIn () {
    return new Promise((resolve) => {
        let parms = {
            url: `https://wechatgate.91160.com/user_point/v1/sign/next_period?${cookie}`,
            headers: {
                "Host": "wechatgate.91160.com",
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4829 MicroMessenger/8.0.21.2120(0x2800153B) Process/toolsmp WeChat/arm64 Weixin NetType/cmnet Language/zh_CN ABI/arm64",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://weixin.91160.com",
                "Referer": "https://weixin.91160.com/vue/userpoint/healthtown.html",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            },
        };
        if(debug){
            console.log(`================这里是测试显示请求的header中的参数================\n`);
            console.log(parms)//这里是显示原版的json数据格式的请求头
            // console.log(JSON.stringify(parms))
        }
        // console.log(parms.url)
        $.get(parms,async (error,response,data)=>{

            if(!debug){
                console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                if((response.status===200)&&(response.statusCode===200)){
                    $.log(`🎉🎉🎉🎉查询签到成功🎉🎉🎉🎉`)
                }
                // console.log(data,typeof (data))
                let res=JSON.parse(data)
                console.log(res)
                console.log(`查询返回状态值${res.error_msg}`)
                // console.log(`查询签到详情信息${JSON.stringify(res.sign_amount)}`)
            }resolve();
            if(error){
                console.log(`✨✨✨查询签到失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                console.log(`签到查询初始化成功!!!!`)
                return true
            }
        })
    });
}

function SignIn () {
    return new Promise((resolve) => {
        let parms = {
            url: `https://wechatgate.91160.com/user_point/v1/sign?${cookie}`,
            headers: {
                "Host": "wechatgate.91160.com",
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4829 MicroMessenger/8.0.21.2120(0x2800153B) Process/toolsmp WeChat/arm64 Weixin NetType/cmnet Language/zh_CN ABI/arm64",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://weixin.91160.com",
                "Referer": "https://weixin.91160.com/vue/userpoint/healthtown.html",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            body:`${cookie}`
        };
        if(debug){
            console.log(`================这里是测试显示请求的header中的参数================\n`);
            console.log(parms)//这里是显示原版的json数据格式的请求头
            // console.log(JSON.stringify(parms))
        }
        console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                if((response.status===200)&&(response.statusCode===200)){
                    $.log(`🎉🎉🎉🎉签到成功🎉🎉🎉🎉`)
                }
                // console.log(data,typeof (data))
                let res=JSON.parse(data)
                // console.log(res)
                console.log(`当前正在二次校验返回值\n${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨签到失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}
// console.log(point_sorts[0],point_sorts[1],point_sorts[2])

function CollectBall () {
    return new Promise((resolve) => {
        let point_sort=point_sorts[Math.floor(Math.random()*point_sorts.length)]
        let parms = {
            url: `https://wechatgate.91160.com/user_point/v1/point/bubble/receive?${cookie}`,
            headers: {
                "Host": "wechatgate.91160.com",
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4829 MicroMessenger/8.0.21.2120(0x2800153B) Process/toolsmp WeChat/arm64 Weixin NetType/cmnet Language/zh_CN ABI/arm64",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://weixin.91160.com",
                "Referer": "https://weixin.91160.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            body:`{"${data2[0]}":"${data2[1]}","point_sort":${point_sort}}`
        };
        if(debug){
            console.log(`================这里是测试显示请求的header中的参数================\n`);
            console.log(parms)//这里是显示原版的json数据格式的请求头
            // console.log(JSON.stringify(parms))
        }
        console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                if((response.status===200)&&(response.statusCode===200)){
                    $.log(`🎉🎉🎉🎉收取积分球初始化成功🎉🎉🎉🎉`)
                }
                // console.log(data,typeof (data))
                let res=JSON.parse(data)
                // console.log(res)
                console.log(`当前正在二次校验返回值${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨领取失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}


function SearchTask () {
    return new Promise((resolve) => {
        let parms = {
            url: `https://wechatgate.91160.com/user_point/v2/task/daily?user_key=${data2[1]}&tsp=v_${time}&${data[1]}`,
            headers: {
                "Host": "wechatgate.91160.com",
                "Connection": "keep-alive",
                "Accept": "application/json, text/plain, */*",
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/4829 MicroMessenger/8.0.21.2120(0x2800153B) Process/toolsmp WeChat/arm64 Weixin NetType/cmnet Language/zh_CN ABI/arm64",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://weixin.91160.com",
                "Referer": "https://weixin.91160.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            },
        };
        if(debug){
            console.log(`================这里是测试显示请求的header中的参数================\n`);
            console.log(parms)//这里是显示原版的json数据格式的请求头
            // console.log(JSON.stringify(parms))
        }
        console.log(parms.url)
        $.get(parms,async (error,response,data)=>{
            if(!debug){
                console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status==200)&&(response.statusCode==200)){
                //     $.log(`🎉🎉🎉🎉查询现有任务初始化成功🎉🎉🎉🎉`)
                // }
                // console.log(data,typeof (data))
                let task=JSON.parse(data)
                // $.log(task)
                // let task1=JSON.stringify(task.data.list)
                // $.log(`${task1}`)
                // $.log(`${typeof(task1)}`)
                // $.log(`现在是测试${task.data.list[1].total}`)
                $.log(`现在测试输出存在的最后一个任务序列${task.data.list.length}`)
                $.log(`恭喜你,现在${task.data.list[(task.data.list.length)-2].total}个评论任务可以做并未作`)
                // $.log(`测试,现在有${task.data.list[(task.data.list.length)-1].total}个点赞任务可以做并未作`)
                $.log(`恭喜你,现在有${task.data.list[(task.data.list.length)-1].total}个点赞任务可以做并未作`)
                // $.log(`恭喜你,现在有${task.data.list[2].total}个点赞任务可以做并未作`)
                $.log(`当前是测试数据的长度${(task.data.list[2].tasks).length}`)
                let len=(task.data.list.length)-1
                let len1=(task.data.list.length)-2
                // for(let index=0;index<(task.data.list[2].tasks).length;index++){
                //     console.log(`这里是当前的第${index+1}个任务输出信息`)
                //     $.log(`当前是测试寻找存在的taskid${task.data.list[2].tasks[index].task_id}`)
                //     let task_id=task.data.list[2].tasks[index].task_id
                //     $.log(`当前是测试寻找存在的title${task.data.list[2].tasks[index].title}`)
                //     let title=task.data.list[2].tasks[index].title
                //     $.log(`当前是测试要请求的链接地址${task.data.list[2].tasks[index].link}`)
                //     let link=task.data.list[2].tasks[index].link

                $.log(`测试______${task.data.list[len].tasks}`)
                for(let index=0;index<(task.data.list[len].tasks).length;index++){
                    console.log(`这里是当前的第${index+1}个任务输出信息`)
                    $.log(`当前是测试寻找存在的taskid${task.data.list[len].tasks[index].task_id}`)
                    let task_id=task.data.list[len].tasks[index].task_id
                    $.log(`当前是测试寻找存在的title${task.data.list[len].tasks[index].title}`)
                    let title=task.data.list[len].tasks[index].title
                    $.log(`当前是测试要请求的链接地址${task.data.list[len].tasks[index].link}`)
                    let link=task.data.list[len].tasks[index].link
                    // if(title==医生短视频){
                    //     ZSP () 
                    // }else if(title==)
                    console.log(title)
                    if(task.data.list[len].tasks[index].status===1){
                        console.log(`${title}任务已完成`)
                    }
                    if(title==="点赞医生短视频"){
                        console.log(`查询医生短视频成功===========\n`)
                        $.log(`******预执行赞函数👍👍👍👍👍👍`)
                        await ZSP(task_id)
                    }
                    if(title!=="点赞医生短视频"){
                        console.log(`查询文章成功===========\n`)
                        let link_html=link.match(/[0-9]+\.html/g)
                        console.log(`link_html是------${link_html},数据类型为${typeof(link_html)}`)
                        link_html=JSON.stringify(link_html)
                        let link_id=link_html.match(/[0-9]+/g)
                        console.log(`link_id是===>${link_id}`) 
                        $.log(`******预执行ZArticle`)
                        await ZArticle(task_id,link_id)
                    }
                    if(title==="点赞医生科普"){
                        console.log(`查询医生科普成功========\n`)
                        let link_html=link.match(/object_id=[0-9]+/g)
                        link_html=JSON.stringify(link_html)
                        let link_id=link_html.match(/[0-9]+/g)
                        console.log(`link_id是==>${link_id}`)
                        $.log(`******预执行ZDocSay`)
                        await ZDocSay(task_id,link_id)
                    }
                    $.log(`====正在准备领取奖励====`)
                    await ReceiveAward(task_id)
                    $.log(`第${index+1}次任务领取奖励成功!!!`)
                }
                // console.log(length())
                for(let index=0;index<(task.data.list[len1].tasks).length;index++){
                    console.log(`这里是当前的第${index+1}个任务输出信息`)
                    $.log(`当前是测试寻找存在的taskid${task.data.list[len1].tasks[index].task_id}`)
                    let task_id=task.data.list[len1].tasks[index].task_id
                    $.log(`当前是测试寻找存在的title${task.data.list[len1].tasks[index].title}`)
                    let title=task.data.list[len1].tasks[index].title
                    $.log(`当前是测试要请求的链接地址${task.data.list[len1].tasks[index].link}`)
                    let link=task.data.list[len1].tasks[index].link
                    console.log(title)
                    if(task.data.list[len1].tasks[index].status===1){
                        console.log(`${title}任务已完成`)
                    }
                    if(title==="给健康早报留言 "||title=="给晚安心语留言 "){
                        console.log(`查询留言成功===========\n`)
                        let link_html=link.match(/[0-9]+\.html/g)
                        console.log(`link_html是------${link_html},数据类型为${typeof(link_html)}`)
                        link_html=JSON.stringify(link_html)
                        let link_id=link_html.match(/[0-9]+/g)
                        console.log(`link_id是===>${link_id}`) 
                        $.log(`******预执行Comment`)
                        await Comment(task_id,link_id)
                    }
                    
                    $.log(`====正在准备领取奖励====`)
                    await ReceiveAward(task_id)
                    $.log(`第${index+1}次任务领取奖励成功!!!`)
                }

            }resolve();
            if(error){
                console.log(`✨✨✨失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}

$.log(JSON.stringify(data[0]),data[0])
// $.log(`{"${data2[0]}":"${data2[1]}","point_sort":${point_sort}}`)
/**
 * 随机整数生成
 */
 function randomInt() {
    return Math.round(Math.random() * (2 - 0) + 0)
}

// $.log(`https://wechatgate.91160.com/user_point/v2/task/daily?user_key=${data2[1]}&tsp=v_${time}&${data[1]}`)
     

function ZSP (task_id) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://wechatgate.91160.com/note/pub/v1/like?${data[1]}&${data1[0]}&${data[0]}`,
            headers: {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Length": "148",
                "Content-Type": "application/json; charset=UTF-8",
                "Host": "snsapi.91160.com",
                "Origin": "https://weixin.91160.com",
                "Pragma": "no-cache",
                "Referer": "https://weixin.91160.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53",
                "X-Requested-With": "XMLHttpRequest",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
            },
            body:`{"likeType":1,"likeId":501725,"userId":263373259,"userProId":1,"accessToken":"${data3[1]}","taskId":${task_id}}`
        };
        // console.log(`++++++++++++++++++++这里是测试是否执行zsp函数++++++++`)
        // console.log(`================这里是测试显示请求的header中的参数================\n`);
        // console.log(parms)//这里是显示原版的json数据格式的请求头
        // if(debug){
        // console.log(`================这里是测试显示请求的header中的参数================\n`);
        // console.log(parms)//这里是显示原版的json数据格式的请求头
        // console.log(JSON.stringify(parms))
        // }
        // console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status==200)&&(response.statusCode==200)){
                //     $.log(`🎉🎉🎉🎉收取积分球初始化成功🎉🎉🎉🎉`)
                // }
                console.log(data,typeof (data))
                let data1=JSON.parse(data)
                $.log(`点赞视频任务${data1.msg}!!!!`)
                // let res=JSON.parse(data)
                // console.log(res)
                // console.log(`当前正在二次校验返回值${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨领取失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}




function ZArticle (task_id,link_id) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://weixin.91160.com/wapnews/like.html?type=good&id=${link_id}&${data[1]}&jstoken=&task_id=${task_id}`,
            headers: {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Host": "weixin.91160.com",
                "Pragma": "no-cache",
                // "Referer": `"https://weixin.91160.com/news/zaobao/25060.html?task_id=${task_id}&business_mark=health_news&action=action_like&object_id=&time_limit=5&amount=5"`,
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53",
                "X-Requested-With": "XMLHttpRequest",
                "Cookie":`${cookie1}`
            }
        };
        $.get(parms,async (error,response,data)=>{
            if(!debug){
                console.log(data,typeof (data))
                
            }resolve();
            if(error){
                console.log(`✨✨✨赞文章失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}




function ReceiveAward (task_id) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://wechatgate.91160.com/user_point/v1/task/prize?${cookie}`,
            headers: {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Length": "19",
                "Content-Type": "application/json; charset=UTF-8",
                "Host": "wechatgate.91160.com",
                "Origin": "https://weixin.91160.com",
                "Pragma": "no-cache",
                "Referer": "https://weixin.91160.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.53",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
            },
            body:`{"task_ids":[${task_id}]}`
        };
        // console.log(`++++++++++++++++++++这里是测试是否执行zsp函数++++++++`)
        // console.log(`================这里是测试显示请求的header中的参数================\n`);
        // console.log(parms)//这里是显示原版的json数据格式的请求头
        // if(debug){
        // console.log(`================这里是测试显示请求的header中的参数================\n`);
        // console.log(parms)//这里是显示原版的json数据格式的请求头
        // console.log(JSON.stringify(parms))
        // }
        // console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status==200)&&(response.statusCode==200)){
                //     $.log(`🎉🎉🎉🎉收取积分球初始化成功🎉🎉🎉🎉`)
                // }
                console.log(data,typeof (data))
                let data1=JSON.parse(data)
                $.log(`领取奖励任务${data1.data}!!!!`)
                // let res=JSON.parse(data)
                // console.log(res)
                // console.log(`当前正在二次校验返回值${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨领取失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}

function ZDocSay (task_id,link_id) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://weixin.91160.com/do/likedocsay?${data[1]}&${data[0]}`,
            headers: {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Length": "34",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": `${cookie1}`,
                "Host": "weixin.91160.com",
                "Origin": "https://weixin.91160.com",
                "Pragma": "no-cache",
                // "Referer": "https://weixin.91160.com/h5/wecontent/doctorarticle/detail.html?id=351837&task_id=6335&business_mark=content_article_doctor&action=action_like&object_id=351837&time_limit=5&amount=5",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/105.0.0.0",
                "X-Requested-With": "XMLHttpRequest",
            },
            // body:"text_id=351837&type=2&task_id=6335"
            body:`text_id=${link_id}&type=2&task_id=${task_id}`
        };
        console.log(`++++++++++++++++++++这里是测试是否执行ZDocSay函数++++++++`)
        console.log(`================这里是测试显示请求的header中的参数================\n`);
        console.log(parms)//这里是显示原版的json数据格式的请求头

        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status==200)&&(response.statusCode==200)){
                //     $.log(`🎉🎉🎉🎉收取积分球初始化成功🎉🎉🎉🎉`)
                // }
                console.log(data,typeof (data))
                let data1=JSON.parse(data)
                $.log(`点赞医生说任务${data1.msg}!!!!`)
                // let res=JSON.parse(data)
                // console.log(res)
                // console.log(`当前正在二次校验返回值${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨领取失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}


function Comment (task_id,link_id) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://weixin.91160.com/comments/v1.0/answering/add?${cookie}`,
            headers: {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                // "Content-Length": "163",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "wechatgate.91160.com",
                "Origin": "https://weixin.91160.com",
                "Pragma": "no-cache",
                "Referer": "https://weixin.91160.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/105.0.0.0",
            },
            body:`{"union_id":${link_id},"content":"${coment}","reply_type":8,"user_id":${data4[1]},"user_key":"${data2[1]}","cid":"16","task_id":${task_id}}`
        };
        // console.log(`++++++++++++++++++++这里是测试是否执行zsp函数++++++++`)
        // console.log(`================这里是测试显示请求的header中的参数================\n`);
        // console.log(parms)//这里是显示原版的json数据格式的请求头
        // if(debug){
        console.log(`================这里是测试显示请求的header中的参数================\n`);
        console.log(parms)//这里是显示原版的json数据格式的请求头
        // console.log(JSON.stringify(parms))
        // }
        // console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(!debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status==200)&&(response.statusCode==200)){
                //     $.log(`🎉🎉🎉🎉收取积分球初始化成功🎉🎉🎉🎉`)
                // }
                console.log(data,typeof (data))
                let data1=JSON.parse(data)
                // $.log(`点赞视频任务${data1.msg}!!!!`)
                // let res=JSON.parse(data)
                // console.log(res)
                // console.log(`当前正在二次校验返回值${res.error_msg}`)
            }resolve();
            if(error){
                console.log(`✨✨✨领取失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                // console.log(`签到初始化成功!!!!`)
                return true
            }
        })
    });
}





function Env(t, e) {
    "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0);

    class s {
        constructor(t) {
            this.env = t
        }

        send(t, e = "GET") {
            t = "string" == typeof t ? {url: t} : t;
            let s = this.get;
            return "POST" === e && (s = this.post), new Promise((e, i) => {
                s.call(this, t, (t, s, r) => {
                    t ? i(t) : e(s)
                })
            })
        }

        get(t) {
            return this.send.call(this.env, t)
        }

        post(t) {
            return this.send.call(this.env, t, "POST")
        }
    }

    return new class {
        constructor(t, e) {
            this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`)
        }

        isNode() {
            return "undefined" != typeof module && !!module.exports
        }

        isQuanX() {
            return "undefined" != typeof $task
        }

        isSurge() {
            return "undefined" != typeof $httpClient && "undefined" == typeof $loon
        }

        isLoon() {
            return "undefined" != typeof $loon
        }

        toObj(t, e = null) {
            try {
                return JSON.parse(t)
            } catch {
                return e
            }
        }

        toStr(t, e = null) {
            try {
                return JSON.stringify(t)
            } catch {
                return e
            }
        }

        getjson(t, e) {
            let s = e;
            const i = this.getdata(t);
            if (i) try {
                s = JSON.parse(this.getdata(t))
            } catch {
            }
            return s
        }

        setjson(t, e) {
            try {
                return this.setdata(JSON.stringify(t), e)
            } catch {
                return !1
            }
        }

        getScript(t) {
            return new Promise(e => {
                this.get({url: t}, (t, s, i) => e(i))
            })
        }

        runScript(t, e) {
            return new Promise(s => {
                let i = this.getdata("@chavy_boxjs_userCfgs.httpapi");
                i = i ? i.replace(/\n/g, "").trim() : i;
                let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");
                r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r;
                const [o, h] = i.split("@"), n = {
                    url: `http://${h}/v1/scripting/evaluate`,
                    body: {script_text: t, mock_type: "cron", timeout: r},
                    headers: {"X-Key": o, Accept: "*/*"}
                };
                this.post(n, (t, e, i) => s(i))
            }).catch(t => this.logErr(t))
        }

        loaddata() {
            if (!this.isNode()) return {};
            {
                this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path");
                const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile),
                    s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e);
                if (!s && !i) return {};
                {
                    const i = s ? t : e;
                    try {
                        return JSON.parse(this.fs.readFileSync(i))
                    } catch (t) {
                        return {}
                    }
                }
            }
        }

        writedata() {
            if (this.isNode()) {
                this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path");
                const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile),
                    s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data);
                s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r)
            }
        }

        lodash_get(t, e, s) {
            const i = e.replace(/\[(\d+)\]/g, ".$1").split(".");
            let r = t;
            for (const t of i) if (r = Object(r)[t], void 0 === r) return s;
            return r
        }

        lodash_set(t, e, s) {
            return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t)
        }

        getdata(t) {
            let e = this.getval(t);
            if (/^@/.test(t)) {
                const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : "";
                if (r) try {
                    const t = JSON.parse(r);
                    e = t ? this.lodash_get(t, i, "") : e
                } catch (t) {
                    e = ""
                }
            }
            return e
        }

        setdata(t, e) {
            let s = !1;
            if (/^@/.test(e)) {
                const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i),
                    h = i ? "null" === o ? null : o || "{}" : "{}";
                try {
                    const e = JSON.parse(h);
                    this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i)
                } catch (e) {
                    const o = {};
                    this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i)
                }
            } else s = this.setval(t, e);
            return s
        }

        getval(t) {
            return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null
        }

        setval(t, e) {
            return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null
        }

        initGotEnv(t) {
            this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar))
        }

        get(t, e = (() => {
        })) {
            t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, {"X-Surge-Skip-Scripting": !1})), $httpClient.get(t, (t, s, i) => {
                !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i)
            })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, {hints: !1})), $task.fetch(t).then(t => {
                const {statusCode: s, statusCode: i, headers: r, body: o} = t;
                e(null, {status: s, statusCode: i, headers: r, body: o}, o)
            }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => {
                try {
                    if (t.headers["set-cookie"]) {
                        const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();
                        s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar
                    }
                } catch (t) {
                    this.logErr(t)
                }
            }).then(t => {
                const {statusCode: s, statusCode: i, headers: r, body: o} = t;
                e(null, {status: s, statusCode: i, headers: r, body: o}, o)
            }, t => {
                const {message: s, response: i} = t;
                e(s, i, i && i.body)
            }))
        }

        post(t, e = (() => {
        })) {
            if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, {"X-Surge-Skip-Scripting": !1})), $httpClient.post(t, (t, s, i) => {
                !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i)
            }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, {hints: !1})), $task.fetch(t).then(t => {
                const {statusCode: s, statusCode: i, headers: r, body: o} = t;
                e(null, {status: s, statusCode: i, headers: r, body: o}, o)
            }, t => e(t)); else if (this.isNode()) {
                this.initGotEnv(t);
                const {url: s, ...i} = t;
                this.got.post(s, i).then(t => {
                    const {statusCode: s, statusCode: i, headers: r, body: o} = t;
                    e(null, {status: s, statusCode: i, headers: r, body: o}, o)
                }, t => {
                    const {message: s, response: i} = t;
                    e(s, i, i && i.body)
                })
            }
        }

        time(t, e = null) {
            const s = e ? new Date(e) : new Date;
            let i = {
                "M+": s.getMonth() + 1,
                "d+": s.getDate(),
                "H+": s.getHours(),
                "m+": s.getMinutes(),
                "s+": s.getSeconds(),
                "q+": Math.floor((s.getMonth() + 3) / 3),
                S: s.getMilliseconds()
            };
            /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length)));
            for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length)));
            return t
        }

        msg(e = t, s = "", i = "", r) {
            const o = t => {
                if (!t) return t;
                if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? {"open-url": t} : this.isSurge() ? {url: t} : void 0;
                if ("object" == typeof t) {
                    if (this.isLoon()) {
                        let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"];
                        return {openUrl: e, mediaUrl: s}
                    }
                    if (this.isQuanX()) {
                        let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl;
                        return {"open-url": e, "media-url": s}
                    }
                    if (this.isSurge()) {
                        let e = t.url || t.openUrl || t["open-url"];
                        return {url: e}
                    }
                }
            };
            if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) {
                let t = ["", "==============📣系统通知📣=============="];
                t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t)
            }
        }

        log(...t) {
            t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator))
        }

        logErr(t, e) {
            const s = !this.isSurge() && !this.isQuanX() && !this.isLoon();
            s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t)
        }

        wait(t) {
            return new Promise(e => setTimeout(e, t))
        }

        done(t = {}) {
            const e = (new Date).getTime(), s = (e - this.startTime) / 1e3;
            this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t)
        }
    }(t, e)
}