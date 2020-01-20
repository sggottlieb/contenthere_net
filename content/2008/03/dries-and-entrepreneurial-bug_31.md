Title: Dries and the Entrepreneurial Bug
Date: 2008-04-01T06:38:00.001Z
Modified: 2015-01-06T12:15:38.079Z
Category: misc
Tags: 
Slug: 2008/03/dries-and-entrepreneurial-bug_31
Authors: Seth Gottlieb

Dries Buytaert has an [announcement on his blog for another startup](http://buytaert.net/mollom-my-content-monitoring-startup) that he is working on called [Mollom](http://mollom.com/).  Mollom is a content monitoring service that is optimized for user generated content.  Beyond tracking and blocking comment spam, Mollom's goal is to rate the quality of content.  Mollom is now in public beta and free (as in beer).  Once out of beta, there will be a free simple version and a for-pay premium version.    
  
The technology works as a web service ([details here](http://mollom.com/how-mollom-works)).  When a comment or user generated post is submitted, your website sends it to Mollom.  Mollum will assess if it is likely to be spam.  If it is, Mollum sends back a CAPTCHA for the submitter to fill out.    
  
The service requires you to install a plugin into your CMS.  Drupal users can take advantage of a pre-built module.  There is also a Java library that can be integrated into Java CMS.  Everyone else must build their own plugin on top of the [Mollom Open API](http://mollom.com/api).  Hopefully, other CMS vendors and users of their platforms will build plugins and submit them to Mollom for distribution.  If Mollom takes off, a [WordPress](http://wordpress.com/) plugin can't be too far away.  
  
I will not try to dig too much into the dynamics between Mollom and [Acquia](http://www.acquia.com).  Dries explains that Acquia is his day job while Mollom is his spare-time, unfunded startup.  In his blog post, Dries mentions that Acquia will offer Mollom as part of their [Caliper project](http://acquia.com/projects/wiki/caliper).  I wouldn't say that Dries is doing this because he is bored.  He started the initiative with fellow student [Benjamin Schrauwen](http://schrauwen.info/benjamin/)  before the Acquia opportunity came along.  When he negotiated the Acquia job, he probably got permission to work on this.  As an Acquia investor, I would be a little concerned about Dries' commitment to their start-up.  But, given Dries' value to any Drupal-based business, I am sure that the VC's are willing to give him wide latitude.    
  
