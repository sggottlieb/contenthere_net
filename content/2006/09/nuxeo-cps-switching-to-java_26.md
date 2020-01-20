Title: Nuxeo CPS Switching to Java
Date: 2006-09-21T08:21:00.002Z
Modified: 2015-01-06T11:32:47.580Z
Category: misc
Tags: 
Slug: 2006/09/nuxeo-cps-switching-to-java_26
Authors: Seth Gottlieb

Stefane Fermigier from [Nuxeo](http://www.nuxeo.com) just announced on the CPS user list that Nuxeo is switching over from Python/Zope to Java technologies.  Here is the content of the email:  
  
>    
> Hi all,  
>   
> here is an announcement that will come as a surprise: Nuxeo is switching to Java technologies for its upcoming product line.  
>   
> As you know (http://blogs.nuxeo.com/sections/blogs/eric\_barroca/2006\_04\_26\_open-source-ecm-cps-platform-4-yellowcake-teaser), we have started 6 months ago to include Java technologies into CPS. This solution is satisfactory for our current needs, but we need to think about the future. We had started to study several technological options for CPS' future, including comparing the progressive migration to Zope 3 (the path we had chosen initially) with a 100% pure Java option.  
>   
> Our final analysis is that switching to Java, if you take into account the respective maturities of the Java EE open source and Zope 3 platforms, will be easier and provide more value than a switch to Zope 3.  
>   
> We also think that with Java 5, modern IDEs like Eclipse, and with all the open source ecosystem that has appeared on Java since the last 5 years, it is much more enjoyable to develop in Java than it used to be 5 years ago when we started.  
>   
> We have discussed this choice with some of our partners and customers, and they all support us in this decision. Jean-Marc Orliaguet has also agreed with this strategy, has started porting CPSSkins to Java, and will join us next week in Paris for a sprint on the Web part of the project.  
>   
> The next version of CPS will be called "Nuxeo 5". You will find there all the key features of CPS, a modern architecture based on extensible components and services, and scalability and integration options that were not possible with a "pure Python" architecture.  
>   
> Please check the following FAQ:  
>   
> <http://www.nuxeo.org/about/java-switch>  
>   
> Here is the roadmap for the project:  
> [  
> http://www.nuxeo.org/about/roadmap](http://www.nuxeo.org/about/roadmap)  
>   
> More information:  
>   
> - The new webste: http://www.nuxeo.org/  
> - The code base: http://svn.nuxeo.org/trac/nuxeo  
> - The developers mailing list: http://lists.nuxeo.com/mailman/listinfo/ecm  
>   
> If you would like to join us in this new endeavor, please join the list.  
>   
> If you want to stay in the Zope world, it's your legitimate right and a sensible choice if CPS (or other Zope-based platforms) fit 100% of your needs. The CPS mailing lists will stay open and our team is still available for the time we will keep on supporting CPS, that is 3 years (at least).  
>   
> If you have questions, please start by reading the FAQ.  
>   
> Thank you, hopefully, for your support.  
>   
>  S.  
>   
This is really interesting news.  Nuxeo CPS is very popular in France and Nuxeo has made large contributions to the Zope community and had grand plans for Zope 3 with their [Z3ECM project](http://www.z3lab.org/sections/front-page/announcements/zope3-ecm-project).  This move appears to come from left field.  CPS is a very mature project with a solid install base.  The port to Java is going to be very disruptive.  It is possible that Nuxeo was feeling pressure from [Alfresco](http://www.alfresco.com).  Nuxeo was justifiably irritated when [Alfresco](http://www.alfresco.com) jumped into the marketplace claiming to be the first open source ECM out there when CPS had been out there for years and actually was delivering on the different aspects of ECM: web content management, document management, digital asset management.  CPS is still well ahead of Alfresco when it comes to non-file based functionality.  
  
So does this mean that "Enterprise" is just a synonym for "Java?"  My experience is that many large organizations have standardized on Java and are uncomfortable about shaking things up.  Alternative technologies (PHP, Python, Ruby) appear to be acceptable for new, experimental, or experimental initiatives but less so for core services like how a company manages its internal assets.  I am wondering if Nuxeo was getting that kind of feedback.  
  
__\[Note: All companies do not think this way. Thankfully, companies like [Google](http://www.google.com) and [37signals](http://37signals.com) don't. Otherwise, they would not be able to innovate at the pace that they do. But this does seem to be the opinion of the majority of companies that try to stay away from the bleeding edge.\]__
