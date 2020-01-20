Title: The Onion&#39;s Migration from Drupal to Django
Date: 2010-03-25T11:22:00Z
Modified: 2015-01-06T12:16:16.790Z
Category: misc
Tags: development, django, drupal, architecture
Slug: 2010/03/the-onion-migration-from-drupal-to
Authors: Seth Gottlieb

There is a great [Reddit thread on The Onion's migration from Drupal to Django.](http://www.reddit.com/r/django/comments/bhvhz/the_onion_uses_django_and_why_it_matters_to_us/) [The Onion](http://www.theonion.com/) was one of the companies that I interviewed for the [Drupal for Publishers report](http://www.scribd.com/doc/77085653/Drupal-for-Publishers). One of the things I mention in the report is that The Onion was running on an early version (4.7) of [Drupal](http:drupal.org). The Onion was one of the first high traffic sites to adopt Drupal and the team had to hack the Drupal core to achieve the scalability that they needed.  While versions 5 and 6 of Drupal made substantial performance improvements, The Onion's version was too far forked to cleanly upgrade.  
  
Still, The Onion benefited greatly from using Drupal. They were able to minimize up-front costs by leveraging Drupal's native functionality and adapt the solution as their needs changed. Scalability was a challenge but it was a manageable one.  Even though forking the code base was not ideal, it was a better alternative than running into a brick wall and having to migrate under duress.  The Drupal community also benefited from the exposure and learning that came from The Onion using Drupal.  Everybody won &amp;mdash how often can you say that?  
  
I can understand the choice of [Django](http://www.djangoproject.com/) 1.1 (current) over a hacked version of Drupal 4.7.  Having built sites in both Drupal and Django, I can also see the appeal of using a Django over Drupal 6.16 (current). Django is a more programming-oriented framework and The Onion has programmers.  [Django is designed to be as straightforward and "Pythonic" as possible](http://www.springerlink.com/content/h6v521138njm2062/). Drupal tries to make it possible to get things done without writing any code at all; and [if you can avoid writing code in Drupal, you should](http://www.yelvington.com/content/first-rule-coding-drupal). As a programming framework, Drupal has more indirection and asserts more control over the developer.  The Onion's staff of programmers clearly appreciate the programmatic control that Django affords and they are quite happy with their decision.
