Title: Plone and Zope 3
Date: 2006-02-06T12:53:00.002Z
Modified: 2015-01-06T11:32:16.894Z
Category: misc
Tags: 
Slug: 2006/02/plone-and-zope-3_89
Authors: Seth Gottlieb

Rocky Burt wrote a nice [post](http://www.serverzen.net/weblog/archive/2006/02/03/plone-and-zope-3) on how Plone development is converging with the new Zope 3 architectural patterns through the help of the [Five Project](http://codespeak.net/z3/five/). If you are just coming up to speed, Zope 3 is a major change from Zope 2.x and introduces some modern architectual patterns such as content views in addition to incorporating some critical content management functionality from CMF (Content Management Framework, an add-on product on top of Zope) into the core. Here Rocky's summary of the benefits and risks:  

>  
> __Benefits__  
> Of course further development, refactoring, and refining the base architecture generally provides a more robust solution to such an extent that businesses have to spend less time and effort managing and supporting deployed solutions. Having reusable components means less time spent developing new components and more time spent plugging in existing components which proves to take less time and thus less expense.  
> 
> __Risks__  
> Migration of existing sites can get quite complicated. Also having to deal with switching frameworks such as making it difficult to maintain backwards compatibility with third-party products. Of course this gets easier as more and more third-party products adopt the same Zope 3 develop techniques which means education of this process moving forward is vitally important.  
> 
> 

In the end, he concludes that committing to the Zope 3 architecture and development style is the right approach. I would tend to agree.
