Title: Licensing of Plone
Date: 2005-11-23T13:35:00.002Z
Modified: 2015-01-06T11:32:15.383Z
Category: misc
Tags: 
Slug: 2005/11/licensing-of-plone_12
Authors: Seth Gottlieb

There is a very interesting conversation happening in the Blogosphere about the conflicting licensing terms of Zope and Plone. [Paul Everitt](http://radio.weblogs.com/0116506/) does a very nice job of [summarizing the issue in his blog.](http://radio.weblogs.com/0116506/2005/11/21.html#a370)   

The general gist is that Zope uses the [Zope Public License (ZPL)](http://www.opensource.org/licenses/zpl.php) which is modeled after the Apache 1 license and is less restrictive than Plone's [GPL](http://www.opensource.org/licenses/gpl-license.php) license. Plone's use of a more restrictive license is thought by some to be uncooperative with the Zope community and confusing to users. I think Paul raises an excellent point that Zope did the exact same thing by not adopting the [OSI Certified](http://www.opensource.org) [Python license](http://python.org/2.3.2/license.html).  

However, [Chris McDonough](http://www.plope.com), in the comments of Paul's blog, raises a very good point that developers on the Plone platform tend to commit code to both Zope and Plone and having different licensing schemes makes things unnecessarily complicated. I definitely hear that. You don't want licensing terms to determine where your code belongs.   

I don't think that this problem is going to get solved but I don't think that it necessarily needs to. Paul has a nice status quo solution:  
>  Forget about product re-use. Instead, focus more on avoiding duplication of framework stuff. When somebody needs to do something, get them to do it at the right stack layer, under that layer's license. This is the goal of Goldegg. I think this is a more useful and realistic answer to code sharing in the stack.  
>   
By "forget about product reuse" Paul means trying to do things like using a piece of Plone in another (possibly proprietary) product. I think this solution makes sense and it is certainly more actionable than trying to get everyone to change their licensing schemes.  
