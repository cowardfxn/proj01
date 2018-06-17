# Notes


[article link](https://blog.sessionstack.com/how-javascript-works-inside-the-networking-layer-how-to-optimize-its-performance-and-security-f71b7414d34c)


All major browser limit the maximum socket pool size to 6 sockets.

#### What's happening when you open a website in browser?
1. The user types a URL into address bar
2. Given the URL of a resource on the web, the browser starts by checking its local and application caches, try to use a local copy to fulfill the request
3. If the cache can not be used, the browser gets the domain name from the URL and querys IP address of the server from a DNS. But if the domain name is cached, no query to DNS.
4. The browser creates a HTTP packet saying it request a web page located on the remote server. (handshaking starts)
5. The packet is passed to the TCP layer which adds its own information on top of HTTP packet. This information is required to maintain the started session
6. The packets is then handled to the IP layer whose main job is to figure out a way to send the packet from the user to a remote server. This information is also stored on top of the packet (HTTP is fulfilled on the basis of TCP/IP).
7. The packet is sent to the remote server. (finally)
8. Once the packet is recevied, the response gets sent back in similar manner (setp 1 to 7 on the remote server).

#### Steps of Transport Layer Security(TLS) handshake
1. The client sends a "client hello" message to the server, along with the client's random value and supported cipher suites.
2. The server responds with a "server hello" message to the client, along with the server's random value.
3. The server sends its certificate for authentication to the client and may request a similar certificate from the client. The server sends "server hello done" message.
4. If ther server has requested a certificate from the client, the client sends it.
5. The client creates a random Pre-Master Secret and encrypt it with the public key from the server's certificate, sending the Pre-Master Secret to the server.
6. The server receives Pre-Master Secret. The server and client each generates the Master Secrete and session keys based on the Pre-Master Secret (a new pair of secret is generated).
7. The client sends a "change cipher spec" notification to indicate that the client will start using new session keys for hashing and encrypting messages. The client also sends a "client finished" message. (update secret usage on server)
8. The server receives the "change cipher spec" and switches its record layer security state to symmetric encryption using the session keys. The server sends a "server finished" message to the cilent. (server side cipher updated)
9. Client and server can now exchange data through the channel they have established. All messages sent from the client to the server and back are encrypted using the session key (symmetric encryption on both side?).

maximum socket poll size
