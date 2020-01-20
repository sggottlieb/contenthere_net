Title: Give Your Repository a REST
Date: 2008-07-22T09:58:00.001Z
Modified: 2015-01-06T12:15:39.149Z
Category: misc
Tags: 
Slug: 2008/07/give-your-repository-rest_22
Authors: Seth Gottlieb

Through my research and my client work I have been running across this recurring pattern of exposing a content repository through a [REST](http://www.infoq.com/rest/) interface.  In the past, I have written about the JCR and [Sling](http://incubator.apache.org/sling/site/index.html) and [Alfresco](http://www.alfresco.com)'s Web Scripts architecture.  I really like both of those implementations.  More recently, I have been working with a client who has built their own REST interface on top of [Day's CRX](http://www.day.com/site/en/index/solutions/content_management.html.html).  They started their project before Sling was a glimmer in Apache's eye and they took a slightly different approach.  Instead of using Sling's [repository-oriented request handling](http://dev.day.com/microsling/content/blogs/main/slingrequestprocessrevisited.html), or Alfresco's model of registering a Web Script (written in Javascript) to a particular path, my client has built out a full URL based query syntax through a servlet.  Right now, the syntax focuses on searching retrieving content and is very powerful.    
  
The strategy of using a REST API for your repository solves a central problem with the JCR and other Java base repositories: remote connectivity.  Without a remote connectivity infrastructure like JDBC or ODBC, technologies wishing to talk to a Java repository must resort to connectivity like RMI (Remote Method Invocation) that are inefficient and do not necessarily play nicely with firewalls.  While not particularly efficient (lots of protocol layers and text processing), REST offers a nice foundation for enabling remote connectivity at the appropriate layer of abstraction (that is, how content is _logically stored_ - not how it is physically persisted).  There are many reasons why REST is a good strategy but I think that the most important ones are:  

1.   There is great infrastructure available for optimizing and controlling HTTP traffic. For example, reverse proxy technologies like [Squid](http://www.squid-cache.org) can stand in front of the REST interface and serve repeated requests out of cache. Firewalls can be used to filter traffic with rules that evaluate the requested path and requester origin (beware [IP Address spoofing](http://en.wikipedia.org/wiki/IP_address_spoofing)).   
    
2.   REST is entirely technology neutral. Everything talks HTTP and XML. You can replace the implementation of either the server or the client with little risk to the overall architecture.   
    

  
I think the only downside is that developing your own API is tricky business.  While you are free to change your underlying data structures, once you publish your API and start writing applications on it, you lock yourself in.  Where possible, it is best to support standardized query syntax like [XQuery](http://www.w3.org/TR/xquery) or the JCR query language in addition to your domain-specific methods.      
  
I expect to see this pattern of REST-based repository access to be pretty much the standard as we get into Web 2.0 architectures that support mash-up applications.  If they can address the overhead of all the text handling, more and more systems will use REST API's to de-couple the various components in the application stack.  Something to consider the next time you design a content-centric application.
