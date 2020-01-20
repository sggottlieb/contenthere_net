Title: Book Review: OpenCms 7 Development
Date: 2008-06-19T14:17:00.001Z
Modified: 2015-01-06T12:15:38.765Z
Category: misc
Tags: 
Slug: 2008/06/book-review-opencms-7-development_19
Authors: Seth Gottlieb

I just got through reading Dan Liliedahl's book [OpenCms 7 Development](http://www.packtpub.com/opencms-7-development/book) ([Packt Publishing](http://www.packtpub.com/)).  I met Dan when I was at the [OpenCms Days](http://www.opencms-days.org/en/index.html) developer conference and was impressed with his presentation.  Dan knows his stuff (not just about [OpenCms](http://www.opencms.org) - he worked for FutureTense in the early days).    
  
The book was first introduced at the conference.  I was surprised that Dan was able to get it out so quickly after Version 7 was released.  It seemed like Version 6 was out a long time before a book on it came out.  Dan did mention that writing about the product as it was being developed was a challenge.    
  
When I started reading the book, I was pleasantly surprised to not have to go through any content management theory.  The book stays true to its title.  Not that theory isn't important but I think it is reasonable to assume that someone developing on a CMS knows the about the basic concepts.  If you don't, some background reading (and also some requirements analysis too) is in order.  
  
One short-coming about diving right into the OpenCms architecture is that the beginning is a little choppy as the author tries to orient the reader to the platform (OpenCms is a very mature and elaborate application).  Although it is choppy, there are some very good explanations of things like OpenCms's request processing chain and how the code is organized.  There are also excellent tips on configuration management and how to configure your IDE.  Still a reader may want to supplement the book by reading some additional OpenCms doc to help introduce him to some of the bigger OpenCms concepts.   
  
The book hits its stride as it gets into the examples, which revolve around building a blogging site.  There is good coverage on everything from creating content types and display templates to building extensions.  By over-engineering some of the design, Dan is able to go into depth in modularizing code and managing logic in Java classes.   Dan's experience in building big sites shows in how he designs for manageability and reuse.  All the code is put into modules that can be exported and deployed to different OpenCms instances.  The book also covers some of the new features like WebDAV, the new security model (with organizational units) and the relationship engine.    
  
The one area that I think could use a little more coverage is on the TemplateOne and TemplateTwo frameworks.  Dan builds everything from scratch to show how OpenCms works but these frameworks allow you to get up an running with less development.  Unfortunately, neither of these are particularly well covered in the OpenCms documentation.  Perhaps a whole book on TemplateOne and TemplateTwo is in order.  
  
Overall, OpenCms 7 Development is a must read for anyone who wants to implement robust sites on the OpenCms platform.  
  
OpenCms is covered in the[ Open Source Web Content Management in Java report](http://www.contenthere.net/products-page/reports/open-source-content-management-in-java).  The [standalone evaluation of OpenCms is also available](http://www.contenthere.net/products-page/reports/open-source-web-content-management-in-opencms).
