Title: Different Storage Models for Content
Date: 2009-04-07T07:34:00Z
Modified: 2015-01-06T12:15:59.180Z
Category: misc
Tags: architecture
Slug: 2009/04/different-storage-models-for-content
Authors: Seth Gottlieb

Joel Amoussou has a great article explaining the [benefits and implications storing your content in a relational database vs. an XML store](http://efasoft.blogspot.com/2008/11/content-imperative-unlearning.html). After making the case for when to consider XML over the more common [RDBMS](http://en.wikipedia.org/wiki/RDBMS)/[ORM](http://en.wikipedia.org/wiki/Object-relational_mapping)/[POJO](http://en.wikipedia.org/wiki/Plain_Old_Java_Object)/Template approach, Joel provides some tips for content modeling and makes some great points about how you need to think a little differently when you work with XML.  

I would like to reinforce Joel's comment that the XML stack is quite different than technologies that you or your developers may be used to. The learning curve can be quite steep and many developers just give up before they really get it. Transitioning to an XML based architecture may not pay off for content management applications where your content types consist of a number of structured fields (like title and author) and one or more unstructured elements (like description and body) that the CMS just reads out what the author typed in - in other words, like this blog. 
