# CORS in server side

[Ref on STO](https://stackoverflow.com/questions/36250615/cors-with-postman/36486188#36486188)

浏览器与Postman/curl这样的开发工具处理跨域请求设置时的操作不同，Postman/curl不会触发跨域请求限制。

## 浏览器 vs. Postman

 - 浏览器: 在向服务器发送API请求之前，发送`OPTIONS`请求检查服务器类型，取得请求`headers`。无论浏览器页面是否设置了`Access-Control-Allow-Origin`。以此推论，请求头里的`Access-Control-Allow-Origin`只是限定哪些跨域请求的origin可以允许通过，虽然浏览器默认只允许相同域名的请求。
 - Postman: 不检查服务类型或者通过`OPTIONS`请求取得请求头里的`Access-Control-Allow-Origin`，直接发送各种`GET`, `POST`, `PUT`和`DELETE`请求。

## 服务端CORS配置
由Postman之类的开发工具所发送的HTTP请求，在请求头钟可能不包含`origin`，在配置服务端的CORS设置时，除了跨域请求域名白名单配置，还要考虑`origin`不存在的情况，以兼容开发者工具或者graphql客户端调用类的请求。
