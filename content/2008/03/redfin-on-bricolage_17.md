Title: Redfin on Bricolage
Date: 2008-03-17T08:39:00.001Z
Modified: 2015-01-06T12:15:37.900Z
Category: misc
Tags: 
Slug: 2008/03/redfin-on-bricolage_17
Authors: Seth Gottlieb

There is a [good post](http://blog.redfin.com/devblog/2008/03/plumbing_upgrade_were_using_bricolage_for_content_management.html) on the [Redfin](http://www.redfin.com) blog about why they selected [Bricolage](http://bricolage.cc) to manage their website including why they broke down and implemented a CMS and why they chose Bricolage over [Alfresco](http://www.alfresco.com), [Drupal](http://drupal.org), [Joomla](http://joomla.org), [Mambo](http://www.mamboserver.com/), and [Plone](http://plone.org).  They also looked at [Interwoven](http://www.interwoven.com/), [RedDot](http://www.reddot.com/), and [CrownPeak](http://www.crownpeak.com/).  
  
Redfin was looking for a de-coupled CMS that would allow them to separate content publishing from updating website code.  Of the open source products that they looked at, only Alfresco and Bricolage could do static publishing (I don't think they came across the [CMFDeployment](http://plone.org/products/cmfdeployment) or [Enfold's Entransit](http://plone.org/products/entransit) project for Plone).    
  
What they didn't like about Alfresco was how index pages were generated.  They felt that they would need JSPs to dynamically render listing pages from directories of statically generated detail pages.  While listing pages can be statically generated through the same mechanism that renders detail pages, the fact that it happens at save time rather than publish time may have created performance problems if they had lots of composite pages.  
  
Their main concern with Bricolage was similar to what most non-periodical websites experience: that the user interface metaphor is highly specialized to publishing stories and related media.  Business users need to mentally map the terminology of the product to their own domain model.  They also found the branching model unintuitive.    
  
Overall, the Redfin development team is happy with their choice of Bricolage and it sounds like they will bring energy and expertise to the Bricolage community.
