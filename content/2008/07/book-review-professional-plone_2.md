Title: Book Review: Professional Plone Development
Date: 2008-07-02T07:54:00.001Z
Modified: 2015-01-06T12:15:39.066Z
Category: misc
Tags: 
Slug: 2008/07/book-review-professional-plone_2
Authors: Seth Gottlieb

I just finished Martin Aspeli's [Professional Plone Development](http://www.amazon.com/gp/product/1847191983?ie=UTF8&amp;tag=contenthere-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1847191983)

<img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=1847191983" style="border:none !important; margin:0px !important;" width="1"/>

.  This is the third [Plone](http://plone.org) book that I have read over the years and it is definitely the most advanced. Do not take the words "professional" and "development" in the title lightly.  Martin is a brilliant developer with a long history in the Plone project so I would expect nothing less from him.  
  
What I found most helpful about the book is its coverage of the many new concepts that were introduced in versions 2.5 and 3 of Plone.  If you have been away from Plone for a while, it may be time to check back in. I think the coolest stuff is the incorporation of [Zope 3](http://www.zope.org/Products/Zope3) constructs.  The overall trend with Zope 3 is to make the platform less monolithic and more modular.  This allows you to use Zope components in everyday Python applications and to use more standard Python programming techniques in Zope applications.  The core Plone community has been energized by these new ideas for a while but they are just now starting to work their way into the mainstream.  If you don't know about these concepts yet, you are starting to fall behind.    
  
Considering the breadth, complexity, and innovativeness of Plone 3, Martin had a lot of ground to cover.  Still, he was able to provide useful summaries and examples while keeping some semblance of narrative flow (don't get too attached to his case example though. the book frequently wanders away from the example project of a movie theater website).  _Professional Plone Development_ helps orient readers and prepare them to embrace and leverage the concepts that advanced Plone developers use in successful projects.   Of course, to complete his education, the developer will have to read the source code and other online resources and, of course, learn by doing.  One thing I would like to see more of is references to online documentation (both in-line references and a "further reading" section at the end of each chapter).    
  
The ideal reader of this book is someone who knows his way around Plone and is proficient in Python - perhaps someone who has read [Plone Live](http://blog.contenthere.net/2005/08/plone-live-review.html) (which is now, unfortunately, pretty outdated - so much for a constantly updating book) and has built a few sites.  This kind of reader will really benefit from Martin's best practices of test-first development and setting up an efficient development environment.    
  
I also like how Martin de-mystifies the Zope platform which I have always regarded with fear and respect (except when I worked on a project to re-wire Zope to talk to an Oracle database rather than the ZODB: [pt1](http://blog.contenthere.net/2005/12/zoracle-part-i-problem.html), [pt2](http://blog.contenthere.net/2005/12/zoracle-part-ii-solution.html), [pt3](http://blog.contenthere.net/2005/12/zoracle-part-iii-connecting-zope-to.html)).  Martin reminds us that Zope is just a bunch of Python modules and it is OK to poke around and modify code to see how things work.  Just remember to set the code back to how you found it or risk angering the mystical Zope spirit :)
