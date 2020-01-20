Title: JCR: More than just Java
Date: 2005-10-24T08:25:00.002Z
Modified: 2015-01-06T11:32:15.275Z
Category: misc
Tags: 
Slug: 2005/10/jcr-more-than-just-java_72
Authors: Seth Gottlieb

If you have been intrigued by the [The JCR](http://www.jcp.org/en/jsr/detail?id=170) but feel left out because you are not a Java shop, you might be interested to know that other technologies are getting in the game as well. Henri Bergius, of the [Midgard CMS](http://www.midgard-project.org/) has started working on [making Midgard accessible to a JCR via JNI](http://www.bergie.iki.fi/blog/jukka_back_from_hiatus__jcr_for_midgard.html) (the Java Native Interface which allows you to execute native, non-java, code from a Java application). There has also been talk about a [PHP-170 project](http://thinkforge.org/projects/php170/) to implement a JSR 170 compliant repository in PHP although no code has been submitted.   

More recently, Stefane Fermigier has written about an attempt to [hook Zope into a JCR](http://blogs.nuxeo.com/sections/blogs/fermigier/2005_06_25_jsr_170_java_content) by using [JPype](http://jpype.sourceforge.net/), a Java-Python bridge. In this blog entry, Stefane makes a good case that the structure of the JCR is very similar to the ZODB because both are node based rather than relational (as in a relational database). Having JCR storage option this would address a common issue with Zope which is that the ZODB is closed and difficult to manage in extreme conditions. My current client has a ZODB which is over 45 GB (That is just text. Images are stored outside.) and is growing at a rate of 2 GB per month (packed). We are working on a prototype to store content in a relational database to get around that limitation. In the elevator, I ran into a former co-worker who works for another company upstairs and they are doing the exact same thing. The ZODB is enticingly easy to build applications on and, in most cases, more than sufficient. However, in extreme cases, alternatives, especially standards compliant ones, are nice to have. 
