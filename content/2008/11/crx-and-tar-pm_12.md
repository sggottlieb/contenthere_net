Title: CRX and Tar PM
Date: 2008-11-12T11:15:00.001Z
Modified: 2015-01-06T12:15:39.989Z
Category: misc
Tags: 
Slug: 2008/11/crx-and-tar-pm_12
Authors: Seth Gottlieb

Thomas Müller has a [blog post that nicely describes how the Tar PM works](http://dev.day.com/microsling/content/blogs/main/tarpm.html).  Tar PM is the fastest of [Day CRX's](http://www.day.com/content/day/en/products/crx.html) pluggable persistence managers.  The speed of Tar PM is a major reason why some companies go with the CRX rather than the free JCR reference implementation [Apache JackRabbit](http://jackrabbit.apache.org/).  
  
The key to Tar PM's speed is that it only supports write operations and these operations just append the new data to the end of one big file (a [TAR](http://en.wikipedia.org/wiki/Tar_(file_format)) file actually).  What content objects are stored where is recorded in an index which is also read-only.  To prevent limitless growth of the data file, you need to periodically run maintenance programs that compress the file be removing deleted records.    
  
This may seem very familiar to those of you who have managed systems built on [Zope](http://zope.org) (like [Plone](http://plone.org)) and have had to "pack the database" - an operation that does essentially the same thing as the CRX tools plus remove unneeded intermediate versions that were defensively saved during transactions.  From my experience with Zope, I know that having a huge, single file database can be scary but not necessarily dangerous.  What do you do if you have a corrupt record in the middle of the file that causes the maintenance tools to crash?  Usually there is some way to fix it but you need access to the experts.  The only issue is that Zope and CRX experts are not as easily found as Oracle, MySQL, or MSSQL experts.  Tar PM seems to improve on the ZODB by switching to a new TAR file after a certain point.  Longtime readers of this blog may remember my ZOracle Series (part [I](http://blog.contenthere.net/2005/12/zoracle-part-i-problem.html), [II](http://blog.contenthere.net/2005/12/zoracle-part-ii-solution.html), and [III](http://blog.contenthere.net/2005/12/zoracle-part-iii-connecting-zope-to.html)) that described a project to point the Zope Object Database (ZODB) to an Oracle database.    
  
Although both Zope and Day have customers with huge repositories, the general rule of thumb is to keep things small when you can.  In the ZODB world there are extensions that store large binary files outside of the database.  In the JCR world, the strategy is to segment content into smaller repositories.  For example, if you have lots of publications, put each one into its own JCR instance rather that combine them all into one.  Companies that pursue this type of segmentation need to have some component in the architecture that can look across repositories and maintain collections of references to show an aggregated view.  At the simplest level, this can be a search engine.  At a more advanced level there could be hierarchical taxonomy system with references to items in different repositories.    
  
This strategy runs against Oracle's vision of all your company's content neatly organized in one big database.  I would argue that putting everything in one place does not necessarily mean that it is well managed or easy to find.  More important than how the content is physically stored is that it is cohesively organized (that is, content that belongs together is stored together) and that there are uniform ways to access it.  This is the strategy of the JCR and it plays well with service oriented architecture where different applications (services) that manage their own data can be combined to support cross-application business processes.   When you have everything in the same database, the tendency is to do your integration at the data level (which can be brittle and proprietary) rather than the application (or service) level.  I won't deny that it is handy to have a database that can scale infinitely in size and there are applications that need very large storage (like archival systems).  But trying to keep things small and segmented has its virtues as well.  I am reminded of the frequently made point that storage is cheap but finding and managing the information can be very expensive.