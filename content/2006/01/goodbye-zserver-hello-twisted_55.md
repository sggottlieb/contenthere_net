Title: Goodbye ZServer, Hello Twisted
Date: 2006-01-11T11:19:00.002Z
Modified: 2015-01-06T11:32:16.339Z
Category: misc
Tags: 
Slug: 2006/01/goodbye-zserver-hello-twisted_55
Authors: Seth Gottlieb

[Eric Shea](http://www.eshea.net/index.html) just passed on [this article](http://uk.builder.com/programming/python/0,39030014,39292462,00.htm) describing how [Zope3](http://www.zope.org/DevHome/Wikis/DevSite/Projects/ComponentArchitecture/FrontPage) is dumpinjg the old ZServer and go with [The Twisted Framework](http://twistedmatrix.com/) for its web server.   

For those of you unfamiliar with the Zope platform, ZServer is ancient, slow and not too secure. The security part is not so much of a problem because any serious Zope 2.x installation is going to sit behind an Apache web server. Twisted, on the other hand is a high performance framework for building Python applications. We did a prototype based on Twisted as part of a proposal for a very high traffic web service and our experience with it has been very positive. You may also notice the last name of one of the Twisted project team (Lefkowitz). [Glyph](http://www.livejournal.com/users/glyf/) is the son of r0ml, our former VP, Research and Executive Education. I am pretty sure that the Lefkowitz family enforces a strict nickname policy.  
