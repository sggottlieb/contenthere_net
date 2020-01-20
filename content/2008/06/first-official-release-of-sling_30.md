Title: First Official Release of Sling
Date: 2008-06-30T08:48:00.001Z
Modified: 2015-01-06T12:15:38.975Z
Category: misc
Tags: 
Slug: 2008/06/first-official-release-of-sling_30
Authors: Seth Gottlieb

The [Apache Sling](http://incubator.apache.org/sling/site/index.html) team recently [announced the first official release of Sling](http://www.theserverside.com/news/thread.tss?thread_id=49864).  Now you can [download](http://incubator.apache.org/sling/site/downloads.cgi) some nicely packaged Sling bundles to play around with.  
  
I have been experimenting with the Sling/[CRX](http://www.day.com/content/site/en/index/solutions/content-centric_infrastructure/content_repository.html) bundle that came with Day Software's [JCR Cup 2008](http://dev.day.com/microsling/content/blogs/cup.c.html) competition (entries due midnight September, 30) and was really impressed by what I saw.       
  
Sling allows you to write applications on top of the JCR using either server side or client side Javascript.  On the server side, you can create [Java Script Templates (ESP files)](http://weblogs.goshaky.com/weblogs/lars/entry/esp_javascript_template_language_syntax) that give you access to the full JCR API. Templates are stored in the repository and called using an elegant [MVC request processing framework](http://dev.day.com/microsling/content/blogs/main/slingrequestprocessrevisited.html). Templates can be called directly, or can be associated with content types and executed when an asset of that time is requested.  As you might expect from [Roy Fielding](http://www.ics.uci.edu/~fielding/)'s [employer](http://www.day.com), it is all very [REST](http://www.infoq.com/rest/).  For client-side scripting, you just import a Javascript file called sling.js and you get methods like "Sling.getContent" (which gives you an array of Javascript objects).    
  
Despite the fact that Sling is still an incubation project, it is fairly mature and robust.  Day's upcoming release of [Communiqué](http://www.day.com/site/en/index/solutions/content_management.html.html) (version 5) uses Sling extensively.  I envision Sling being used in a presentation tier where pages are statically rendered (baked) from content in the JCR and Sling is used to power dynamic AJAX overlays using content from replicated JCR workspaces.    
  
I really like the fact that logic is written in an interpreted language like Javascript.  Development and deployment is faster when you take out the compilation step.  Furthermore, Sling is built as [OSGi](http://www.osgi.org/About/Technology) (using [Apache Felix](http://felix.apache.org/site/index.html))  bundles so it is more modular and flexible than a typical monolithic Java web application.    
  
The CRX (or the free [Apache JackRabbit](http://jackrabbit.apache.org/) implementation of the JCR) and Sling should be considered along side [Alfresco](http://www.alfresco.com/) with its elegant [Web Scripts](http://wiki.alfresco.com/wiki/Web_Scripts) (which also uses Javascript as a scripting language).  Alfresco has some nice virtualization features but there may be a higher level of lock-in to the Alfresco API's.    Alfresco has a user-oriented user interface while the CRX only has a JCR browser which is really only intended for administrators.  However, in both cases, you will probably want to develop your own user interfaces because Alfresco's current WCM UI is [not optimized for managing web content](http://blog.contenthere.net/2008/04/alfresco-releases-enterprise-edition-22.html) ([improvements are scheduled for mid 2009](http://blog.contenthere.net/2008/03/new-web-user-interface-coming-for.html) - interestingly, the Alfresco team is calling these enhancements "project _Sling_shot).    
  
  
