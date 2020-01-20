Title: Python Gets Drupy
Date: 2008-06-23T14:07:00.001Z
Modified: 2015-01-06T12:15:38.831Z
Category: misc
Tags: 
Slug: 2008/06/python-gets-drupy_23
Authors: Seth Gottlieb

Via [Boris Mann's blog](http://bmannconsulting.com), I just learned about [Drupy](http://drupy.net/) - a full port of [Drupal](http://drupal.org/) on [Python](http://www.python.org/).  Among all the initial reactions I have to this announcement, the one that screams the loudest is "why?"  
  
Drupal is an intentionally, non-object oriented framework.  Drupal does not use PHP's implementation of classes and there is no inheritance - at least not in a classic OOP sense .  The architecture works by exposing _hooks_ by which modules can be called by core system functions and do extra stuff.  To a Python programmer thats just, well, [un-pythonic](http://faassen.n--tree.net/blog/view/weblog/2005/08/06/0).    
  
Python is a super-object oriented language.  EVERYTHING is an object.  Even a function is an object (pause to wait for non-pythonista heads to stop spinning).  Python also has plenty of frameworks of its own.  [Zope](http://zope.org) is the grand-daddy of content oriented web application frameworks but it is a lot more complicated to fully understand than Drupal.  [Django](http://www.djangoproject.com/) fills the role of a leaner, content-friendly Python web application development framework.  Furthermore, one of the really great things about Drupal is that it is written in PHP and it doesn't take too long for a good PHP programmer to understand how it works.  There are far fewer Python developers than PHP developers out there.  
  
The single reason why this could be a good idea is if you could run Drupal modules on top of Drupy.  However, given that modules often don't work across multiple versions of Drupal, my confidence that they could integrate with Drupy is very low.  I think a better idea would be a CMS that is functionally similar to Drupal written on top of a Python framework (like Django).  In particular, a CMS with strong user profile management, a taxonomy based system for organizing the repository, and extensible through the addition of modules.    
  
Of course, like with a lot of other things, I reserve the right to change my mind when I see more.  But for now, I'll take my Drupal in PHP and go with something else when I want to code in Python.  Drupy team, I welcome you to prove me wrong.
