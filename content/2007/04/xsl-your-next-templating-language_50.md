Title: XSL - Your Next Templating Language?
Date: 2007-04-03T12:39:00.002Z
Modified: 2015-01-06T11:32:49.857Z
Category: misc
Tags: 
Slug: 2007/04/xsl-your-next-templating-language_50
Authors: Seth Gottlieb

When you implement a web content management system, you usually do most of the development on the presentation tier.  Expect to spend 2/3 to 3/4 of your development time working on page templates.  (Also expect to spend double what you expect in content migration but that is the topic of [another post](http://contenthere.blogspot.com/2006/10/migrating-content.html)).  That is where you define the page layouts, the formatting of the content, and other visitor facing behavior.    
  
If you have implemented a number of WCM products, you know that most have have their own proprietary templating syntax or at least their own set of tags to use.  After a while you begin to realize that while the syntax varies, the core concepts are  common.  Most are designed on the assumption that a dynamic web page is actually mostly static with a few dynamic regions embedded within.   
  
As a result, the page template is mostly static HTML with a bit of code to retrieve and display dynamic content in the defined regions.  The proprietary tags (be they JSP tag libraries, XML tags, or scriptable objects) encapsulate the work of finding, retrieving, and formatting content from the underlying repository.  Some templating systems are stricter than others about keeping business logic out of the template code and forcing that logic to be embedded in more reusable objects.  For example, in the Java world, [FreeMarker](http://freemarker.sourceforge.net/) and [Velocity](http://velocity.apache.org/) deliberately limit what can be done in a presentation template.  JSP, with its ability to embed any Java code scriptlets, puts developers on the honor system.  
  
With this delineation, server side developers and web designers are able to keep from treading on each others toes.  There is a long standing process for implementing the presentation tier that goes like this:  graphic designers create page mockups in something like Adobe Photoshop; creative developers code the mockup in statich HTML (or DHTML); and then the server side developer embeds the objects and tags to replace the static example text and pictures with dynamic content.  Some templating syntaxes are supported by HTML editors (such as DreamWeaver) to facilitate round trips between server side developers and HTML developers.  With the appropriate plugins you can get code completion and other conveniences.  Zope's Tag Attribute Language (TAL) is nice because it does everything in extended attributes within regular HTML tags and that reduces the chances that the HTML editor will scramble the dynamic code.    
  
The common patterns, tool support, and the fact that you can orient yourself in the code by reading through the familiar HTML, make the traditional templating systems relatively easy to learn.  It's a great system that the majority of the industry has embraced.  It's great, I should say, until those bits that you expected to be static and unchanging start to change.  To make matters worse, they become variable in unexpected ways: by exception.  All of the sudden, someone from the business side wants to do a "small change just on a few pages."  Or it might be a global change like when a new browser comes out and HTML tricks that you used to be able to get away with start breaking pages.  Of course, these changes are urgent and need to be done yesterday.  You put in a hack like a temporary template expecting to fix it later.  However, you know that later you will be responding to some other urgent change.    
  
Even if you are clever about using server side includes, macros and other best practices, unless you constantly refactor your template code and actively manage the presentation tier, you will start to experience template proliferation.  At first, this seems like an acceptable price to pay for the ease of development.  Having lots of templates may not seem like such a problem if they are easy to read and edit.  For companies with small to medium sites and modest pressure to make special feature layouts, this might be totally acceptable.  But for large media sites with lots of content and lots of editors, things get out of control.  One of my clients had 7,000 templates.    
  
An alternative strategy is to use XSLT.  Unlike traditional web templating technologies, XSL templates build the whole page dynamically as a result tree and fragments can be overridden in a CSS kind of way (not exactly, but you get the idea).  So, if you want to override a section of static HTML markup in one area on the page,   in one section of the site, you do not have to write an alternative template out include that is identical but for that one difference.  The die-hard JSP guys out there are thinking "I wouldn't do that, I would write conditional logic around that little fragment."  You could.  But that makes the JSP harder to read and manage.  Think about how easy it is to have a media specific CSS style sheet for a print-only view that does a "display:none" for all the HTML classes and IDs that you don't want on the print version.  Contrast that with writing a bunch of JSP "if" statements around screen only HTML.      
  
Do not think that XSLT is all light and happiness.  There are several limitations that may rule out XSLT for you.  For example, XSL has nowhere near the tool support that traditional HTML based templating languages have.  Forget about WYSIWYG editors.    There are a couple of them out there but they are nowhere near as good as straight HTML editors.  Most HTML programmers get totally lost in XSL code.  XSL processors have traditionally been slower than other presentation systems that are optimized for request time response.  There are a couple of WCM systems that use XSL (commercial products like [Ingeniux](http://www.ingeniux.com/) and [Hannon Hill](http://www.hannonhill.com/) and the open source WCM [Apache Lenya](http://lenya.apache.org).  [Alfresco](http://www.alfresco.com) has an XSL templating option), but as one sales engineer said, they have had to sell <span style="font-style:italic;">around</span> this aspect of the product rather than highlight it.  Writing dynamic, request time logic for something like personalization is harder on a presentation tier built on XSLT.  [Apache Cocoon](http://cocoon.apache.org) is an XML web application framework designed to address this limitation but, for some reason, it has not getting a lot of attention lately.  
  
Still, I think that the tide is shifting on XSLT and here is why:  

*   Layout is now more driven by CSS. This does two things. First of all, the HTML is getting much simpler (no more nested tables for positioning) and semantically meaningful so the XSL will need to do less work. Second, the declarative style of CSS is similar to XSL so HTML programmers are more prepared to think in this way.  
    
*   With all of interest in AJAX, HTML developers are starting to get more comfortable with XML.  
    
*   XSL processors are getting faster.  
    
*   Also thanks to AJAX, you can have a statically deployed ("baked") HTML website with dynamic AJAX components layered in. Baking style presentation tiers are especially appropriate for XSLT.  
    
*   XML is becoming increasingly popular for data exchange and storage. You can't go to a content management conference without hearing the term XML in every presentation. Even large companies like [Content Here](http://contenthere.net) are using XML for content authoring :).   
    
*   Better browser support for XML may make client side XSLT rendering a reality soon.   
    
*   Architects are looking for standards and de-coupled architectures to reduce lock-in. Just as the JCR or any other standards based repository presents flexibility and an exit strategy, a presentation tier that uses XSLT will make it cheaper to move to another platform. All you need to do is get another platform that publishes XML and your page templates will still work.  
    

  
  
Depending on your need  
s, XSLT may not be appropriate for your architecture.  But if you are searching for a presentation tier to address problems in template proliferation and poor separation between business and display logic, you might consider it.
