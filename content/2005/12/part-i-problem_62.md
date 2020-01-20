Title: &quot;ZOracle&quot; Part I: The Problem
Date: 2005-12-27T12:38:00.002Z
Modified: 2015-01-06T11:32:15.944Z
Category: misc
Tags: 
Slug: 2005/12/part-i-problem_62
Authors: Seth Gottlieb

[Optaros](http://www.optaros.com) recently finished a project to build a prototype that adapted an elaborate [Zope CMF](http://www.zope.org/Products/CMF/)-based custom CMS to persist content to an Oracle database rather than the ZODB. The reason for doing this was that the ZODB was not performing adequately under the heavy load that the CMS was subject to and was not open to non-Zope technologies that our client wanted to share data with at the database layer. The next set of blog posts will talk about the problem, various solutions, and what we did. These posts are slightly more technical than other posts on this blog and I wonâ€™t be insulted if some of the more management types just skim through them ;)  

__The problem__  
  
The system that we were working with has a very large repository (45 GB of text - images and other binary files are stored outside of the ZODB) that is continually being written to (tens of thousands of new objects a day). They use FileStorage, rather than [DirectoryStorage](http://zopewiki.org/DirectoryStorage), because there are so many objects in the ZODB that the operating system would run out of [inodes](http://en.wikipedia.org/wiki/Inode). Because the database is so big and gets bombarded by so many write requests (the ZODB is effectively single threaded and is optimized for reading rather than writing), the systemâ€™s performance is just barely acceptable. There is also a risk of data corruption which would lead to extensive down time which would be disastrous for this mission critical application.  

In a [Zope CMF](http://www.zope.org/Products/CMF/) based application, everything is stored in the ZODB (except, in this case, binary files which are stored directly on the file system). This includes objects themselves, version information, history, the search indexes (called portal\_catalog), and, to some extent, code. While the maintaining the search index represents a significant amount of overhead in this application, the primary target for removing from the ZODB was the actual content objects themselves because there was a desire to expose the content within the repository (read only) to non Python applications. Oracle as a repository was particularly desirable because the client owns a site-license for Oracle and wants to leverage Oracleâ€™s capabilities of administration, tuning, and back-up and recovery.   

The system already uses [ZEO](http://zopewiki.org/ZEO) but technologies that would relieve pressure on the storage tier, such as [Zope Replication Services](http://www.zope.com/products/zope_replication_services.html), were tried and failed because of the write-intensity of the application. The right solution would improve performance and store content in fielded data (as in relational tables) rather than the ZODB. Also critical, the solution needed to go in smoothly with as little disruption as possible to the sophisticated and complex application sitting on top. None of the existing solutions seemed to have much promise.   

*   [OracleStorage](http://www.zope.org/Products/OracleStorage) was ruled out because, in addition to being somewhat stagnant over the passed few years, it fails on the requirement of being open to non-Zope technologies. OracleStorage stores Zope objects in [Python Pickles](http://www.zvon.org/other/python/doc21/lib/module-pickle.html) which are serialized Python objects (equivalent to [Serializable](http://java.sun.com/j2se/1.4.2/docs/api/java/io/Serializable.html) in Java. Non-Python applications would have a difficult time reading pickles.  
    
*   The newer project [APE](http://hathawaymix.org/Software/Ape), an [Object-Relational Mapping](â€http://en.wikipedia.org/wiki/Object-relational_mappingâ€) layer for Zope (like [Hibernate](http://www.hibernate.org/) in the Java world), looked like a viable option but earlier prototypes using APE suffered from performance. There was also concern about how the underlying caching mechanism would behave under load. The ultimate breaker was that the documentation on configuring APE was pretty thin.  
    
*   Another solution, which may still be used as a fall-back, was to have a nightly script that iterates through the ZODB and writes to an Oracle schema. This would solve the problem of having the content available in a relational database, but it would not solve any performance issues and would not a safeguard against corruption. This option could be selected in conjunction with Oracle storage if OracleStorage was more actively maintained.  
    

  
The solution that we wound up going with took advantage of a particular design characteristic of the system: that all of a content asset's attributes were actually stored outside of the asset in a class derived from Zopeâ€™s [PropertySheet](http://www.zope.org/Control_Panel/Products/OFSP/Help/PropertySheet.py).   

Next: an overview of the solution we went with.
