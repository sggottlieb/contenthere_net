Title: Web content retention requirements
Date: 2010-09-13T20:59:00Z
Modified: 2015-01-06T12:16:17.339Z
Category: misc
Tags: selection
Slug: 2010/09/web-content-retention-requirements
Authors: Seth Gottlieb

During a recent web content management system selection project for a client in a highly regulated industry, I ran across a rather advanced content retention requirement that I have not seen before — at least not in web content management. This requirement was also new to the vendors that we were working with. I am curious if anyone has encountered a similar requirement and, if so, how it was satisfied. 

  

The general gist is that the client does not want to retain outdated versions of assets outside of its mandated retention window of ten years. I am familiar with requirements for purging _assets_ based on particular rules but _versions of assets_. Here is the scenario:

  

### Purge old versions

  
>    
> 
> A monthly process searches through the content repository and deletes the following:
>   
> 
> *   __Unpublished or replaced versions of assets that have been not been on the site for ten (10) years.__  
>     
> *   Entire assets that have been removed from the site greater than ten (10) years ago.
> 
>   
> 
> Based on these rules, the following items are deleted on June 1st 2020:
>   
> 
> *   __A version of the terms of service that was superseded by another version on June 1st 2010.__  
>     
> *   A promotional block (and all versions) that expired on June 1st 2010.  
>     
> *   An article (and all versions) that was archived on June 1st 2010.
> 
>   
> 
> Purged assets and versions of assets are not recoverable by any means.
>   
>   

I first wondered why I had not run into this requirement before. I rarely see content retention requirements in web content management. Retention is more of an issue when it comes to email archiving and records management. Is purging old content necessary for WCM? Is it reasonable for WCM? One thing that makes web content different from these other forms of content management is that web content is deliberately _published_ to an audience whereas other content may contain private communications between individuals. Consequently, a company should have greater confidence in their web content as being official corporate information. Furthermore, once something is published, it is out there. Infinite copies are made. Destroying the original won't make a difference.  

My second thought was about the feasibility of satisfying this requirement. It strikes me that in order to meet this requirement, the CMS's API must support the ability to query and manipulate versions of assets. The CMS should also record the archival date (the date that the version was superseded by a following version) of each version. Otherwise queries may have to look at the publish date of the following version to determine the archival date of a version.

  

If you have experience or ideas on this issue, I would love to hear from you in the comments or via email (seth at contenthere.net)
