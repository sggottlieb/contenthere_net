Title: Whatever happened to the URL?
Date: 2006-08-21T14:04:00.002Z
Modified: 2015-01-06T11:32:19.149Z
Category: misc
Tags: 
Slug: 2006/08/whatever-happened-to-url_6
Authors: Seth Gottlieb

Even back when I was developing websites in 1998, it was considered really amateur to use frames.   One of the primary arguments against using frames is that they mess up book marking (that, and they cause the back button to behave inconsistently).  The browser does not know which frame within the frameset you are interested in.  When you reload the page, the frameset reloads to its default state.  The only way to get back is to re-enact the sequence of actions that took you to that view.   
  
The single most important thing about the web is the URL.  The URL is a resource's identity on the web.  It is the magic behind links.   It is your only way to get back to where you were.  Without URL's the interconnected web melts into a de-referenced puddle.  
  
So why are there so many new web technologies disrespecting URL based navigation?   AJAX is actually not so bad as long as you use it for targeted functionality and give the user an alternative link based navigation.  But [JSF](http://java.sun.com/javaee/javaserverfaces/) and [Flash](http://www.adobe.com/products/flash/flashpro/) based web applications really annoy me.  Applications built on these technologies seem to have abandoned the concept of the web and are just using a browser as a runtime environment.  That may be OK if you think of the web as just an efficient software deployment tool but it is <span style="font-style: italic;">not</span> OK if you want your application to behave as a node in an interconnected network.   With content, especially web content but also documents, it is <span style="font-style: italic;">absolutely essential </span>that each asset is referenceable.  Referenceable content allows for very easy integration across systems.  For example, you can link to an item in your Digital Records Management system from within your Customer Relationship Management system so a user is able to see an invoice that a customer complained about.  This is the ultimate in loosely coupled architectures.  With WYSIWYG editor, a very non-technical business user is able to create all sorts of aggregated views of content.   Why even bother with a web services API if you can't even do this?  
  
So if you are like me and you believe that the Internet, [Web 2.0](http://www.oreillynet.com/pub/a/oreilly/tim/news/2005/09/30/what-is-web-20.html), and the [Semantic Web](http://www.w3.org/2001/sw/) is all about making connections with content, stay away from technologies and uses of technologies that undermine the linkages.
