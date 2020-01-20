Title: Book Review: Django 1.0 Template Development
Date: 2009-03-26T21:47:00Z
Modified: 2015-01-06T12:15:59.082Z
Category: misc
Tags: django, book review
Slug: 2009/03/book-review-django-10-template
Authors: Seth Gottlieb

I just finished reading Scott Newman's book _[Django 1.0 Template Development](http://www.packtpub.com/django-1.0-template-design-practical-guide/book)_. This is the second [Django](http://www.djangoproject.com/) book that I have read (the first was <em><a href="http://www.amazon.com/gp/product/1590597257?ie=UTF8&amp;tag=contenthere-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=1590597257">The Definitive Guide to Django</a><img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=1590597257" style="border:none !important; margin:0px !important;" width="1"/><br/></em>) and I am very impressed by the number (and quality) of Django books that have been published. 21% of the respondents to a recent ["This Week in Django" poll](http://thisweekindjango.com/twid/episode/50/this-week-django-50/) said that they learned Django from reading a book (65% learned from the online documentation). Considering that until recently there were no Django books, this is significant.  

_Django 1.0 Template Development_ lives up to its title by focusing on the template layer of the Django web application framework although it does go through some basics of setting up your project and some of the details of the Django request handling pipeline. There is very little coverage of models - just enough to give the sample project some data to work with.  

There is good coverage of how templates are loaded and guidelines of how to develop views \[[1](#1)\] with plenty of tips on leveraging Django's many convenience features (like generic views) and organizing code for better manageability. There are examples for using and writing custom middleware, filters, and tags \[[2](#2)\] with special attention paid to best practices in security. A whole chapter is devoted to working with Django's pagination system. Explanations are well supported with the theory behind and examples that demonstrate the details of Django's behavior.  

The area that I was hoping for a little more depth was in optimizing performance. Django gives the developer a lot of options of how to design the application. For example, in addition to the typical template "include" syntax, Django also supports template inheritance (where a child template can extend and override blocks of a page from its parent). There is not much information on the performance implications of deep template hierarchies. The caching chapter gives a nice overview of Django's different caching options and engines and general guidelines but perhaps the art of really tuning a site is the topic for another book.  

I would highly recommend _Django 1.0 Template Development_ for anyone who wants to efficiently build a clean and manageable template layer for a Django project. In particular, a developer who needs to make the display tier flexible and extensible (such as the book's example of managing a separate site skin for mobile browsers). Although the preface recommends the reader have a working knowledge of Django and Python, I don't think that is really necessary. There is just enough information to help the developer to understand the overall Django framework but the emphasis is definitely on displaying data.

  
  
  

### Notes:

  

*   <a name="1">1</a> in Django, the "view" is the code that gathers and preprocesses the data for the template to render
  

<li><a name="2">2</a> These are important for a template developer because Django deliberately limits the amount of logic you can put into a template to force developers to keep templates clean and make code more reusable. Logic belongs in filters (that manipulate data) and tags (that do more complex logic), and middleware (where you inject additional functionality into the request/ response cycle).</li>
