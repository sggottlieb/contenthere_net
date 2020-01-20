Title: Nice article benchmarking Joomla! and Drupal
Date: 2006-08-22T13:04:00.002Z
Modified: 2015-01-06T11:32:19.250Z
Category: misc
Tags: 
Slug: 2006/08/nice-article-benchmarking-joomla-and_40
Authors: Seth Gottlieb

I just saw this [blog post](http://buytaert.net/drupal-vs-joomla-performance) by Dries, who is one of the lead programmers on the Drupal project.  The article compares the performance of [Drupal](http://drupal.org) and [Joomla!](http://www.joomla.org).  The tests look pretty fair. The interesting finding is that, while Joomla! generates pages faster, Drupal's caching system is more efficient.  Joomla!s performance boost from caching seems really modest. Perhaps Dries knows more about Drupal caching than Joomla!  That would be understandable.  For both of these applications, the caching mechanism is not used for logged in users.   Both projects are adding framework layers and making the code more object oriented.  These layers of abstraction make the code more maintainable but make the application do more work in executing code.  Both give you choices of developing PHP based templates or using a rendering engine with non-PHP based tagging syntax.  Still, the benchmarks look pretty good.  I am sure they would be even better with a PHP accelerator.   
  
On a similar topic, I was at a meeting of the Boston Chapter of [CM Professionals](http://www.cmprofessionals.org) and one of the attendees brought up the fact that most commercial software EULAs and certain Federal laws forbid customers from publishing reviews or benchmarks of their software.  Man, I would get into trouble if I wrote about commercial software.  If anyone knows more information about this, please post comments or send me an email.
