Title: Supporting Internet Explorer 6
Date: 2010-04-14T10:13:00Z
Modified: 2015-04-10T13:55:22.719Z
Category: misc
Tags: browsers, development
Slug: 2010/04/supporting-internet-explorer-6
Authors: Seth Gottlieb

<a href="http://www.flickr.com/photos/sggottlieb/4420066985/" title="IE6 not supported on Microsoft.com by sggottlieb, on Flickr"><img alt="IE6 not supported on Microsoft.com" height="408" src="http://farm5.static.flickr.com/4053/4420066985_c6f108df82.jpg" width="500"/></a>  

  

Over the past few days, I have been involved in a number of conversations about supporting Internet Explorer 6.  Arguing about when to drop support for outdated browsers is a sport that is as old as the web itself.  There is nothing really new here but the IE6 support debate feels particularly emotional — not as charged as back when people were arguing for only supporting Internet Explorer, but close.  

IE6 had a really long run.  [It was Microsoft's browser offering for 5 years (late 2001 through late 2006)](http://en.wikipedia.org/wiki/Timeline_of_web_browsers).  Up to that point, Microsoft was releasing a major version of IE every year.  Now it looks like they are settling into a pace of every other year. That means that IE 6 was installed on a lot of computers.  In particular, a lot of computers that were bought when internet usage was starting to get really ubiquitous.  In many businesses and households, these computers were bought as an internet appliance with a really long expected lifespan — like a refrigerator or a telephone.  Companies are hanging onto their old IE6 computers.  Vista's flop means that Windows XP is still the corporate standard and IE6 comes with XP.  Unless you have a technical or information-intensive job or are working at a new company, chances are you are on a highly locked down, old Windows XP computer that your employer begrudgingly bought to give you access to email and the intranet.  Your employer doesn't want to upgrade your machine unless absolutely necessary.  That usage pattern has caused IE6 to linger longer than other browsers.  See how IE8 seems to eat up more of IE7's market share than IE6's?  

  

<a href="http://www.flickr.com/photos/sggottlieb/4520850462/" title="Internet Explorer Browser Share by sggottlieb, on Flickr"><img alt="Internet Explorer Browser Share" height="242" src="http://farm3.static.flickr.com/2691/4520850462_539af4d708.jpg" width="500"/></a>  

  

Not only do the numbers of IE6 user continue to be significant, the types of users seem to be desirable as well: internet n00bs that click on ads and buy what they see (with the money that was not taken by [Nigerian 419 scams](http://en.wikipedia.org/wiki/Advance-fee_fraud)).  

Technical people have little empathy for these types of users.  The first thing we do when we boot up a relative's computer for home tech support is stop the malware/adware processes, install Firefox, and hide the IE icon.   As developers, we know that a requirement for IE6 support translates into maintaining two code bases: one that uses all the goodness of the latest HTML and CSS standards and fast Javascript engines; and another that is a bundle of hacks to compensate for IE6's quirks.  Many web development firms I know are starting to charge an additional 20% - 30% to include IE6 support.  They are not price gauging. This is probably less than the actual cost.  The customer will probably invest an even larger percentage of additional resources to maintain the application.  

For this reason, an increasingly larger number of websites are discontinuing support for IE6.  They have done the calculations and have decided that the convenience for the IE6 hold-outs is not worth additional cost and drag on innovation.  I don't mean  to sound like a jerk, but big web properties (like [Google](http://www.google.com/), [Microsoft](http://www.microsoft.com/), and [Content Here](http://www.contenthere.net/)) dropping IE6 is a good thing for everyone (almost):  

  

*   Visitors will have a greater incentive to upgrade. If they can't upgrade on their own, they can make the case to their employers that running a 9 year old browser is not acceptable.
*   The more modern technology will increase overall security
*   Web sites and applications can be developed more cheaply and with higher quality.
*   The spending to upgrade outdated equipment will be good for the economy. Companies and households don't have to buy $2,000 laptops, they can probably get away with cheap NetBooks.

  

This site never supported IE6.  If you are stuck on that browser, I am sorry for the inconvenience that I have caused.  But, I figure you are used to browsing broken websites by now :)
