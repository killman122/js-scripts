const $=new Env('超市合伙人')
let auth='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwcm9kIiwiaWF0IjoxNjc0MzIwNDM2LCJleHAiOjE2NzY5MTI0MzYsIm5iZiI6MTY3NDMyMDQzNiwidWlkIjoxMjQ0MTd9.wyCwtEE3x7fygU4sLh2eR5n3UzvqoWpbvEoo8I3X3f8'||process.env.cshhr
let auths=[]
let debug=1
let time=new Date().getTime()
console.log(`当前的十三位的时间戳是${time}`)
let coments=['好','对','是']
let coment=coments[Math.floor(Math.random()*coments.length)]//随机评论
let res2,sit_a,sit_b
let i=1
let res3=0

!(async ()=>{
    if(auth){
        auths=auth.split('@')
        $.log(`总共有${auths.length}个auth`)
        $.log(typeof auths)
        for(let index=0;index<auths.length;index++){
            // let num=index+1
            // console.log(num)
            console.log(auths[index])
            $.log(`正在获取用户信息,确定合成位置`)
            await get_user_info()
            await user_buy()
            // await user_update_gold()
            await get_list()
            await open_gold()
        }
    }else {
        $.log(`\n请先获取auth填入后在运行\n`)
    }
})()

function get_user_info() {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/user/get_user_info`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auth,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
            },
            body:`{}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                if((response.status===200)&&(response.statusCode===200)){
                    $.log(`🎉🎉🎉🎉查询用户信息请求成功🎉🎉🎉🎉`)
                }
                // console.log(data,typeof (data))
                let res=JSON.parse(data)//string转json
                // console.log(res,typeof res)
                // let res1=res['data']
                res2=res.data.buy_id
                $.log(`当前欲购买的商品id是${res2}`)
                console.log(res.data.positionInfo,typeof res.data.positionInfo)
                let res1=res.data.positionInfo
                let k
                let a=[]
                for( k in res1){
                    // $.log(k)
                    $.log(`第${k}号位置,等级为${res1[k].lv}`)
                    a.push(res1[k].lv)
                }
                $.log(a)

                same()
                function same(){
                    for (let i=0;i<=a.length;i++){
                        // console.log(i)
                        // console.log(`正在测试${a[i]}`)
                        for(let j=i+1;j<=a.length;j++){
                            if((a[i]===a[j])&&(a[j]!=0)){
                                // console.log(i+1,j+1)
                                sit_a=i+1
                                sit_b=j+1
                                user_move(sit_a,sit_b)
                                a.pop()
                            }
                        }
                    }
                }
                // $.log(res.data.positionInfo['1'])
                if(res.msg=='success'){
                    $.log(`已完成获取用户信息`)
                    // $.log(`正在获取位置${res1}`)
                }else {
                    await $.wait(20000)
                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                return true
            }
        })
    });
}


function open_gold() {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/timing/open_gold`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auth,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)"
            },
            body:`{}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                if((response.status===200)&&(response.statusCode===200)){
                    $.log(`🎉🎉🎉🎉领取金币红包请求成功🎉🎉🎉🎉`)
                }
                // console.log(data,typeof (data))
                let res=JSON.parse(data)//string转json
                console.log(res,typeof res)
                if(res.msg=='success'){
                    $.log(`已完成红包领取`)
                    // $.log(`正在获取位置${res1}`)
                }else {
                    if(res.msg!='今日红包已领完'){
                        await $.wait(20000)
                        $.log(`红包已经领取过,请等待`)
                        await $.wait(500000)
                        await open_gold()
                    }

                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                return true
            }
        })
    });
}

function user_buy() {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/user/user_buy`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auth,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
            },
            body:`{"buy_id":${res2},"type":1}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // console.log(data,typeof (data))
                let res=JSON.parse(data)//string转json
                console.log(res,typeof res)
                let r0=res.data
                console.log(r0,typeof r0)
                // let r1=r0['buy_price']
                // let r2=r0.assets
                if(res.msg=='success'){
                    let r1=r0['buy_price']
                    let r2=r0.assets
                    $.log(`用户购买成功`)
                    if(r2>=r1&&res['code']!=400){
                        await $.wait(20000)
                        await user_buy()

                    }
                }else {
                    await $.wait(20000)

                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                return true
            }
        })
    });
}

function user_move(sit_a,sit_b) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/user/user_move`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auth,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
            },
            body:`{"position_id_one":${sit_a},"position_id_two":${sit_b},"type":1}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){
                // console.log(data,typeof (data))
                let res=JSON.parse(data)//string转json
                console.log(res,typeof res)
                // let res1=res['data']

                // $.log(res.data.positionInfo['1'])
                if(res.msg=='success'){
                    $.log(`已完成商品的合成`)
                    // $.log(`正在获取位置${res1}`)
                    await $.wait(20000)
                    await get_user_info()
                }else {
                    await $.wait(20000)
                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                return true
            }
        })
    });
}


function user_update_gold() {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/user/user_update_gold`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auths,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
                "Connection": "Keep-Alive",
            },
            body:`{}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // console.log(data,typeof (data))
                let res=JSON.parse(data)//string转json
                // console.log(res,typeof res)
                let res1=res.data['assets']
                console.log(`正在测试res1的值和数据类型${res1,typeof res1}`)
                if(res.msg=='success'){
                    $.log(`已完成金币领取`)
                    if(res3!=res1){
                        for(i;i<=100;i++){
                            $.log(`预计将再领取${100-i}次`)
                            $.log(res1)
                            i=i+1
                            res3=res1

                            await $.wait(200)
                            await user_update_gold()
                        }

                        await open_gold()
                        // $.log(`正在获取位置${res1}`)
                    }

                }else {
                    await $.wait(20000)
                    $.log(`开金币失败`)

                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
                return true
            }
        })
    });
}

function get_list() {
    return new Promise((resolve) => {
        let parms = {
            url: `https://cs.taoliutech.com/game/api/v1/task/get_list`,
            headers: {
                "Host": "cs.taoliutech.com",
                "Accept-Encoding": "gzip, deflate",
                "Gameversion": "1.0.331",
                "Authorization": auth,
                "Versioncode": "331",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
                "Connection": "Keep-Alive",
            },
            body:`{"type":"1"}`
        };
        //两种 $.log(parms.url)     $.log(parms['url'])
        $.post(parms,async (error,response,data)=>{
            if(debug){

                let res=JSON.parse(data)//string转json
                if(res.msg=='success'){
                    $.log(`已完成任务列表的获取`)
                    $.log(res['data'].list,typeof res['data'].list)

                }else {

                    await $.wait(20000)
                    $.log(`开金币失败`)

                }
            }resolve();
            if(error){
                console.log(`✨✨✨任务失败,脚本参数问题请检查并升级脚本`)
                return false
            }else {
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