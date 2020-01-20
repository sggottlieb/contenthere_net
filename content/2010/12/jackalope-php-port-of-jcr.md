Title: Jackalope: A PHP Port of the JCR
Date: 2010-12-09T09:03:00Z
Modified: 2015-01-06T12:16:17.555Z
Category: misc
Tags: jcr, php
Slug: 2010/12/jackalope-php-port-of-jcr
Authors: Seth Gottlieb

Kas Thomas (from [Adobe/Day](http://www.day.com)) writes that a [PHP port of the JCR (called Jackalope) is near completion.](http://dev.day.com/content/ddc/blog/2010/12/a_php_port_of_jcr.html) A big part of the project was to translate the JCR specification (which, like Java, is statically typed) to PHP's dynamic typing model.  The result is a derivative specification called the [PHPCR](https://github.com/jackalope/phpcr/blob/master/doc/JCR_TO_PHPCR.txt).  
  
PHP developers have had access to JCR repositories for quite some time through [Apache Sling](http://sling.apache.org/site/index.html) (which puts a nice REST interface in front of a JCR).  What [Jackalope](https://fosswiki.liip.ch/display/jackalope/Home) brings to the table is a PHP-based, in-process API that may be faster than hitting a REST interface.  However, that doesn't mean PHP developers can totally forget about Java.  The current implementation is an adaptor that connects to a JCR ([Apache JackRabbit](http://jackrabbit.apache.org/)) through webDAV (so http is still in the mix too).  The next phase of development will swap out the JCR storage backend with a basic database thereby removing the JVM from the picture entirely.
