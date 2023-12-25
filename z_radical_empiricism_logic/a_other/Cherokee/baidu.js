const translate = require("baidu-translate-api");
translate()
translate("hello", {
    from: "en",
    to: "fra"
}).then(res => {
    console.log('rex', res);
    console.log(res.trans_result.dst);
    // Let's translate it!
}).catch(err=> console.log("error " + JSON.stringify(err, null, 2)))