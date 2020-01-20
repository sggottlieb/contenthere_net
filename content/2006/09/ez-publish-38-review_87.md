Title: eZ publish 3.8 Review
Date: 2006-09-27T22:51:00.002Z
Modified: 2015-01-06T11:32:47.664Z
Category: misc
Tags: eZ Publish
Slug: 2006/09/ez-publish-38-review_87
Authors: Seth Gottlieb

[Authors Note:  This is a derivative work of a white paper written by me and published by Optaros called "Content Management Problems and Open Source Solutions."  For more information on the original report, read [here](http://contenthere.blogspot.com/2006/01/content-management-problems-and-open.html).  Rather than try to republish the whole report, I am going to post updated reviews here.  The general concept is the same: group systems by how they are most frequently used.  Describe them in terms of Content Structure and Editing, Management, Presentation and Layout, Community and Support, Roadmap and Vision.  I also rate things like resources available.  The ratings are still in terms of below average (*), average (***), or above average(****).  I am also trying something with microformats in my brief assessments of the resources available.  Next up, will be Magnolia which I have been wanting to review for a long time.]

<table class="review-table"><tr> <th width="20%"></th> <th width="80%"></th></tr><br/><tr> <td class="review-category">Version Reviewed</td> <td class="review-result">eZ publish version 3.8.3</td></tr><tr><br/> <td class="review-category">Most common use</td><br/> <td class="review-result">Informational Brochure Site</td><br/></tr><br/><tr><br/> <td class="review-category">Also used</td><br/> <td class="review-result">News site, eCommerce</td><br/></tr><br/><tr><br/> <td class="review-category">Architecture</td><br/> <td class="review-result">Lamp</td><br/></tr><br/><tr><br/> <td class="review-category">Organization</td><br/> <td class="review-result">Development controlled and supported by eZ systems</td><br/></tr><br/><tr><br/> <td class="review-category">License</td><br/> <td class="review-result">Dual GPL/Commercial</td><br/></tr><br/><tr><br/> <td class="review-category">Resources</td><br/> <td class="review-result">Books:<br/> <ul><li class="hReview"><span class="item"><a class="url fn" href="http://ez.no/products/books/ez_publish_basics">eZ publish basics</a></span>. Rating: <abbr class="rating" title="3.0">*****</abbr></li></ul></td></tr></table>

 

<div class="description">This book is published by eZ systems and is the basis for their training and certification program.  It is easy to read and very strong on the basic concepts.  However, it is thin on advanced development topics.</div>

  
 

<li class="hReview"><span class="item"><a class="url fn" href="http://www.amazon.com/gp/redirect.html?ie=UTF8&amp;location=http%3A%2F%2Fwww.amazon.com%2FLearning-publish-Management-Solutions-Leaders-PHP-based%2Fdp%2F1904811019&amp;tag=contenthere-20&amp;linkCode=ur2&amp;camp=1789&amp;creative=9325">Learning eZ publish 3: Building Content Management Solutions</a></span>. Rating:<abbr class="rating" title="3.0">***</abbr></li>

<div class="description">This book is somewhat outdated.  It is targeted toward a more technical audience and addresses more advanced topics.</div>

  
   
  Training:   
<ul><li class="hReview"><span class="item"><a class="url fn" href="http://ez.no/services/training">eZ publish just started offering training in North America and has a certified developers program.</a></span>  Rating:<abbr class="rating" title="3.0">*****</abbr></li></ul>

<div class="description">The certification program is new but off to a good start.  The test was hard.</div>

  
  Online Documentation:  
<ul><li class="hReview"><span class="item"><a class="url fn" href="http://ez.no/doc/ez_publish/technical_manual/3_8">Technical Manual.</a></span>  Rating:<abbr class="rating" title="3.0">*****</abbr></li></ul>

<div class="description">Much improved over earlier versions.  Good API reference.</div>

  
   
  User Forums:  
 <ul><br/> <li class="hReview"><span class="item"><a class="url fn" href="http://ez.no/community/forum/developer">User Forums</a></span>  Rating:<abbr class="rating" title="3.0">*****</abbr></li></ul>

<div class="description">Very active and helpful.</div>

  
   
  
  
   

## Overview

  

eZ publish is a commercially-supported, dual license web content management system written in PHP by Norway-based eZ systems. The GPL and commercial licensed version of the software are identical. Most end users can use the GPL version unless they intend to resell or OEM the software. eZ publish has many reference sites including ecommerce, educational, interactive media, and corporate web sites. Development of the core product is closely managed by eZ Systems with the community contributing extensions and patches that may later be incorporated into the core product. eZ publish does not have the grassroots development community that Joomla!, TYPO3, and Drupal have. Perhaps this is because this is a commercial open source project, not a community driven project. However, In addition to eZ systems, which licenses and supports the product, there is a large partner network that provides integration and training services. eZ systems is also having an impact on the general PHP community with their introduction of eZ components which competes with the new Zend Framework and more established frameworks such as Symfony and CakePHP as a standard framework for building PHP applications. If eZ components is successful, the population of developers that are familiar with the technology concepts behind eZ publish, such as the templating framework, will increase.  

Architecturally, eZ publish is well designed and extensible with a nice separation between business logic (implemented as modules) and presentation (implemented as views in eZ publish's templating language). There is good support for pure content management features such as versioning, localization, and single sourcing. In addition to the content module, which handles all the content management services, and other modules, such as the user module and the web shop module, developers can create custom modules to work within the framework. The contributions section of the eZ systems website has a decent library of modules for free download.   

The administrative user interface can be a little overwhelming for non-technical, un-initiated users. This may be a reflection of eZ publish's purist approach to content management with notions of content classes and objects and node hierarchy, strong versioning, and translation. The administrative interface definitely makes the user feel like he is managing an application rather than just editing a website.

  
  

## Content Structure and Editing

  

eZ publish ships with several basic content types such as articles and various binary formats and as well as complex content types, such as a company (that could be used to support a feature like a partner directory) and a product. Content types can be defined at run time through the management UI by creating classes from attributes based on roughly 30 pre-defined datatypes (such as text, selection, xml block). Each of these datatypes has an associated editing widget so the content editing forms are built dynamically based on the composition of the content type. Certain datatypes can be designated as information collectors which allows a content class to represent form that external users can use to submit information (like a contact form). Collected information is stored in the database and is accessible through the management UI where it can be exported to various text formats.  

The XML block datatype is used to store user formatted text for free-text areas.   
Content stored in these attributes is actually stored an XML markup rather than plain HTML. For example, rather than using an &lt;H1&gt; HTML tag, eZ publish requires a user to use &lt;heading level=â€1â€&gt;. The Online Editor (now bundled with the basic eZ publish package) gives the user a WYSIWYG form control so he does not have to be aware of the XML based content behind the scenes. There are a couple of trade-offs associated with this design. On the negative side, it locks eZ publish into a single editor whereas other CMS can use any of several open source, or even  
 closed-source editors. Standard HTML editors allow the user to turn them off and paste complex HTML from other sources directly without an editor interpreting and possibly interfering with the original source. Still, the Online Editor seems stable and handles pasted text reasonably well. Also on the negative side, all this XML transformation may contribute to eZ publish's hunger for computing power. On the positive side, storing content in more structured XML increases the system's understanding of and potential to reuse the content. For example, eZ publish is aware of every link entered into an XML block field and has a features which checks for internal and external broken links.  

In eZ publish, a page on a website has two components: the node or location, which places the content the site hierarchy; and the actual content object that stores the content. This design allows a single piece of content to be used in several places on the website. This feature is very useful for situations like having a news folder with all the news articles and then promoting certain articles on the home page. Another use is to have content type which represents a "promotion" and placing that promo on different areas of the site. Content objects are not associated to nodes until they are published. This can be confusing because it means that unpublished pages do not appear on the page tree of the administrative interface. They appear as drafts on the user's my drafts page. 

  
  

## Management

  

eZ publish does not support an in-site editing model where a user can navigate through the site and click on an icon to make an edit. Instead, eZ publish has a management interface that is standard (although it can be modified, most customers do not) and is kept totally separate from the visitor facing website. The management interface is what a system administrator would expect to see in an administrative interface: lots of control and an engineers logical view of the content. However, this view goes over the head of a non-technical, untrained content author or editor. There is the capability to turn off sections of the user interface but all those sections are really needed to navigate and edit the content. If you deploy eZ publish, expect to train your non-technical users on a bit of content management theory and how to execute basic tasks. Once the initial learning curve is conquered, they will probably appreciate the control that the UI affords. 

The architecture of keeping the management interface separate from the visitor view is controlled by a system called "siteaccess." Each siteaccess is a set of configurations that control what design is used and what content is being managed. Typically, a website will have one siteaccess for the administration interface and another siteaccess for the visitor facing website. These two siteaccesses share the same content but have a different design templates. The same mechanism could be used to support several co-branded websites with the same content or several totally independent websites each with their own administrative interfaces. Some of the major hosting companies that deal with eZ publish have many websites running on the same eZ publish instance.  

eZ publish has a very strong versioning and translation system. Each content object can have different versions (called "drafts" until they are "published" and "archived" if they are replaced by a newer published version). Content can be rolled back by copying an older version forward and publishing the copied version. By default, eZ publish will save 10 versions of a content object but that setting is configurable. Each version can have one or more translations. In this way, different translations of the same content object can be kept in sync. Different language versions of the same website are controlled by the siteaccess framework in which a primary language and fall back languages are set.   

eZ publish comes with a very basic two-step workflow that can be extended by adding events (written in PHP) that affect the state of the asset and also can trigger additional functionality. Extending workflow is generally considered one of the more challenging customizations to make in eZ publish. Most customers stick with the basics.  

The eZ publish access control system is very powerful and secure. Access is controlled by granting roles (bundles of policies which grant access with various limitations) to users or groups. Policies can be associated to sections of the site or branches of the node hierarchy. Groups can contain users or other sub groups. 

  

## Presentation and Layout

  

For the most easy to satisfy customers, the installation process includes a set of pre-built themes that can be modified through the UI (such as the type of navigation style, etc). However, most customers (especially if they are using eZ publish for their corporate identity site) will want to do in depth customization to the presentation templates. The method of doing this is to follow a model of template overrides. When rendering a page, the templating engine looks in the design folders specified by the siteaccess for the appropriate template and then falls back to the standard design if the appropriate templates are not found. Changing things like the overall page layout involves copying templates from the standard or other designs into the appropriate design folder and making modifications.   

There is also a system for creating rules that determine what templates are selected. These rules can be based on the content type (or datatype), the section of the site, the original template that would have been used, or the individual node id. The rules are defined in a configuration file. Although the management interface theoretically could control these rules, it is so unusable that it is best to just edit the file.  

The actual syntax that is used to develop templates is based on the [Smarty PHP templating engine](http://smarty.php.net/). The general concepts and much of the syntax are similar but, at the time eZ systems was considering Smarty, it was too primitive for their needs so they pushed ahead with their own templating language. Since that time both Smarty and eZ publishes templating system have evolved, sometimes in similar ways. If a developer knows Smarty, eZ will look very familiar. In fact, if you have Smarty based text highlighting rules in your text editor, they will work nicely with eZ publish templates. The templating engine is also part of eZ components so it will compete with Smarty to be used in other open source projects or custom web applications. The eZ publish templating framework rigidly separates layout from application logic. There is no way to write PHP code in a "scriplet" as can be done with some other templating frameworks. Anything resembling programming logic must be created as an "operator" which can be registered with the templating framework. eZ ships with most of, if not all, the operators you need to build a site such as comparing values, converting strings, and extracting data from content objects. Tags like "foreach" and "if" dictate control flow.   

eZ publish manages two sets of URLs: the system URL, which is of the format \[module\]/\[view\]/parameters (for example, /content/view/12 to view node 12) and the search engine friendly "virtual URLs" that are automatically managed by the system based on the name of the node (example: "/about") and manually managed by manual overrides (this is handy if you are migrating a site onto eZ publish and your URLs change).  

The presentation supports three level of caching: view caching, template caching, and static caching. View caching caches the output of the view (usually in the central well of the page), template caching stores compiled PHP code (generated from interpreting the templates) that is optimized by using "cache-block" statements in the page templates. Static cache stores rendered static HTML on the file system  
 for rapid access. When you configure static cache, you tell it under what conditions to refresh the cache. Additionally, eZ publish (for good reasons) recommends the use of a PHP accelerator, such as APC, that stores PHP code in memory and greatly improves execution latency caused by disk I/O.   

Turning off caching (necessary if you are doing development) reveals why there is so much caching built into the architecture. eZ publish is _slow_. Several factors contribute to this: the abstraction of the templating framework; conversion of XML blocks to HTML; the highly normalized and complex data model which supports user defined content classes, versioning, and translations; and the template override system. Just because eZ publish is written in PHP, do not think that it can be run on an inexpensive $20 per month virtual Linux server.   
Still, caching, plus eZ publishes support for clustering (enhanced in version 3.8) make eZ publish capable of supporting very high traffic websites.   

  

## Community and Support

  

Over the past few months, the documentation, especially for the 3.8 release has improved dramatically. However, if you get stuck, the best place to start with an eZ publish question is the forums, which are extremely active and have a searchable archive. The lists are moderated, so almost all questions get answered, although sometimes there is a delay between the question and the answer. There are several extremely active forum contributors that are credited with hundreds of posts. eZ systems also leverages blogs and RSS for community outreach.  

Recently eZ systems has stepped up its presence in North America. After establishing an office in Vancouver and seeding it with some senior staff, eZ systems is building its North American partner program with lots of outreach and programs including training and partner events. eZ systems looks to partners for system implementation/integration work and bases its own revenue on support and value-add modules that it sells. eZ systems sells a network product that can be installed on a production instance to check for compliance, monitor its health, send updates, and be used by eZ systems support for issue diagnosis.   

## Roadmap/Vision

  

eZ systems follows a release schedule of every 6 months. The most recent release was mostly architectural including better support for clustering. The next major release will be more features based. eZ publish still does not support PHP 5 and there are no immediate plans to do so. However, this is not so much of a problem as eZ systems employs one of the top committers on the 4.x PHP series.
