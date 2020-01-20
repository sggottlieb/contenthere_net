Title: Evaluating PHP Applications
Date: 2006-03-27T14:35:00.002Z
Modified: 2015-01-06T11:32:17.530Z
Category: misc
Tags: 
Slug: 2006/03/evaluating-php-applications_86
Authors: Seth Gottlieb

While not quite as trendy and chic as [Ruby on Rails](http://www.rubyonrails.org/), PHP is becoming widely accepted as an excellent platform for rapidly building web applications. PHP runs fast and lean on a server and is easy to work in. The PHP language supports object oriented programming and there are a number of frameworks that support patterns and functionality similar to some of the Java web application frameworks. Even IBM, which invested millions of dollars developing and promoting Java, has integrated [PHP into their strategy](http://contenthere.blogspot.com/2005/12/boston-php-user-group-meeting.html) and has made [some bets on the technology](http://searchwebservices.techtarget.com/originalContent/0,289142,sid26_gci1113808,00.html). [JSR 223](http://www.jcp.org/en/jsr/detail?id=223) is a new Java specification for writing Java objects so that they can be accessed from scripting languages like PHP. Not surprisingly, many of the open source CMS are built in PHP.   

One valid and accepted concern with PHP is security. Over the years, there have been several rather serious exploits to PHP based applications. Part of this is the technology itself and part of it is the style with which the applications may have been developed: fast and loose. This problem is not unique to open source or PHP. I have seen plenty of commercial software products with gaping holes. For example, it used to be when you installed Interwoven TeamSite, you got a wide open proxy server that anyone could use. If you were not careful, you could have half of China connecting through you to get to sites forbidden by the government. This information wasn't published anywhere obvious (certainly not on the sales literature), I found out when the bandwidth consumption was going through the roof.   

With open source, you have a better chance of finding about about these problems because they are publicly discussed within the community. When selecting software, look at the security track record which you should have access to. [This article by Harry Fuecks](http://www.sitepoint.com/blogs/2006/03/24/evaluating-php-applications/) gives some useful pointers. Once you have deployed the application, stay on the developer list (many projects have security specific lists) and subscribe to web security alerts. With a little bit of attention, you can have piece of mind about the security of your application.  