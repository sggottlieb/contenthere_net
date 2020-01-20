Title: &quot;VIBE&quot; on Liferay. Does this portal need a portal?
Date: 2009-05-28T15:36:00Z
Modified: 2015-01-06T12:15:59.366Z
Category: misc
Tags: portal
Slug: 2009/05/on-liferay-does-this-portal-need-portal
Authors: Seth Gottlieb

I just created an account on a new [Department of Energy](http://www.energy.gov/) site called [VIBE: Virtual Information Bridge to Energy Efficiency and Renewable Energy](http://vibe.nrel.gov). I love the idea. It is a site that provides data on many of the various energy issues and programs that the [National Renewable Energy Laboratory (NREL)](http://www.nrel.gov/) is working on. The site is even powered by renewable energy!

  

Another aspect of the site is that it is running on the Java portal platform [Liferay](http://www.liferay.com). While Liferay is definitely a mature and sophisticated platform, I wonder if using a portal was a good choice for this site. Like many portal-based sites, VIBE does a good job of putting lots of information on one page but struggles when it comes to navigating and organizing content. While there is no shortage of menu items on the VIBE site, many of the pages are empty containers waiting for portlets. If this was a regular content driven site, the navigation could be built up as content was added to the site. I wonder why they just didn't build the site on a more general web application framework. 

  

This experience reminded me of the narrow range of applications that need a true (as in [JSR 168 and 286](http://developers.sun.com/portalserver/reference/techart/jsr168/)) portal platform. When a business owner asks for a "portal" that presents lots of information from various sources, it doesn't mean that a developer should go and start downloading a portal product. In fact, I would go further to say that unless users _need_ to select their own portal themes and choose portlets on their pages, you should _not_ us a portal product. The reason why I emphasized the word "need" is that most users will not take the time to customize their own portal page. I had the ability to create my own personalized page on VIBE but I didn't want to bother. 

  

I am seeing a general trend of companies replacing portal-based delivery tiers with simpler technologies. One such example is the [Jahia](http://www.jahia.org/cms) web content management platform. They used to be based on [Jetspeed 2](http://portals.apache.org/jetspeed-2/). Now they just use the [Pluto portlet container](http://portals.apache.org/pluto/) that allows them to incorporate components that have been implemented as portlets. One of my newspaper clients replaced their portal based delivery tier for a simple, easier to manage JSP based architecture. 

  

Getting back to VIBE, I think their best portal strategy would be to not build a portal but rather provide Google and Facebook gadgets that people can use on the sites that they go to frequently. If a visitor takes any time to customize any portal page, it will probably not be their VIBE page. The bottom line is that due to their aggregating nature, the world actually needs only a few consumer facing portals. Far better to focus on producing great information and making it available on the portals that people are already using.
