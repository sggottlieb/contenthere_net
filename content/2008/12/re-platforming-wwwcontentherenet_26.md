Title: Re-platforming www.contenthere.net
Date: 2008-12-26T22:33:00.001Z
Modified: 2015-01-06T12:15:40.585Z
Category: misc
Tags: 
Slug: 2008/12/re-platforming-wwwcontentherenet_26
Authors: Seth Gottlieb

If you have been playing close attention, you might have noticed that [www.contenthere.net](http://www.contenthere.net) is now running on [WordPress](http://wordpress.org).  Prior to the migration, the site was hosted on a combination of [Blogger](http://www.blogger.com), [Yahoo Store](http://smallbusiness.yahoo.com), and some hand coded HTML (managed in [Subversion](http://subversion.tigris.org/) of course).  That arrangement was fine but I ran into limitations with the integration between Yahoo Store and the rest of the architecture.  There were no big show stoppers, just little inconveniences that I was getting tired of working around.  Besides, I was itching to tinker - we techies get like that sometimes.  
  
Selecting a new platform was fun because I got to be the client in a process in which I am normally the consultant.  I was quite different from a typical Content Here client.  First of all, I had no budget.  Second, the president of the company (i.e. me) wanted the technology to be fun to program in.  Third, I didn't want to choose a platform that I would recommend to my typical clients because I do not want to appear biased.  Incidentally, the last point is a main reason why I have held off implementation of a content management solution for so long.  
  
My first choice was the [Django](http://www.djangoproject.com/) web application framework.  I had done some prototyping on the platform and was really impressed with the cleanness of the architecture and how quickly you could build applications.  It is a little like [Ruby on Rails](http://rubyonrails.org/) but in Python.  Furthermore, Django has a popular e-commerce application called [Satchmo](http://www.satchmoproject.com/).  I installed Satchmo and was able to understand the code and make some quick customizations on it.  What really killed Django for me was the lack of a good blogging platform.  [There are a number of simple django blogging applications out there](http://blog.michaeltrier.com/2007/12/30/django-blogging-apps) but nothing seemed to fit the bill.  The closest was [Banjo](http://getbanjo.com/) but it didn't seem to be that well supported.   There is actually a [long standing discussion in the Django community about the framework's lack of mature blogging applications](http://www.b-list.org/weblog/2007/nov/29/django-blog/).  
  
The next two finalists were [Drupal](drupal.org/) and [WordPress](http://wordpress.org).  I have built sites on Drupal and like the framework a lot.  However, the commerce module always seems to be far behind the current release of the core.  I also think that Drupal is a little bit more than I need for my simple site (a blog with a shopping cart).  
  
My decision to go with WordPress started as a simple prototype.  I was amazed at how quickly I could create a theme to match my old design.  The commerce module [WP e-Commerce](http://www.instinct.co.nz/) looked pretty solid and I was able to quickly get it working with PayPal as my payment gateway.  I also found some useful plugins to provide me the features I was missing in Blogger (like related posts, etc.).  The thing that sealed the deal for me was the ease with which WordPress imported all my blogger posts and comments.  I was even able to make the permalinks match the same structure as Blogger's for easier URL re-mapping (just a simple rewrite rule).  Wordpress surely has its warts (there are plenty of places where the code gets pretty sketchy) but for a simple, reliable blogging platform with e-commerce capabilities, I am quite pleased.