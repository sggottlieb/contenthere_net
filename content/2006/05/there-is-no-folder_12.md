Title: There is no folder
Date: 2006-05-08T15:28:00.002Z
Modified: 2015-01-06T11:32:17.962Z
Category: misc
Tags: 
Slug: 2006/05/there-is-no-folder_12
Authors: Seth Gottlieb

I had [this blog post by](http://theploneblog.org/blog/archive/2006/03/18/there-is-no-folder) Jonah Bossewitch bookmarked for quite some time and I figure I should mention it not only for it's brilliant [Matrix](http://www.imdb.com/title/tt0133093/) reference ("Do not try to bend the folder -- that's impossible. Instead, only try to realize the truth. Then you will see that it is not the folder that bends--it is only yourself."), but its mind bending implications for content management.  

Most web content management systems, see content as something that can be organized into hierarchical structures. Web sites are frequently represented by sitemaps and navigation which presume everything has a place in a tree. I say this is a vestige of a static web world where the web server merely served up what was on a file system (which is a hierarchical organization of folders and files). If the web were to be organized that way, it would stink. Luckily it isn't. The web is a collection of interconnected nodes. Search engines flatten out the web into topic based lists based on the occurance of words and [billion dollar algorithms.](http://finance.yahoo.com/q?s=GOOG) Interestingly [Google Desktop](http://desktop.google.com/?promo=mp-gds-v1-1) evokes a devotion similar to [TiVo](http://www.tivo.com/0.0.asp) for making a mess of poorly organized content (television is organized by time) accessible and useful. So, it isn't even that we don't understand other people's hierarchical organizational structure, we can't even find things that we file away in our own, custom designed filing system.  

The latest trends in tagging and social bookmarking are just other, more intentional, ways to create lists of content on a topic area. [Flickr](http://http://flickr.com)'s [Tag Cloud](http://en.wikipedia.org/wiki/Tag_cloud) is an example of structureless dynamic navigation.   

So what open source content management systems are the best for supporting this more _evolved_ view of websites? I would agree with Jonah that [Drupal](http://drupal.org) is the most oriented toward tagging. Drupal has no folders, just vocabularies and topics. It makes sense that Drupal would be first to execute this new vision because it is designed to enable a community to post and discuss ideas and news which don't necessarily belong in a single place within an informational tree. Blog software such as [Wordpress](http://wordpress.org/) and [Roller](rollerweblogger.org) deliver this functionality through categories. Sadly, [Blogger](www.blogger.com) does not have categories. Perhaps this is over-confidence in the Google search algorithm? Granted, your average not-so-technical knowledge worker may have a hard time breaking out of the desktop metaphor of putting things in representations of physical "places."  

Jonah also points out how [Plone](http://plone.org), which is built on the folder based [Zope](http://zope.org), has Smart Folders which are really saved searches. This allows you to create dynamic topic based lists without entering the same search criteria every time. I am waiting to see a Plone site whose navigation is all Smart Folders. Incidentally, Smart Folders and [ATCTSyndication](http://plone.org/products/plone/roadmap/128) is a powerful combination that will allow you to create a RSS feed on any search.   

While [eZ publish](http://ez.no) is very folder based, it has a nice separation between "object" and "location" that allows an object to exist in more than one locations. Content assets within [CPS](http://www.cps-project.org) exist in a placeless repository and are accessible through the site hierarchy through "proxies." This also allows a piece of content to exist in multiple places at once.   

If you enjoy this topic you should take the time to read Clay Shirky's long but very good blog post [Ontology is Overrated: Categories, Links, and Tags](http://shirky.com/writings/ontology_overrated.html), which inspired Jonah's post. Clay makes some great observations about how [Yahoo!s](http://www.yahoo.com) elitist, top down organization of the web ("We understand better than you how the world is organized, because we are trained professionals") is inferior to Google's view that "There is no shelf. There is no file system. The links alone are enough." I would add that [dmoz](http://dmoz.org/) is even more deluded thinking that a web site only belongs in one node of their hierarchy.  

It looks like tagging is trumping hierarchies and taxonomy on the big Web. I would be very interested in hearing how these concepts are playing inside of the corporate firewall. If you have a story to tell, please comment here or send me an email. The average corporate intranet is definitely failing to deliver on the promise of being "institutional knowledge at your fingertips." Will tagging and search be the paradigm that saves it?