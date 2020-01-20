Title: Hints of change at Alfresco
Date: 2009-11-11T07:29:00Z
Modified: 2015-01-06T12:16:00.983Z
Category: misc
Tags: alfresco
Slug: 2009/11/hints-of-change-at-alfresco
Authors: Seth Gottlieb

I am beginning to see hints at serious changes happening within [Alfresco](http://www.alfresco.com). Historically the company has essentially operated as a commercial software company with a closed development model (that is, an internal opaque development team) and an open source version that was treated like shareware ("start using it and, if you like it, pay for the real product."). Gradually, Alfresco has been opening up to be more transparent and developer friendly. For example, now you can get the source of the Enterprise Edition. You just need to pay an annual subscription to use the compiled version if you want to get support.

  

Recent blog posts by Matt Asay (Alfresco's VP of Business Development) and John Newton (CTO) make me think there is more change to come. First, in April Matt wrote this post on how the (very permissive) [Apache Software License is better than the GPL](http://news.cnet.com/8301-13505_3-10229817-16.html?tag=col1;post-4129). That had me scratching my head because Alfresco uses the GPL license which is very strong at protecting IP. Alfresco had already loosened up a bit by providing a "FLOSS Exception" where a developer working on another project with another OSI approved license can incorporate Alfresco under that license. But the full Apache Software License goes much further. If Alfresco was Apache licensed, Oracle could embed Alfresco in one of their commercial software products for free.

  

Then John Newton wrote a post talking about the [virtues of professional open source and described Alfresco as a company that made money entirely from support](http://newton.typepad.com/content/2009/07/professional-open-source-software.html). At the time, I didn't really believe him because the terms felt like you needed to pay to use supportable software rather than pay for the support itself. I know this is a minor distinction but a support contract seems easier to walk away from than an annual subscription to use software. Still, I guess it would be possible to downgrade to a version of the Enterprise Edition that you compiled yourself.  

[More recently, Matt comes up with this article that is critical of "fauxpen source:"](http://news.cnet.com/8301-13505_3-10394478-16.html?part=rss&amp;tag=feed&amp;subj=TheOpenRoad) products that come out of a closed development process but are distributed under an open source license. He writes:  
>  In the future, I think we'll see this "fauxpen-ness" fade as companies clearly separate their open-source efforts from their revenue models. Open source can provide a platform for monetization, but it isn't the best way to actually generate cash. Not for most companies, anyway.   
I take this to mean that software companies will start to leverage the open source development model and get their revenue from sources other than renting out the IP of the software. Matt doesn't mention [Day Software](http://www.day.com) but that is clearly what Day is doing. Day sells commercial software products (CQ5 and the CRX) but heavily invests in components ([JackRabbit](http://jackrabbit.apache.org/) and [Sling](http://sling.apache.org/site/index.html)) that they have donated to the Apache Software foundation for open development. They use these Apache components in their products and encourage their competitors to do so too. Similarly, IBM invests in lots of Apache projects and Eclipse. Ex-Alfrescan Kevin Cochrane now works at Day and I am wondering if he is convincing his former co-workers on this strategy. I wonder if, now that there is a sufficient developer community, Alfresco will start to put development of some of their components (like their CIFS implementation or their Surf framework) out in the open where more people can contribute to it.  

If this _is_ what is happening, (and now I am really speculating) it could mean one of two things. One, Alfresco has reached a size and level of profitability that it can afford to let go of some immediate revenue to fuel some longer term growth. Two, Alfresco is less focused on creating a company with a tight grip on IP that it can quickly sell. Either way, I am very interested in how this plays out and will be watching for Alfresco components being released into an active development community.

  
  

___Disclosure__ I do not have any inside information on Alfresco and am speculating based on what I read on the web. I may be (and probably am) totally wrong._
