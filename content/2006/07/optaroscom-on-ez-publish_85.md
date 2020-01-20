Title: optaros.com on eZ Publish
Date: 2006-07-12T08:06:00.002Z
Modified: 2015-01-06T11:32:18.728Z
Category: misc
Tags: eZ Publish
Slug: 2006/07/optaroscom-on-ez-publish_85
Authors: Seth Gottlieb

As is the case with most internal projects when staff utilization on client work is through the roof, our project to deploy www.optaros.com on eZ publish seemed to go on forever. But, thanks to some really dedicated individuals, we finally got the project over the line and we are [live](http://www.optaros.com). With our first CMS based release of www.optaros.com\[[1](#1)\], the retail view of the site does not change at all except for URL changes (except if you are a German speaker in which case you will be thrilled to know that the whole site [is translated into your favorite language](http://www.optaros.com/de))  

Being an internal project, a lot of people were involved during short bursts. I think in general, they found the eZ publish syntax easy to pick up given enough examples. Our business users had no trouble learning the user interface. Other features we like include easily configurable content classes (through the UI, you can create custom content classes) which we use heavily. Among the content classes we created were Partner Company, Person, Case Study, Promo, Career, and White Paper. This allows us to surface different pieces of content throughout the site with different views. For example, the same Person class is used to contain the information [here](http://www.optaros.com/en/company/leadership_team#Gottlieb) as [here](http://www.optaros.com/en/publications/white_papers_reports). Localization and Versioning are excellent. Also eZ publish has a nice way to handle multiple sites including different language translations of the same site or totally different sites. We could have done a domain based mapping (i.e. http://www.optaros.de rather thand http://www.optaros.com/de) but we decided against it for various reasons.  

One thing to be aware of when deploying an eZ publish site. Performance. Don't let the "PHP" fool you. eZ publish does a lot of work on the rendering side. If you look at the code, you can kind of guess why. There are lots of includes and text transformations. For example, when you have an HTML text area, it is really stored in XML so there is a view of that field that you have to invoke to render the XML as HTML. From an architectural perspective this is very nice. It means that you could override this view for a different device such as a PDA. However, if you want to host on really really cheap hardware (such as a virtual host with 256MB of RAM), this level of abstraction is costly on limited server resources. eZ publish has lots of tuning parameters. Some of the best documentation is on the eZ publish forum [here](http://ez.no/community/forum/setup_design/improving_ez_publish_environment_and_performance) and [here](http://ez.no/community/forum/general/ez_publish_performance_optimisation_faq). You definitely need a PHP accelerator such as [eAccelerator](http://eaccelerator.net/) or [APC](http://pecl.php.net/package/APC). You should configure template, view, and, if necessary, static caches. Still, hosting a dynamic ("fried", not "baked" as [Tony Byrne](http://www.cmswatch.com) would say) on really weak hardware is ambitious no matter what technology you are using.  

Overall, eZ publish was a good choice for this site. It might be for your as well but it all depends on your users. eZ publish does not have an in-site editing model. That is, there is a distinct back end for managing content and a front end for viewing content. This made sense to our users. They were able to map pages they saw on the "retail" side with the page tree on the management side. However, I have seen business users who want to edit the content that they see on the fron end right there. Some of the other CMS that do this nicely are: TYPO3, Lenya, Plone, and Joomla.   

  
Notes:  
  
<a name="1">1</a>: I know you are asking yourself, how could a company that Seth Gottlieb works for not have a Web CMS? Here are the answers.  

*   Most of the poeple in the company know HTML and source control. Our marketing person could usually find someone to make a text change.  
    
*   We do all the formatting in CSS. This allows us to make a formatting change in one place and have it reflected all over the site.  
    
*   We like to experiment with the design a lot. It is easier for a creative developer that can cut HTML code faster than you can use a word processor to work in static HTML than presentation templates.   
    

  

But now times are changing. We are around 60 people now and growing rapidly. Our marketing department needs direct control over the website without being dependent on consulting resources. We are publishing our site in multiple languages (French is coming out soon). We get all that from eZ publish.
