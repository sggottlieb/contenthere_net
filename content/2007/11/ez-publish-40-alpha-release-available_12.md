Title: eZ publish 4.0 Alpha release available
Date: 2007-11-04T10:26:00.002Z
Modified: 2015-01-06T11:32:50.965Z
Category: misc
Tags: 
Slug: 2007/11/ez-publish-40-alpha-release-available_12
Authors: Seth Gottlieb

eZ Systems [recently announced the alpha release of eZ publish version 4](http://ez.no/company/news/new_ez_publish_releases_include_php_5_support_and_the_ez_find_search_engine_extension).  If you are pleased with with eZ Publish's functionality, but your in-house PHP programmers are turning up their noses for its lack of PHP5 support, this will be some welcome news.   
  
eZ's earlier stance was to move ahead with functional improvements before making the platform PHP5 compatible.  However, having addressed some usability concerns with their in context "Web-In" interface, eZ turned their sights towards PHP5 support which several other PHP based WCM platforms (such as [Drupal](http://drupal.org), [None](http://www.modxcms.com/), [TYPO3](http://typo3.org), [Modx](http://www.modxcms.com/) and [SilverStripe](http://www.silverstripe.com/)) already have.  [Joomla!](http://joomla.org) does not anticipate PHP5 compatibility until release 2.0 (Joomla! just announced a release candidate of version 1.5 so 2.0 may be a ways off).   
  
Part of the process of adopting PHP5 is the migration of eZ Publish onto their PHP framework [eZ Components](http://ez.no/ezcomponents).  This will bring the products closer together technically to allow the same development effort to improve them both. All the eZ Publish installs will help test eZ Components.  Code in eZ Publish that is redundant with code in the eZ Components framework will not be maintained in future releases.   
  
While the PHP5 move is big, it won't have much impact on most developers.  Most basic eZ Publish implementation work is done in their templating language that effectively abstracts PHP code out of the presentation layer.  On the plus side, however, early reports indicate that adoption of PHP 5 has improved performance considerabely.  Readers may recall [my reporting](http://contenthere.blogspot.com/2006/09/ez-publish-38-review.html) that performance was quite slow without optimization.
