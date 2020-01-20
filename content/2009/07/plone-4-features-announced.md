Title: Plone 4 Features Announced
Date: 2009-07-13T15:31:00Z
Modified: 2015-01-06T12:15:59.945Z
Category: misc
Tags: 
Slug: 2009/07/plone-4-features-announced
Authors: Seth Gottlieb

I was catching up on my blog reading and noticed that the [Plone](http://plone.org) community has [announced what features will be in Plone 4](http://plone.org/news/plone4-plips-accepted). Version 4 will incorporate 40 "PLIPs" ("Plone Improvement Proposal:" the Plone project's issue/enhancement tracking system). You can see the [list of enhancements and bug fixes here](http://dev.plone.org/plone/milestone/4.0). The release is expected to be completed in the end of 2009. 

  
While, to me, 4.0 seems like a less ambitious release than 3.0, a few features caught my eye:  

*   __Tiny MCE replaces Kupu as the default WYSIWYG editor__. From a user perspective, this is probably the most noticeable change. While a number of number rich text editors are supported through add-on modules ("Products"), Plone has been a bit of an outlier for using Kupu as the default, and best integrated editor. Plone has favored Kupu because of its simplicity and the well formed HTML that it produces. However, users tend to like all the buttons and additional formatting features offered by TinyMCE and FCK. TinyMCE is widely used as the standard editor in many open source and commercial CMSs. Plone will be in good company.  
    
*   __Cleaner handling of object references.__ Plone's repository (an object database) is hierarchical like the Java Content Repository. In most cases, business users like the similarity with the familiar filesystem model. However, like file systems, there is a disadvantage when you want the same item to appear in more than one place in the content tree. Like most hierarchical repository systems, Plone has developed a referencing system (like a symbolic link or a shortcut). Version 4.0 of Plone will make references cleaner and easier for non-technical users to use.  
    
*   __Delegated group management.__ Plone has a good system for managing groups and roles. However, to this point, only a site manager can control group membership. With this release, there can be group owners who manage membership for the groups that they own.  
    
*   __jQuery will be bundled.__ jQuery, the popular AJAX framework is becoming nearly ubiquitous. Now Plone will ship with it bundled into the basic install. From this, I expect to see lots of little UI optimizations in the upcoming releases. Of course this will be balanced with Plone's emphasis on accessibility.  
    
*   __Improvements to the self registration system.__ Plone can be configured to allow users to register to the site and be put into a pending status or become full blown members. 4.0 will have some enhancements to fine tune these configurations with more sophisticated behavior.  
    
*   __Better control over portlet visibility.__ Plone 4.0 will make is easier to configure rules that control when a portlet displays on page. For WordPress users, I think this is a little like [Widget Logic](http://freakytrigger.co.uk/wordpress-setup/). [Drupal](htt://drupal.org) users will recognize this as part of the blocks framework. Hopefully, Plone will not ask the user to implement the display logic in code.  
    
*   __New default theme__ Plone 4 is going to ship with a new default theme based on the newly redesigned plone.org site. This will affect intranet implementations (which tend to do less custom theming work) than external website implementations.  
    

  

Those are the big changes from what I can tell but I am sure that I am leaving things out. Please add any major oversights in the comments. 
