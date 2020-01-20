Title: Hippo Launches Hippo CMS 7.0
Date: 2009-01-26T17:52:00Z
Modified: 2015-01-06T12:15:40.897Z
Category: misc
Tags: hippo
Slug: 2009/01/hippo-launches-hippo-cms-70
Authors: Seth Gottlieb

[It's official](http://www.onehippo.com/en/news,2009/01/Open-source-vendor-Hippo-launches-Hippo-CMS-versio.html). [Version 7](http://www.onehippo.org), a near-total rewrite of Hippo CMS, is now GA.  Hippo CMS 7, formerly called ECM 1.0, is based on newer technologies [Apache Wicket](http://wicket.apache.org/) and [JackRabbit](http://jackrabbit.apache.org/).  This new architecture gets Hippo off of the complicated, difficult to learn [Cocoon framework](http://cocoon.apache.org/) and the retired [Apache Slide](http://jakarta.apache.org/slide/) project.  
  
One thing that I particularly like is that they have achieved a [compromise between the JCR's inherent hierarchical organization and a more free form faceted navigation](http://www.onehippo.org/about/docs_guide/orphans/hippo-ecm-concepts/facets/facetsearch.html).  Hippo CMS 7 is designed for high content volume websites and shows a lot of thinking in this area.  The faceted filters can be used at the API level by developers building websites on the platform.  Unfortunately, this functionality has not yet been surfaced in the user interface.  
  
As with earlier versions of Hippo, version 7's architecture has a clean separation between the repository, the management application and the front end delivery tier.  Hippo CMS 7 gives developers a bit more of a starting point for building a front end website by shipping with a JSP tag library refers to display components managed in the CMS.   Developers are still free to roll their own delivery tier using whatever display technology they choose.  The standards-based Java Content Repository, plus frameworks like [Sling](http://incubator.apache.org/sling/site/index.html), will make custom Hippo powered websites easier to build.  
  
  
  
Hippo CMS 7 has a plugins framework that facilitates adding new functionality to the platform.  There [Hippo Forge site](http://forge.onehippo.org) will be a place for the community to share their components and tools.  These plugins surface on the dashboard and in other areas of UI and are better encapsulated than Hippo 6.x customizations.  
  
<a href="http://www.flickr.com/photos/38298452@N00/3229154322" title="View 'hippo7-edit-blg' on Flickr.com"><img alt="hippo7-edit-blg" border="0" height="361" src="http://farm4.static.flickr.com/3523/3229154322_cf76a56813.jpg" width="500"/></a>  
  
On the UI side, Hippo CMS 7 shares some basic concepts with earlier versions of the platform.  Version 6.x users will recognize the stateful tabs but will appreciate a new three column layout that allows a user to browse the repository and edit multiple content items at once (see screenshot).  There are several other AJAX-enabled goodies like type-ahead search and linking and image placement through drag and drop.  If you have seen Day's new CQ5 UI, there are some similarities there.  In fact, an alpha of Hippo CMS 7 won second place in the Web Idol demo competition at the [jboye08 conference last November](http://jboye08.dk/).  Hippo has plans to create specialized versions of the user interface to optimize the usability for specific user segments.  For example, they are working on a user interface view that is optimized for power users on wide-screen displays that will maximize the use of the multi-column layout.  
  
Being a new product, there only 2 customers live on Hippo CMS 7.  Two more implementations are in progress.  The documentation is not going to win Pulitzer but I have found the mailing lists to be very helpful.  If you like what you see, I would recommend setting up some kind of arrangement with the Hippo team where they work closely with your implementation and they can submit fixes/improvements back into the core.  Current 6.x customers will be supported by a dedicated V6 team who will maintain the platform with fixes and minor enhancements.  No new support contracts will be sold for V6.  
  
This is a big release for Hippo CMS.  Usability-wise, there are significant improvements - particularly for power users managing large content repositories.  Architecturally, CMS 7 offers a more modern technology stack that flattens the learning curve and enables more efficient development of the product.  With a couple of successful implementations on the 7.x series, Hippo CMS may get it some deserved attention (particularly in North America where it is not widely known).
