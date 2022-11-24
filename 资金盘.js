const $=new Env('资金盘')
let cookie='{"type":24,"_silent":true,"token":"3caea93d17a1274d41618145bb9098c4","method":"api.goldTask.ASMMember","device":"android"}'||process.env.jk160//user_key=0017338a6dc7374dd2ffb5d7af8f3e91SRrdDVXS20221206185848&cid=16
let cookies=[]
console.log(cookie)
// 16680519106688891
// let i;
// for(let i=16680519106688891;i<16680519106788891;i++){
//     console.log(i)
//     await $.wait(800)
//     await Bug(i)
//     await $.wait(200)
// }

// for(let index=0;index<cookies.length;index++){
//             let num=index+1
//             $.log(`======现在正在分割user_key和cid,正在获取数据类型======`)
//             data=cookies[index].split('&')
//             $.log(`这是分割完的json对象数据user_key和cid\n${data},数据类型为${typeof (data)}`)//将object中的对象变为数组
//             console.log(`这是分割完整的数据中的user_key保存在data[0]${data[0]}`)
//             console.log(`这是分割完整的数据中的cid保存在data[1]${data[1]}`)
//             data2=data[index].split('=')
//             $.log(`!!!!!!!!!!!这是测试连续分割字符串中的数据量!!!!!${data2}\n`)
//             $.log(`这是测试连续分割字符串出现的输出的前缀userkey在data2[0]中${data2[0]}`)
//             $.log(`这是测试连续分割字符串出现的输出的前缀userkey的数据值在data2[1]${data2[1]}`)
//             // console.log(data,typeof(data))
//             $.log(`======现在正在分割ascstoken和userId======`)
//             data1=asstokens[index].split('&')
//             console.log(`这是分割完的json对象数据asstoken和userId\n${data1},数据类型为${typeof (data1)}`)
//             console.log(`这是分割完整的数据中的accessToken保存在data1[0]${data1[0]}`)
//             console.log(`这是分割完整的数据中的userId保存在data1[1]${data1[1]}`)
//             data4=data1[1].split('=')
//             $.log(`这是测试分割出user_id在${data4}`)
//             data3=data1[index].split('=')
//             $.log(`!!!!!!!!!!!这是测试连续分割字符串中的数据量!!!!!${data3}\n`)
//             $.log(`这是测试连续分割字符串出现的输出的前缀accessToken在data3[0]中${data3[0]}`)
//             $.log(`这是测试连续分割字符串出现的输出的前缀accessToken的数据值在data3[1]${data3[1]}`)
//             // console.log(asstokens[0])
//             // console.log(data1,typeof (data1))
//             $.log(`=========开始第${num}个账户任务========\n\n`)
//             cookie=cookies[index]
//             $.log(`当前任务是查询签到状态+++`)//is_signed:1代表签到成功,反之如果为0代表签到不成功
//             await CheckSignIn()
//             await $.wait(2000)
//             $.log(`=====当前正在执行的是签到任务====`)
//             await SignIn()//这里是post请求的签到接口,正在执行签到任务
//             await $.wait(2000)
//             $.log(`开始查询任务列表...\n`)
//             await $.wait(2000)
//             $.log(`正在查询任务列表,目前仅支持点赞功能~~~`)
//             await SearchTask()
//             await $.wait(1000)
//             $.log(`====当前正在执行的是随机领取气泡球====`)
//             await $.wait(2000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             await  CollectBall()
//             await $.wait(1000)
//             $.log(`气泡球任务执行完成\n`)
//
//         }
!(async ()=>{
    if(cookie){
        for(i=16680519106688892;i<16680519106788891;i++){
            console.log(i)
            // await $.wait(800)
            await Bug(i)
            await $.wait(200)
        }
    }else {
        $.log(`\n请先获取cookie填入后在运行\n`)
    }
})()


function Bug (i) {
    return new Promise((resolve) => {
        let parms = {
            url: `https://shiapp.huajiet.com/api.html?XDEBUG_SESSION_START=16315&X-CSRF-TOKEN=${i}`,
            headers: {
                "Accept": "application/json",
                "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/27.636364)",
                "Content-Type": "application/json",
                "Content-Length": "122",
                "Host": "shiapp.huajiet.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "Cookie": "PHPSESSID=16680519106688764",
            },
            body:`${cookie}`
        };

        console.log(`================这里是测试显示请求的header中的参数================\n`);
        console.log(parms)//这里是显示原版的json数据格式的请求头
            // console.log(JSON.stringify(parms))

        console.log(parms.url)
        $.post(parms,async (error,response,data)=>{
            if(1){
                // console.log(`========这是测试获取请求后的响应数据========\n`)
                // console.log(response,typeof (response))
                // if((response.status===200)&&(response.statusCode===200)){
                //     $.log(`🎉🎉🎉🎉签到成功🎉🎉🎉🎉`)
                // }
                console.log(data,typeof (data))
                // let res=JSON.parse(data)
                // // console.log(res)
                // console.log(`当前正在二次校验返回值\n${res.error_msg}`)
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