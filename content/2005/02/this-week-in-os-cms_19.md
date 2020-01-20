Title: This week in OS CMS
Date: 2005-02-09T11:45:00.002Z
Modified: 2015-01-06T11:32:13.626Z
Category: misc
Tags: 
Slug: 2005/02/this-week-in-os-cms_19
Authors: Seth Gottlieb

This post is an experiment on the concept of a weekly summary of development activity on an open source project. One of the great things about open source software is the transparency. All discussions happen out in the open on mail lists and forums so an enormous amount of knowledge is captured in an archivable format. On the downside, following these lists takes an inordinate amount of time for someone with other priorities. Therefore, I was thinking a human filtered and summarized digest would be something of value to users of an open source software product.  
  

I am trying to determine the appropriate level of detail. The targeted audience is a manager of either software development or network operations - someone who does not have time to read the full list but wants a little more information than what one would get with announcements. I would appreciate feedback as to whether this type of information is useful. __Now, on with the show.....__  
  
  

__This Week in Plone__  
  

Release 2.1 is scheduled for May 2005. It will run on Zope 2.x rather than the new Zope 3.x  
  

Three developers (Philip Auersperg, Jadok Batlogg, and Jens Klein) have started an initiative to enhance Plone's content editing forms by adding some client side scripting to perform functions like validation and multiple object editing without reloading the page. This is in response to [PLIP 53](http://members.plone.org/development/plips/53). The team has a [mockup](http://members.plone.org/Members/batlogg/concepts/zuccaro/daidalos_edit) available for review.  
  

  
  
  

__This Week in Lenya__  
  

A new feature which enables XMLHTTP was submitted by Josias Theony and checked into the trunk on February 9th. For those who do not know, XMLHTTP allows a page to call back to the server to get more data without an entire page reload. Probably the most famous example of XMLHTTP in action is [Google Labs'](http://labs.google.com/) [ Google Suggests](http://www.google.com/webhp?complete=1&amp;hl=en). Try typing in the search box and watch common search terms start appearing.  
  

An enhancement to make the menuing system cleaner and more flexible has been added to the trunk.  
  

There have been a few updates to improve the installation guide.  
  

On February 8, a massive patch (1.2 MB) was applied to the trunk. This was the result of code cleanup effort by Gregor Rothfuss. The update adds missing javadocs, fixes some resource leaks, and makes exception handling more explicit. Now the Eclipse Find Bugs plugin is more useful on the Lenya code base.  
  

Version 1.4 of Lenya will introduce a replacement to Lenya Usescases (sequences of pages) called UsecaseFramework which uses Cocoon Flow. There is some updated information on the [Wiki](http://wiki.apache.org/lenya/LenyaUsecases)
