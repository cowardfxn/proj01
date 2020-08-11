# gRPC

[官方文档](https://grpc.io/docs/what-is-grpc/core-concepts/)

官方文档对gRPC的定义是高效的RPC(Remote Procedure Call, 远程进程调用)框架。

gRPC使用**Protocol Buffer**(一种由谷歌发布的数据序列化/反序列化格式协议)作为IDL(Interface Definition Language)来定义接口方法和数据。

定义gRPC接口方法的文件一遍以`.proto`为后缀。`.proto`文件声明了接口方法的参数类型和返回类型，在调用gRPC接口方法时，同样使用`.proto`文件存放接口参数数据。

gRPC客户端与服务端之间通信时，使用的数据格式都是**protocol buffer**，不同语言的gRPC驱动都需要从**protocol buffer**读取数据或者将数据转换成**protocol buffer**格式。

可以通过安装*protoc*编译器，编译`.proto`文件，生成C++、Java、Python或其他语言的gRPC客户端/服务端代码。

目前默认使用*proto2*版本的gRPC协议，最新的是*proto3*版本。

根据实现方法或者调用方式的不同，gRPC接口可以是异步的也可以是同步的

## gRPC接口方法的四种类型
根据功能的不同，gRPC接口可以分为四大类。

 - *Unary RPCs* 一元RPC，基础的接收-发送数据形式
 - *Server streaming RPCs* 服务端流式RPC，服务端返回数据流
 - *Client streaming RPCs* 客户端流式RPC，客户端向服务端发送数据流
 - *Bidirectional streaming RPCs* 双向流式RPC，服务端与客户端通过互相独立的数据流发送数据，两个数据流内数据按被发送的顺序存在

实装上，四种类型的主要区别在于方法定义是的参数类型和返回值类型的不同

 - *Unary RPCs*  
  `rpc sayHello(HelloRequest) returns (HelloResponse);`
 - *Server streaming RPCs*  
  `rpc lotsofReplies(HelloRequest) returns (stream HelloResponse);`
 - *Client streaming RPCs*
  `rpc lotsOfGreetings(stream HelloRequest) returns (HelloResponse);`
 - *Bidirectional streaming RPCs*
  `rpc bidiHello(stream HelloRequest) returns (stream HelloResponse);`

gRPC允许客户端请求指定过期时间

### 四种类型的方法的生命周期
#### *Unary RPCs*

 1. 客户端调用gRPC方法时，会向服务端发送客户端的[元数据](https://grpc.io/docs/what-is-grpc/core-concepts/#metadata)和方法名，如果客户端支持设置请求过期时间，也可以传递请求超时设置（可以是有效时长或某个过期时间点，依所用语言而定）
 2. 服务端收到客户端发送的初始数据后，可以向客户端发送连接初始化的元数据，或者等待客户端的请求消息到达。按照设定，服务端发送给客户端的第一批数据必须是连接初始化的元数据。
 3. 一旦服务端收到客户端发来的请求数据，就会开始请求方法对应的处理，并生成返回对象(response)，如果业务处理正常结束，服务端会将返回对象、状态码、状态消息(可选)和请求返回用的元数据(可选)发送给客户端
 4. 如果返回消息状态是"OK"，客户端会接收到返回数据，RPC方法调用结束

#### *Server streaming RPCs*
Server streaming RPC与unary RPC类似，不同之处是服务端返回数据流。向客户端发送了所有数据之后，服务端会像unary RPC那样返回状态码、状态消息(可选)和请求返回用的元数据(可选)，并结束服务端的方法调用。

客户端会在接收到最后返回的状态码等数据后结束方法调用。


#### *Client streaming RPCs*
Client streaming RPC也与unary RPC类似，区别是客户端会发送消息流。一般情况下，服务端会在接收到所有消息后返回状态码、状态消息(可选)和请求返回用的元数据(可选)，但并非必需如此，例如，服务端可能在接收到某个特定的字符后，返回状态码，停止接收后续消息。

#### *Bidirectional streaming RPCs*
对于Bidirectional streaming RPC，第一步是客户端执行方法请求，向服务端发送客户端元数据、方法名和过期时间，服务端可以选择是返回连接初始化元数据，还是等待客户端发来的数据。

依据实现方式的不同，客户端和服务端所使用的数据流可能有细微的差别。  
两个相互独立的数据流支持客户端与服务端以多种多样的方式发送数据，例如，服务端可以等到客户端已经发送所有的数据再返回数据；或者是“乒乓模式”，服务端接收一个请求，返回一个消息，客户端收到一个返回消息，就发送一个请求，如此往复。

## Cancelling an RPC
无论任何时候，客户端与服务端都可以取消一个RPC请求。被取消的RPC请求会立即中止，但是在服务端或客户端已经执行的操作不会会退。

## 进阶知识点
 - authentication in metadata  如何在gRPC中实现请求认证
 - channels type definition, querying  gRPC中的channel
 - context management  gRPC中请求上下文管理

