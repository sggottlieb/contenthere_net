Title: An Evening with Joomla&#39;s Mitch Pirtle
Date: 2006-01-04T14:37:00.002Z
Modified: 2015-01-06T11:32:16.070Z
Category: misc
Tags: 
Slug: 2006/01/an-evening-with-joomla-mitch-pirtle_69
Authors: Seth Gottlieb

Last night [BostonPHP](http://www.bostonphp.org) hosted an evening with Mitch Pirtle of [Joomla!](http://www.joomla.org/) fame at our [our Boston office](http://www.optaros.com). Mitch is a great speaker and his passion for Joomla! and open source really came through in his presentation. While most of the talk turned into an introduction to Mambo, Mitch did weave in some good background about Joomla!'s break from Mambo and where Joomla! is going. He promises to come back to get more into details about technology behind Joomla!  

First, some details about the split. Mitch related his experience of sitting in a conference booth representing Mambo and then seeing an [open letter](http://forum.mamboserver.com/showthread.php?t=56587) announcing Miro's formation of the Mambo foundation without involving the core development team. Just at that moment, he saw [Eben Moglen](http://emoglen.law.columbia.edu/) from the [Software Freedom Law Center](http://www.softwarefreedom.org/) coming up the escalator. Eben and the SFLC were critical in guiding the Joomla team through a process littered with potential land mines. Joomla! also received support from [VA Software](http://www.vasoftware.com/) who donated hardware, software ([SourceForge Enterprise Edition](http://www.vasoftware.com/sourceforge/index.php)) and hosting services for the new [Joomla Forge](http://developer.joomla.org). [Rochen](http://www.rochenhost.com/) donated hosting for www.joomla.org and, before long, Joomla! and [Open Source Matters](http://www.opensourcematters.org), the holding organization for Joomla!, came were born.  

According to Mitch, nearly all of the core development team and much of the community, as well as many third party component developers have shifted over to the Joomla! side. Today the Joomla! project is thriving. The forums already have over 160,000 posts and are growing at a 1,100 per day pace. There are already 11,000 registered developers and 700 projects on Joomla Forge (just like the big [SourceForge](http://www.sf.net), many have not been started yet). One interesting project that is going on is to put a Joomla! front end on SourceForge using the new Web Services API. VA is helping with the initiative.  

[Packt publishing](http://www.packtpub.com/), who sells [Building Websites With Mambo](http://www.amazon.com/gp/product/1904811736/qid=1136410461/sr=8-1/ref=pd_bbs_1/104-8625054-6739149?n=507846&amp;s=books&amp;v=glance), is planning on publishing a similar Joomla! book. I have not recently talked to the Mambo team, which has reloaded their core team with new developers, but it does seem like Joomla! has the momentum of the two projects.  

Mitch talked a little about the new 1.1 release (due out soon). The key advancement of 1.1 will be full UTF-8 support. This feature trumped a bunch of other items on the roadmap because of the urgent need for supporting an extended character set. While the team was working in the core, they couldn't resist doing some deep refactoring and modernization of the code. Thanks to better code design, the new version of Joomla! is expected to be faster. Joomla! 1.1 also introduces the first steps of a database abstraction layer which will make it easier to run Joomla! on databases other than MySQL (Postgres will be supported soon with commercial databases like Oracle and SQLServer soon after). Templates will use the templating engine [patTemplate](http://www.php-tools.net/site.php?file=patTemplate/overview.xml) rather than simple PHP. Great, another tagging syntax to learn! 1.1 also brings a more sophisticated error handler.  

People hoping for user facing features like fine grained security, workflow, and versioning will have to wait for version 1.2 which looks like it is going to be huge. Interestingly, a lot of this code has already been written but Joomla! is being conservative about how much new stuff to release at a time to reduce the pain of upgrades. Support for PHP 5 will have to wait for Joomla! 2.0, a total rewrite which will probably be based on the [Zend Framework](http://www.zend.com/news/zendpr.php?id=109) to which Mitch's company [JamboWorks](http://www.jamboworks.com/) is contributing a security module.  

I asked if separating from Mambo gave the project more freedom to extend and modernize the application and Mitch did say that backwards compatibility with earlier versions of Mambo was a constraint that they are happy to be released of. I don't know if the team would have done the level of refactoring that they did if they were worried about a migration path. Also, I am sure that the feeling created by starting something new energized the team.  

During the talk, there were some references to some useful Joomla! resources:  

*   [The API site](http://api.joomla.org) was unveiled. This site uses the PHP library tool [phpDocumentor](http://www.phpdoc.org/) to automatically generate documentation based on comments (like Javadoc). The comments are a little thin right now but now that the API site is up, there will be more incentive to write good comments.  
    
*   The [JamboWorks Template Club](http://www.jamboworks.com/Join_the_JamboWorks_Template_Club/) is a membership based service which gives access to a collection of pre-made templates. There are currently 12 templates on the site and a new template will be added every month. There were some great examples in the demo. $75 per year gives you access to the whole collection.  
    
*   Boston PHP has just published a release candidate of [josCommerce](http://www.joscommerce.com/) which ports the popular [mosCommerce](http://mamboforge.net/projects/moscommerce/) eCommerce component to Joomla.  
    

  
