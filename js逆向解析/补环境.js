// npm install jsdom
//目标是模拟足够的Web浏览器子集，以便用于测试和挖掘真实世界的Web应用程序
const jsdom = require("jsdom");  // 引入 jsdom
const { JSDOM } = jsdom;  // 引出 JSDOM 类， 等同于 JSDOM = jsdom.JSDOM

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);  // 创建DOM对象(浏览器)
window = dom.window
console.log(dom.window.document.querySelector("p").textContent);

const dom = new JSDOM(``, {
    url: "https://example.org/",  // window.location，document.URL
    referrer: "https://example.com/",  // document.referrer
    contentType: "text/html",  // document.contentType
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42",  // UA
    includeNodeLocations: true  // 保留由HTML解析器生成的位置信息，允许使用nodeLocation()方法
});

const jsdom = require("jsdom");  // 引入 jsdom
const { JSDOM } = jsdom;  // 引出 JSDOM 类， 等同于 JSDOM = jsdom.JSDOM

const dom = new JSDOM(
    `<body>
              <script>
              document.body.appendChild(document.createElement("hr"));
              console.log("hello world");
              </script>
           </body>`, 
    { runScripts: "dangerously" }  // 需要配置runScripts 否则不运行 JS
    );

const cookieJar = new jsdom.CookieJar(store, options);
const dom = new JSDOM(``, { cookieJar });