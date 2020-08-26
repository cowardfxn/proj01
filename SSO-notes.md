# SSO
Single sign-on

Only authentication, authorization in application is another story

当用户试图访问网站资源时
1. 网站检查当前用户是否已有SSO认证，如果有，则允许用户访问资源
2. 如果用户没有SSO认证，则向用户发送包含SSO登陆服务的登陆接口
3. 用户输入用户名/密码，点击登录按钮
4. SSO登陆服务向认证提供商或网站使用的内部认证服务发送请求，验证用户输入
5. 用户通过SSO登陆服务认证，转回登陆网站
6. 登陆后，网站向用户发送认证数据，以便用户在打开新页面时认证

SSO不包含服务内的权限认证
