# RPC Style vs. REST Web APIs


[原文链接](https://blog.jscrambler.com/rpc-style-vs-rest-web-apis/)

## 简介
基于HTTP协议的服务形式多种多样，你所使用的服务类型应该视需要解决的问题而定。对此，最常见的错误就是本应使用*RPC（Remote-Procedure-Call）*的服务却用了*RESTful*实现。

网络服务开发上经常会有这样的混用。RPC是一种创建网络接口的规范，REST则是另一种规范，它们各有不同的实现方式。两者通过HTTP协议进行通信，因此经常有人误解，认为所遇到的网络服务接口都是REST类型的。

这里，我们讲深入探讨RPC和REST规范在实现网络接口时的区别。希望可以在你下次实现网络服务接口时有所帮助。

但是请注意，这二者之间并没有绝对正确的选项，每个规范的目的不同，也有各自的支持和反对意见。

## 为什么使用者应该注意？
和其他的编程问题一样，最适合自己的需求的才是最佳方案。理解RPC和REST规范的优缺点可以帮你决定什么才是最合适的。

如果你的目的是只允许一小部分接口访问数据，RPC接口会很合适，它可以有效降低网络带宽的消耗，而且简化服务代码。你可以任意添加需要的限制，甚至在网络服务中无视其他代码，只实现你需要的接口。

REST接口会将收到的请求视为对服务器资源的调用。域名决定了要访问的资源位置，至于代码是何功能，域名本身并不关心，它只是告诉程序如何找到请求需要的资源在哪。REST接口的优点在于可以接收来自多个用户的请求。REST接口只关心域名指向的资源是否可用。

那么，RPC形式的接口和REST形式的接口都是什么样子呢？

我们用*Node*来实现两种接口，首先，引用`http`库：

```
const http = require("http");
```

假设有一群猫科动物，我们想查询其中的一只雪豹。以此为例，我们来看看两种规范的不同之处。

以下是猫科动物列表：

```
const CAT_ID = 1;

const ELUSIVE_CAT = [
 { id: CAT_ID, name: 'Snow Leopard', conversationStatus: 'Vulnerable' }
];
```

## RPC类型的接口
假定RPC接口的用户只关心如何通过id查询动物名字，我们希望请求返回包含*name*熟悉的**JSON**对象。

代码实例:

```
const rpcApp = http.createServer((req, res) => {
    if (req.url === '/getElusiveCatNameById?id=' + CAT_ID) {
        const cat = ELUSIVE_CAT.find(c => c.id == CAT_ID);

        res.setHeader('Content-Type', 'application/json; charset=utf-8');

        res.end(`{ "name": "${cat.name}" }`)
    }
});
```

这个服务注册了一个匹配`/getElusiveCatNameById`地址，并附带名为`id`的参数的URL。RPC规范最为人所知的就是将函数名写在URL里。这样用户可以很方便的通过URL就知道接口的作用和会返回的结果。示例种的服务不关心这个接口之外的数据，因此显得很简单。

要启动服务，还需要监听某个端口。

```
rpcApp.listen(1337);
```

调用这个RPC接口会得到以下结果：

```
➜ curl http://localhost:1337/getElusiveCatNameById\?id\=1
{ "name": "Snow Leopard" } 
```

## REST类型的接口
对于REST类型的接口，我们需要将它视作服务器资源。想象一下荒野中有一片聚集了猫科动物的区域，你要在这个区域中寻找一只雪豹。

示例代码：

```
const restApp = http.createServer((req, res) => {
    if (req.method === 'GET' && req.url === '/elusive/cat/' + CAT_ID) {
        const cat = ELUSIVE_CAT.find(c => c.id == CAT_ID);

        res.setHeader('Content-Type', 'application/json; charset=utf-8');

        res.end(`{ "id": "${cat.id}", "name": "${cat.name}", "conversationStatus": "${cat.conversationStatus}" }`);
    }
});
```

这个服务注册的URL是`/elusive/cat/1`。HTTP请求的方法对于REST接口有特殊的意义。`GET`类型的请求告诉服务我们想找的是`cat`区域下的所有属性的数据，这也是为什么这个接口会返回所有数据。这样，用户通过这个接口所能获得的数据就被限制在当前区域内。这个服务可以接受多个想要查询猫科动物信息的用户请求。

调用这个REST接口会得到以下结果：

```
➜ curl http://localhost:1337/elusive/cat/1
{ "id": "1", "name": "Snow Leopard", "conversationStatus": "Vulnerable" }
```

## 结论
当服务功能简单时，RPC类型的接口非常合适。如果只有一两个用户，这样的网络服务足以胜任。鉴于RPC接口功能单一，可以在网络服务内直接实现业务代码。

对于REST接口，你应该将它视为按区域提供数据的服务。它的优点是可以直接通过URL地址拆分数据。当有很多用户请求数据时，这种方式很有用。REST规范会将数据与代码或业务逻辑解耦。

实际项目中，使用哪种类型的接口需要视情况而定。REST接口可能适用于一个大型的分布式系统，却不适用于只有一项功能的服务。RPC适用于只有基本的CRUD功能的，几乎不需要考虑可扩展性的MVC系统。

了解二者的区别，你就可以选择使用何种类型的方案实现接口。如何选择并没有标准答案，重要的是知道哪种规范可以解决你面临的问题。


## 结论2
 - `RPC API`与`REST API`的区别在于API设计规范不同，`REST`要求在服务器端保留用户的访问记录（请求缓存），而`RPC`则没有服务器端缓存的要求
 - `RPC API`限定了API以方法名限定了请求所能访问的代码范围，`REST API`的API与方法的实现代码之间没有强关联，也无从限制API所能访问到的代码范围
 - 根据`REST API`的设计规范，不同的HTTP方法(`GET`, `POST`, `PUT`, `DELETE`, `PATCH`)有不同的适用范围，而`RPC API`则主要使用`GET`和`POST`方法
 - 更直观一点，`REST API`要求设计者把部分数据或结构信息放在URL路径里(例如 `/domain/context/<:contextId>/`)，而`RPC API`则没有这方面的要求
