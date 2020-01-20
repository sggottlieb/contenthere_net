Title: PHP + JCR = PHPCR
Date: 2011-07-18T10:38:00Z
Modified: 2015-01-06T12:16:18.396Z
Category: misc
Tags: jcr, php, development, architecture
Slug: 2011/07/php-jcr-phpcr
Authors: Seth Gottlieb

My former colleague [Lukas Kahwe Smith](http://pooteeweet.org/) recently gave me a update on what is happening with the [PHPCR initiative](http://phpcr.github.com/). Readers of this blog might remember me make [a brief mention of PHPCR and the Jackalope implementation](http://www.contenthere.net/2010/12/jackalope-a-php-port-of-the-jcr.html). My initial response was that I was unsure of whether the idea would take off but now I am pretty impressed with what I heard from Lukas.  

Lukas and his team from [Liip AG](http://www.liip.ch/) have been contributing to Jackalope as part of a large custom, content-centric web application they are building for a client using [Symfony2](http://symfony.com/). Jackalope goes beyond standard relational database persistence by providing sophisticated content services like content hierarchy, tree traversal, versioning, and content staging — common weaknesses in [homebrew CMSs](http://www.contenthere.net/2007/07/homebrew-cms.html).  

I can see a number of benefits to a PHP developer using PHPCR

  

  
 *   There is less to build than when working directly against a REST interface like [Apache Sling](http://sling.apache.org/site/index.html). You don't have to worry about making requests and marshaling XML or JSON into programmable PHP objects.
  
 *   Your code can store any type of data in the JCR (not just documents). Using CMIS would be a bit of a stretch for anything but document data. Liip has developed an [object-to-JCR node mapping layer (called phpcr-odm. Part of the Doctrine project)](https://github.com/doctrine/phpcr-odm) that behaves like a PHP [ORM](http://en.wikipedia.org/wiki/Object-relational_mapping) service.
  
 *   The persistence engine is abstracted so you can swap it out with something that meets your performance needs. Jackalope ships with [Apache JackRabbit](http://jackrabbit.apache.org/) but there are also transports in the works for [MongoDB](http://www.mongodb.org/) and standard SQL databases. They should be mature by the end of the year.
  
 *   You can use PHP to build delivery tiers and other web applications using content managed in a JCR-based CMS (such as [Adobe CQ5](http://www.day.com/day/en/products.html), [HippoCMS](http://www.onehippo.com/en/products/cms), or [Magnolia](http://www.magnolia-cms.com/)).
  

  

If you are building a content-centric web application in PHP, and you find yourself doing unnatural things to a relational database to meet your requirements, consider using Jackalope or the [Midgard PHPCR implementation (which is designed more for speed)](https://github.com/bergie/phpcr-midgard2). You are probably already be using Lucene for search indexing, how much trouble can one more Java application be to manage on your infrastructure?
