Title: Daisy 2.1 Release is Official
Date: 2007-09-04T07:27:00.002Z
Modified: 2015-01-06T11:32:50.766Z
Category: misc
Tags: daisy
Slug: 2007/09/daisy-21-release-is-official_32
Authors: Seth Gottlieb

[Outerthought](http://outerthought.org/) just [announced the official release of Daisy CMS: version 2.1](http://outerthought.org/site/news/news-2007-09-03.html).  For those who are not familiar with [Daisy](http://cocoondev.org/daisy/index.html), it is a fairly simple, easy to use Java based WCM platform.  The front end is styled after a wiki although it supports more comprehensive WCM functionality such as structured content types, decent access control, and workflow.  The repository is de-coupled and is accessible through a ReST style interface so the more ambitious or [Cocoon](http://cocoon.apache.org/)-phobic (the user interface is written in Cocoon that has a steep learning curve) can write their own management interface and front end.   
  
Daisy is primarily used for basic informational sites, intranets, and knowledge bases.  Some companies use it to create documentation because of its XML  oriented architecture, its book publishing features, and also its powerful versioning and localization functionality.  Thanks to a partnership with the Belgian systems integrator [Schaubroeck](http://www.schaubroeck.be/), Daisy is widely used for local and regional Belgian government sites.  Daisy development is managed by Belgian systems integrator and software developer [Outerthought](http://outerthought.org) which also sells support packages on the platform.    
  
This new release is supposed to be easier to configure and manage (thanks to a new [Spring](http://www.springframework.org/) based runtime container) and includes a very cool visual version diff'ing tool.  Unfortunately Daisy is still missing user input validation out of the box.  You can only set whether a field is required and the size of the input box.    
  
If you have been looking for a basic, mature Java WCM and have been turned off by the complexity (in terms of user interface, architecture, and social dynamics of the community) of [Apache Lenya](http://lenya.apache.org), you should give Daisy a look.
