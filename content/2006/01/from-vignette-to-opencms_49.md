Title: From Vignette to OpenCMS
Date: 2006-01-06T18:04:00.002Z
Modified: 2015-01-06T11:32:16.193Z
Category: misc
Tags: 
Slug: 2006/01/from-vignette-to-opencms_49
Authors: Seth Gottlieb

Apoorv Durga on his [PCM Blog](http://www.apoorv.info/index.php) has a [nice post](http://www.apoorv.info/index.php/2006/01/07/from-vignette-to-opencms/) about a migration from [Vignette](http://www.vignette.com) to [OpenCMS](http://www.opencms.org). The overall project went well and the client was pleased with the results. Apoorv also points out that some features are missing from OpenCMS most notably large site features such as replication and backup. For example, in Vignette, you have a staging server where you manage content and a production server where you display content. OpenCMS does not have that so you you have one server (or cluster) doing both content management and delivery. This may have security and (in extreme cases) performance implications (although with caching turned on and clustering, it is likely that it is not an issue.).  

If content syndication is important, you might try [Magnolia](http://www.magnolia.info) which has a subscriber model that allows an authoring server to publish content to display servers. Of course, Magnolia is missing many of OpenCMS's advanced features such as versioning and workflow. But if those are not important (frequently people think they need these things more than they actually do), you should give Magnolia a look. It uses a [JCR](http://www.jcp.org/en/jsr/detail?id=170) (implemented by [The Apache JackRabbit Project](http://incubator.apache.org/jackrabbit/)) and that is not something that you see in many commercial products.  
