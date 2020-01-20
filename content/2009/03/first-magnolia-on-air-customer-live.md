Title: First Magnolia On Air Customer Live
Date: 2009-03-04T11:03:00Z
Modified: 2015-01-06T12:15:58.819Z
Category: misc
Tags: magnolia
Slug: 2009/03/first-magnolia-on-air-customer-live
Authors: Seth Gottlieb

It looks like the first customer of [Magnolia's On Air platform](http://www.magnolia-cms.com/onair) is now live.  [RTSI](http://www.rsi.ch/home.html) is a Swiss radio and television company.  They are moving to On Air from a home grown system.  Eventually eight stations will be supported on the new platform.  
  
<a href="http://www.flickr.com/photos/sggottlieb/3129093136/" title="magnolia-onair-arch by sggottlieb, on Flickr"><img alt="magnolia-onair-arch" height="271" src="http://farm4.static.flickr.com/3125/3129093136_51d807b260.jpg" width="500"/></a>  
__Architecture diagram showing integration between Media Workflow Engine and Magnolia (please excuse the colors).__  
  
For those of you who are not familiar with On Air, it is an integration between [Magnolia CMS Enterprise Edition](http://www.magnolia-cms.com/home/products/enterprise.html)&nbsp;([reviewed here](http://www.contenthere.net/products-page/reports/open-source-web-content-management-in-magnolia)) and a third party product called Media Workflow Engine by FutureLabs.  MWE provides capture, workflow, and advanced (non-destructive) editing functionality for video, audio and images.  Images are represented in the Magnolia repository (the [Apache Jackrabbit](http://jackrabbit.apache.org) JCR implementation) as proxy objects.  This saves the Magnolia repository from becoming bloated with binary files.  Another nice feature of the integration is that workflows can be initiated in either system and can be continued in the other system.  For example, a visitor uploading a video to a site can kick off a workflow in MWE.
