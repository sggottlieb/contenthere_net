Title: Planning for Localization
Date: 2012-04-03T09:53:00Z
Modified: 2015-01-06T12:30:24.216Z
Category: misc
Tags: localization, Global Marketing Operations, architecture
Slug: 2012/04/planning-for-localization
Authors: Seth Gottlieb

Localization can be an elusive requirement for a website. During the platform selection process, internationalization is often listed as a "strong" requirement. Why wouldn't you want the ability to reach new markets? Then, during the implementation process, localizing gets downgraded as a "nice to have" or "future" requirement as time and resources dwindle and compromises need to be made to launch the primary language site. Eventually, localization becomes an "oh crap" requirement when someone expects to have a "Spanish version of the site up ASAP". After all, localization _was_ part of the business case and a key selling point of the platform. Yes, localizing the site would have been as easy as hiring translators _if only_ some accommodations had been made during initial implementation. But they were not. Hence the "oh crap."

  
  

While you may not have budget to localize your website during your initial CMS implementation, following these steps will make adding a new language easier down the road.

  
  

  
2.   __Learn how internationalization works on your platform.__   
     
    
    Different platforms have different approaches and best practices for internationalization. If you make the modest investment to fully understand these techniques, you will at least make educated decisions about how to defer localization and not rule it out. If you are working with a systems integrator, which I highly recommend, make sure they have experience building (and maintaining) localized websites on the platform.
    
      
    
3.   __Use the translation framework provided from the templating system.__   
     
    
    Any given web page will have a lot of static text that lives in templates (as opposed to in the content). For example, there might be a label on the upper right that says "search" or a copyright statement on the bottom of the page. It is not practical to manage these little "content crumbs" through your usual editorial workflow — they are small, numerous, easy to lose track of, and rarely change. But if you are planning on localizing your site, you don't want those strings in your templates either. It is much better manage these strings separately in "resource" or "message" files that can be shipped off to translators. Most templating languages come with a system for invoking externally managed strings. For example, in JSP Standard Tag Library, translated strings are invoked like this:
    
      
     <code><br/>        &lt;fmt:message key="some.text"/&gt;<br/> </code>  
    
    
    In eZ Publish they look like this:
    
      
     <code><br/>        {"Some text you are going to translate"|i18n('design/standard/node')}<br/> </code>  
    
    
    Setting this up is easy enough to do when you are building out your templates for the first time. However, it is very tedious to retrofit old mono-lingual templates with this system. You wind up doing it for templates that are no longer used "just in case." Worse of all, you have to visually re-inspect every pixel of the site because you are touching nearly every line of view code.
    
      
    
4.   __Keep text out of images.__   
     
    
    Having text in images adds a lot of friction to the localization process. First, you must remember to keep the image source files on-hand so you can produce the translated versions. Second, the translation process goes through additional steps of extracting and then re-imported the localized text. Managing all of those image files can be a real pain too. It is much better to float text over image backgrounds for buttons, navigation, and slides. Incidentally, applying this practice will also help with SEO and accessibility.
    
      
    
5.   __Make room for other languages.__ 
    
    Think as your primary language as the first of several languages when you are designing your content repository and defining roles and workflows. These localized content collections need a place to live. They will need access control so that a local team can safely work in their content without risking the overall content repository. Pay special attention to how "global" reusable content components are managed and retrieved.
    
      
    
6.   __Buy your top level domains NOW.__ 
    
    If you will be publishing your sites to different markets, start working on acquiring those top level domains (like .fr or .es). It will be really embarrassing to enter into a new market only to find someone else squatting on your domain.
    
      
    
7.   __Set the appropriate character encoding__  
    
    
    Most of the time this is a non-issue because most modern technologies default to UTF-8. Just make sure that you set up your databases with UTF-8 encoding and collation. Some older versions of programming languages require adjustments when dealing with Unicode too.
    
      
    

  

If you think localization may be in your future, plan for it now. Take the additional steps to reduce rework and risk when you are under the gun to get that new language published. If you didn't follow this advice, I would look into [translation proxies](http://www.contenthere.net/2012/02/introduction-to-translation-proxies.html).
