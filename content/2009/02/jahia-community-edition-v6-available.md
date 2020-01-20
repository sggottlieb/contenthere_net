Title: Jahia Community Edition V6 Available
Date: 2009-02-04T05:48:00Z
Modified: 2015-01-06T12:15:58.449Z
Category: misc
Tags: 
Slug: 2009/02/jahia-community-edition-v6-available
Authors: Seth Gottlieb

[Jahia](http://www.jahia.com) has some big news. As of today, V6 of their Community Edition is now available. This is a big release for Jahia on a number of levels. Architecturally, they have refactored the application to make it cleaner by removing [Jetspeed-2](http://portals.apache.org/jetspeed-2/) from the architecture. JSR 286 portlets are still supported through the [Apache Pluto portlet container](http://portals.apache.org/pluto/). More importantly, they have developed a framework for "pluggable repositories" where Jahia can now connect to content providers like a JCR or a file system (see screenshot). A new rules engine can be configured to do different actions on content depending on its type. For example: unzip an archive when it is uploaded. 

<a href="http://www.flickr.com/photos/38298452@N00/3251384576" title="View 'Jahia 6 File Manager' on Flickr.com"><img alt="Jahia 6 File Manager" border="0" height="437" src="http://farm4.static.flickr.com/3389/3251384576_6f4a436826.jpg" width="500"/></a>  
__The Jahia 6 File Manager has a Outlook-style tabbing scheme that allows you to browse multiple repositories__

  

There are plenty of new contributor features such as improved workflow, inline editing, and a preview feature where you can emulate preview for a specific user type on a specific date (see screenshot). There is also image cropping and scaling functionality built in. From a usability perspective, Jahia has aggressively adopted [Google Web Toolkit (GWT)](http://code.google.com/webtoolkit/) to AJAX-ify the user interface. There are now fewer popups and many other subtle improvements that lead to better user flow.   
<a href="http://www.flickr.com/photos/38298452@N00/3250607329" title="View 'Jahia 6 &quot;Preview as&quot;' on Flickr.com"><img alt='Jahia 6 "Preview as"' border="0" height="266" src="http://farm4.static.flickr.com/3387/3250607329_a02d697381.jpg" width="500"/></a>  
__Jahia 6 preview feature allows a contributor to emulate a specific user type and date.__

  

One of the biggest changes in Jahia 6 has to do with the licensing. Readers of my [Jahia 5 evaluation](http://www.contenthere.net/products-page/reports/open-source-web-content-management-in-jahia) know that I have been quite hard on Jahia for talking so much about open source but not offering a single open source product (their Community Edition had a non-OSI-certified badgeware license). Well, as of V6, Jahia Community Edition is licensed under the [GPL (V2)](http://www.gnu.org/licenses/gpl-2.0.html). Version 6 of the commercially licensed Enterprise Edition (due out this summer) is also going to have some licensing changes but I don't want to spoil the surprise. For now, you can try out the supportable, open source licensed Community Edition.  
