Title: Nuxeo Web Engine
Date: 2008-07-11T08:31:00.001Z
Modified: 2015-01-06T12:15:39.121Z
Category: misc
Tags: 
Slug: 2008/07/nuxeo-web-engine_11
Authors: Seth Gottlieb

[Nuxeo](http://www.nuxeo.com/) just [announced the first official release of their WebEngine](http://blogs.nuxeo.com/sections/blogs/fermigier/2008_07_11_first-release-nuxeo-webengine).  I have been hearing updates about this project for a while and have been meaning to check it out.  From glancing through the slides, WebEngine seems very similar to [Apache Sling](http://incubator.apache.org/sling/site/index.html) and has many of the things that I like about Sling: a RESTful interface and a lightweight, content-centric programming model. In WebEngine templates are written in FreeMarker and you can script in your choice of Groovy, Python, Ruby, Javascript and other languages (thanks to [JSR 223](http://java.sun.com/developer/technicalArticles/J2SE/Desktop/scripting/)) which provides a scripting interface for Java applications).  I am looking forward to playing around with WebEngine.  In my past experiences with Nuxeo applications, I found them to be well engineered.  
  
If you are new to Nuxeo, they have a legitimate claim to being the first open source ECM company.   Their primary geographic focus is in France and they are less well known in the US.  Nuxeo's original ECM product (which combined Document Management, Collaboration, and Web Content Management) was written on the Zope platform.  In 2006, they ported their product (then called CPS for Collaborative Portal Server) to a Java stack ([using JBoss Seam](http://www.slideshare.net/sfermigier/nuxeo-ep-5-a-seam-case-study/)).  Long time readers of this blog may remember [me being skeptical of whether they could pull it off](http://blog.contenthere.net/2006/09/nuxeo-cps-switching-to-java.html).  It turns out that they did a great job with the migration and have been aggressively pushing the platform forward.   
  
Like, [Alfresco](http://www.alfresco.com), Nuxeo's experience and customer base leans towards the document management side of ECM.  Web content management is a newer focus that is (I think) well timed as more companies are looking for ways to rapidly build internally and externally facing content centric web applications.
