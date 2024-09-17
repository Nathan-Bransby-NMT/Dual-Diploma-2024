# Assessment Task 01

## Answer these questions in a Word Document regarding HTTP and Database Structure

1.**We know that HTTP drives the web however we often do not know what the protocol does. Describe HTTP in your own words.**

**- Please include any updates,**

***- Technical specifications such as protocols***

***- Any images that will explain more.***

- **HTTP/0.9** - `1998 - 1991`

> The HyperText Transfer Protocol (HTTP), was originally developed in 1989 as part of the 'World Wide Web' project as way for Nuclear Scientist within Europe belonging to the research organisation 'CERN' to share documents and data over the Internet. The very first version (`HTTP/0.9`) was released in 1991 which only contained the `GET` method that allowed users to retrieve HTML pages.

- **HTTP/1.0** - `1996`

> Between 1991 - 1995, the protocol was operated with a try-and-see approach. Interoperability issues were quite common, so as an effort to address and solve these issues, an informational document known as [RFC 1945](https://datatracker.ietf.org/doc/html/rfc1945) was produced, that described the first set of common rules and practices when publishing and transmitting via HTTP. This lead to the development of HTTP/1.0 which introduced the standardisation of response codes, introduced headers and brought more methods such as `POST` & `HEAD`. This gave users the ability communicate between clients with ease for the first time ensuring that information was resolved at each end.

- **HTTP/1.1** - `1997`

> Once HTTP started implementing a standardised process for all clients and host, there was need to clarify ambiguities, this lead to the development of HTTP/1.1, also known as the standardised HTTP. HTTP/1.1 would be officially released in 1997 as [RFC 2068](https://datatracker.ietf.org/doc/html/rfc2068). This contained several improvements with the protocol, which included:
>
> - The ability to reuse a connection, which meant that it no longer needed to open multimedia multiple times to display resources and embeddings.
> - The introduction of Pipelining was brought to the protocol, allowing a second request to be sent before resolving the response.
> - Network support for chunked responses.
> - Additional cache control system.
> - Content negotiation, including encoding and type, giving client & server a way to resolve content that otherwise would have conflicted when exchanged.
> - The introduction of the `HOST` header, which allowed servers to host multiple domains on the one IP address.
>

- **HTTPS (SSL & TLS)** `1994`

>Although HTTP/1.1 was the standardised protocol, there were growing concerns around how secure data was whilst being transmitted. This lead to the public adoption of the HyperText Transfer Protocol Secure (HTTPS) which combined Transfer SSL 2.0 (Secure Socket Layer) Layer Security (TLS) to encrypt data transferred between client and server. SSL 1.0 was never released to the public, However SSL 2.0 & SSL 3.0 were both eventually adopted. Although this change in protocol became essential for protecting sensitive information being passed via the Internet, it wouldn't become widely adopted until the late 2000's to mid 2010's.

- **REST APIs** `2000`

> In 2000, the pattern for Representational State Transfer (REST) was designed. This allowed any web application to let an API retrieve and modify its data without having to update the browser or servers. All information needed was embedded in the files that the website served through the standard HTTP/1.1. The drawback was that each site defined its own unique nonstandard RESTful API and had total control over it.RESTful APIs became common throughout the 2010s.
>
> Other forms of API that became available to webpages that created extensions of the HTTP protocol (specific uses) include:
>
> - Server-sent Events
> - WebSocket, this new protocol can be set up by upgrading an existing HTTP connection.

- **HTTP/2** `2015`

> With the increasing complexity in web pages along with the overhead in HTTP/1.1 connections, which contained issues such as having duplicate data transmitted and lack of responsiveness. Due to this, Google had developed an experimental protocol SPDY in the mid 2010s, which was an alternative way of exchanging dat between client and server. In doing so they were able to increase responsiveness whilst solving the problem of duplicate data being transmitted, this would go on to become the foundation of the HTTP/2 protocol.
>
> Officially standardized in May 2015, HTTP/2 use peaked in January 2022 at 46.9%.
>The HTTP/2 protocol differs from HTTP/1.1 by introducing the following:
>
> - Handling itself as a binary protocol rather than text, which means that it can't be read and created manually. Further more this allows for the implementation of improved optimisation techniques.
> - Being a multiplexed protocol, which means that parallel requests can be made over the same connection, which was impacting HTTP/1.1s performance.
> - It compresses headers, in a  way to remove the duplication & overhead of data being transmitted.
> - It also allows a server to populate data in a client cache using the a mechanism called the server push.

Over time the adoption of HTTP/2 has gradually increased.

- **HTTP/3.0** `2022`
The latest update of HTTP, HTTP/3 was developed in 2022 and contains the same semantics as earlier versions, however this version uses QUIC instead of TCP. This upgrade is designed to provide quicker setup and lower latency for HTTP connections through using TCP handshakes combined with a TLS handshake rather than as a second handshake, allowing instant transmissions. Similarly to HTTP/2 it is a multiplexed protocol, however QUIC implements packet loss detection and retransmission independently for each stream, so that if an error occurs, only the stream with data in that packet is blocked. 

***References***

- MDN Web Docs. (n.d.). *Evolution of HTTP*. MDN Web Docs. Retrieved from [https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP)

- MDN Web Docs. (n.d.). *REST - MDN Web Docs Glossary: Definitions of Web-Related Terms*. Retrieved from [https://developer.mozilla.org/en-US/docs/Glossary/REST](https://developer.mozilla.org/en-US/docs/Glossary/REST)

- MDN Web Docs. (n.d.). *Server-sent events - Web APIs*. Retrieved from [https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

- Mozilla. (2019, November 28). *The WebSocket API (WebSockets)*. MDN Web Docs. Retrieved from [https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

- W3Techs. (n.d.). *Usage statistics of HTTP/2 for websites, February 2021*. Retrieved from [https://w3techs.com/technologies/details/ce-http2](https://w3techs.com/technologies/details/ce-http2)

- MDN Web Docs. (n.d.). *QUIC - Glossary*. Retrieved from [https://developer.mozilla.org/en-US/docs/Glossary/QUIC](https://developer.mozilla.org/en-US/docs/Glossary/QUIC)

- IETF. (n.d.). *RFC 9114: HTTP/3*. Retrieved from [https://datatracker.ietf.org/doc/html/rfc9114](https://datatracker.ietf.org/doc/html/rfc9114)

---

2.**What are the limitations of HTTP when it comes to developing web applications?**

***- Are there any?***

The limitations of HTTP when developing web application include:

> - Statelessness: Each request is independent, making session management challenging.
> - Performance Issues: Latency, overhead from headers, and limited asynchronous connections can slow down applications.
> - Security: Data is transmitted in plain text, making it vulnerable without HTTPS; session management can be complex.
> - Bandwidth Consumption: HTTP headers add overhead, especially with many requests.
> - Caching Issues: Poor caching strategies can lead to outdated content or unnecessary server load.

***- What is a web application?***

A web application is software that runs in a browser, that allows you to utilise benefits such as security and complexity that you would with normal software, but without the need to download or install any application. 

***- Are there any new advances for web Applications?***

Although Progressive Web Applications (PWA) are not a new thing, through the latest advancements in many web browsers the gap between native applications and PWAs has never been so small. Features that were once only available through device specific languages are now available through standard web technology such as: 

- The ability to handle files.
- Access device hardware (i.e., Bluetooth, USB, etc.)
- Sync Data and fetch resources in the background (Drastically improving performance when rendering pages.)

and many more.

...

***References:***

- Amazon Web Services. (n.d.). *What is a Web Application?*. Retrieved from [https://aws.amazon.com/what-is/web-application/](https://aws.amazon.com/what-is/web-application/)

- Microsoft. (n.d.). *Progressive Web Apps (Chromium) Overview*. Retrieved from [https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/)

---

3.**Please identify the advantages in using HTTP when developing web applications.**

***- How is HTTP used in web applications?***

Like regular web pages, web applications use HTTP for :

- **Client Requests** when a user interacts with the application (i.e., GET, POST, PUT, DELETE).
- **Server Response** after processing a request that contains;
  - A Status code: (i.e., `200 OK`, `404 Not Found`, etc.)
  - Headers  to provide metadata about  response
  - A Body: (HTML, JSON, etc...)
- **RESTful APIs** which use HTTP methods to provide access to the application's backend data / resources
- **Encryption** through the HTTPS (HTTP Secure) protocol to utilise application security
- **Session Content** to maintain user session content (i.e., cookies / tokens) due to the statelessness of HTTP.

This is just some of the ways that web-apps use HTTP.

***- What is the Advantage?***

Web Application Servers, hold the ability to multithread simultaneously, which helps deliver web content faster than traditional web servers. Web Application Servers support many different protocols, this is including HTTP which eliminates the need to host both a web server as well as an application server. The key differences between the two are seen in the table below.

| **Task**  | **Web server** | **Application server** |
|-----------|----------------|------------------------|
| **Tasks covered** | Web servers deliver responses to simple requests. | An application server delivers more complex content from databases, services, and enterprise systems. |
| **Protocols used** | Web servers primarily use HTTP. They also support FTP and SMTP. | Application servers support many protocols. |
| **Content types** | Web servers deliver static content, like HTML pages, images, videos, and files. | Application servers deliver dynamic content, like real-time updates, personalized information, and customer support. |
| **Multithreading** | Does not typically use multithreading. | Uses multithreading to process requests concurrently. |

***- What is the Future of Web Applications?***

...

***References:***

- MDN Web Docs. (n.d.). *HTTP overview*. MDN Web Docs. Retrieved from [https://developer.mozilla.org/en-US/docs/Web/HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)

- Amazon Web Services. (n.d.). *The difference between a web server and an application server*. Retrieved from [https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/](https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/)

---

4.**Describe a database structure and how HTTP works with a database.**

- outline internet technology as it relates to the use of databases

- identify and apply programming control structures, including object-oriented programming
and structured query language (SQL)

- explain web programming concepts, including:
  
  - authentication and web security

  - hypertext transfer protocol (HTTP)
  
  - session management
  
  - defining the principles of stateless programming.

---

5.**Describe the processes and techniques related to object-oriented programming.**

- What is Object Oriented programming and what language are you using?

We are writing in JavaScript. OOP is a programming method where rather than writing sequentially down a script (in step by step order), you write a "blueprint" that describe how an objects is built. Objects contain their own attributes and functions (known as methods). OOP contains 4 pillars that describe the different object behaviors, which are:

> - ***Inheritance:*** When an object class derives from another object class, this inherits all of the parent classes attributes and methods.  
> - ***Encapsulation:*** This is when one class is contained within another, allowing public methods and attributes from an object to be referenced from within another class.
> - ***Polymorphism:*** This is when a method utilises overloading methods, which is when a class method defined multiple times to contain different parameters and producing different results.
> - ***Abstraction:*** This is when an abstracted class is used to define a set of shared attributes and methods between classes. Generally programming languages that include abstraction, will require all defined abstract parent attributes methods to be implemented by the child class that is abstracting from the parent.

- **describe the process for developing small-size applications**

- identify and outline the key features of a graphical user interface (GUI), for interaction with
an operator.

6. **Include APA references for all your answers, even if you know the answer. Your answers will need to be backed up by reference information of another source.**

_YES_
