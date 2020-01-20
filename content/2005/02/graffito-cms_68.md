Title: Graffito CMS
Date: 2005-02-15T13:55:00.002Z
Modified: 2015-01-06T11:32:13.707Z
Category: misc
Tags: 
Slug: 2005/02/graffito-cms_68
Authors: Seth Gottlieb

I recently started tracking the [Graffito project](http://incubator.apache.org/graffito/). Graffito is a very early stage open source Java-based CMS project being incubated by the [Apache Software Foundation](http://www.apache.org). What interests me the most about Graffito is that it seems to be the answer to a need that I have been hearing a lot recently: a Java-based CMS that integrates into an existing presentation tier.   

Graffito is a set of components that can work with different repositories and integrate with other various Java based presentation layers. Graffito provides functionality that people need out of a CMS:  

*   A repository abstraction layer which gives a common API to access content (documents, folders, etc.) from a relational database (through OJB), WebDav (such as Slide), or a JCR based repository. Currently, the OJB connector is the only one that has been implemented.  
    
*   Concurrency management so that multiple users do not interfere with each others work.  
    
*   Security  
    
*   Content integration which can integrate content from multiple repositories into one tree  
    
*   Workflow  
    

  

Graffito is closely tied to and integrates with [Jetspeed 2](http://portals.apache.org/jetspeed-2/), which is one of the Apache portal projects. I have a feeling that Jetspeed 2 may give Graffito some momentum as Jetspeed 2 users look for a CMS to put content on their portals.  

Recently the Graffito project [website](http://incubator.apache.org/graffito/) has been showing lots of change. Broken links are being fixed and a lot of new information is being added. This should be a good project to watch if not participate in.
