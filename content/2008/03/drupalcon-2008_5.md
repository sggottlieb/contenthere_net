Title: Drupalcon 2008
Date: 2008-03-05T11:38:00.001Z
Modified: 2015-01-06T11:32:51.886Z
Category: misc
Tags: 
Slug: 2008/03/drupalcon-2008_5
Authors: Seth Gottlieb

__\[Update: [here are the slides and the recorded presentation in case you couldn't be there](http://buytaert.net/state-of-drupal-presentation-march-2008)\]__  
  
![](http://media.contenthere.net/blgimages/drupalconScreen.png)  
I am back home in Florence after a couple days at [Drupalcon](http://boston2008.drupalcon.org/) and [AIIM](http://www.aiimexpo.com/aiimexpo2007/v42/index.cvn).  It was great to see all my colleagues at both events.  I didn't attend any of the AIIM sessions but I did catch a few of the Drupalcon talks.  Here are some quick notes and observations.    
  
Drupalcon was huge.  The attendance doubled from 400 last year in Barcelona to over 800 this year and there were people turned away because the venue was at capacity.  AIIM was also pretty well attended - at least on the Expo floor.    
  

#### [Drupal Usability](http://boston2008.drupalcon.org/session/report-formal-usability-testing-university-minnesota-libraries)

I arrived a little late and squeaked into the session "[Report from formal Drupal usability testing at the University of Minnesota Libraries](http://boston2008.drupalcon.org/session/report-formal-usability-testing-university-minnesota-libraries)," which reported results of non-Drupal users trying to do 7 tasks in Drupal.  The study looked very professional and well executed.  Unfortunately I missed Task 1 which most of the users got hung up on.  For more information, you can go to the [Drupal Usability Group](http://groups.drupal.org/usability) where there is already a nice discussion and the team plans to post the slides, video and other findings.    
  
At a high level, I think it was great that the Drupal community was able to do this.  No one was at all defensive and everyone seemed excited to fixed the problems uncovered.  They welcomed external criticism and that is a good characteristic of an open source project.      
  
Some of the specific points from my notes:  

*   Newbies are confused by the stuff that the pros just ignore.  
    
*   Help was not helpful.  
    
*   Even after tweaking of the terminology (less references to the word "node"), users are still confused.  
    
*   There needs to be a good glossary. There used to be one but it was removed  
    
*   There are too many options and that buries the important stuff.  
    
*   There should be tutorials.  
    
*   A common complaint was that users lost the page that they just created.  
    

  

#### Keynote

Dries did a good keynote on the state of Drupal (that is strong, by the way).  Some specific notes....  
  
Drupal 6 came out with February 16th, like previous Drupal releases, it was big.  The number of downloads over the first month doubled the first month (100,000 vs 50,000 for first month of Drupal 5).  There were 741  contributors (Drupal 5 had 472).  And several thousand more fix/enhancement patches than Drupal 5.  There are now 20,000 live Drupal 6 instances pinging home.    
  
Looking forward, the Drupal community wants to improve the project to make it ready for the next wave of adopters.  This includes addressing pain points like module compatibility and expanding Drupal's relevance.  One nice quote was "the Social Graph just connects people. we have the opp to build a graph that connects everything."  Dries went into a discussion of the semantic web and RDF and how Drupal could be a major player.  Not a lot of people can get away with promising about the semantic web.  I guess Dries is one of those people.  Here are some ideas:  
  
Web 1.0 = WCM  
Web 2.0 = Web 1.0 + user management + infinite extensibility  
Web 3.0 = Web 2.0 + infinite interoperability  
  
RDF is the way to achieve infinite interoperability and federated data sources.  In my opinion, Drupal is very weak in this area and in things like web services and REST style interfaces.  Drupal developers are very database oriented and tend to use MySQL replication to move data around rather than application to application APIs.  
  
Getting into specific features, Drupal faces the [same dilemma that Plone and every other content management system face](http://contenthere.blogspot.com/2008/02/plone-strategic-planning-session.html): is it a framework for developers or is it an application for business users?  Dries took a mathematical strategy to solving the problem.  A survey of the Drupal community found that 32% wanted to focus on end users of small to medium sites, 44% wanted to focus on enterprise users, and 24% wanted to focus on developers.  Out of that he concluded that Drupal 7 should have 70% user facing features and 30% developer oriented improvements.  It is a simple solution but I don't know if I buy it.  In particular, this approach makes it hard to do some of the major refactoring that projects sometimes have to do in order to prepare for a new set of features or reach a new market.    
  
Dries also predicted that Drupal 7 would be out October 15th 2008.  In the past the community had been very reluctant to put out target dates.  It will be nice to see them make this date that they set.  Having [Acquia](http://www.acquia.com) pushing things along and dedicating developers like they did with Drupal 6 will help.  
  
More robust testing practices were also mentioned.  There was talk about getting a testing framework into the core and establishing testing procedures.  This will help improve the quality of the code and make it easier for Drupal to get into more demanding IT organizations.  Better testing procedures will also make it easier for the contributor community to safely grow.  
  

#### [Drupal and the Knight Foundation](http://boston2008.drupalcon.org/session/drupal-and-knight-foundation)

The [Knight Foundation](http://www.knightfoundation.org/) is giving away a lot of money through the [News Challenge](http://www.newschallenge.org/index_lang.html) to users and developers that are using Drupal to transform community news.  [Lisa Williams](http://www.newschallenge.org/winners/lwilliams.html) was there to talk about [PlaceBlogger.com](http://www.placeblogger.com/) and [Benjamin Melançon](http://www.newschallenge.org/winners/melancon.html) talked about his "related" module.  For more information on what newspapes are doing on Drupal, see [Newspapers on Drupal](http://groups.drupal.org/newspapers-on-drupal).  
  

#### [Drupal Configuration Management](http://boston2008.drupalcon.org/session/drupalcon-tutorial-best-practices-development-environments-staging-build-management-and-prod)

Configuration management (as in managing multiple environments and promoting code forward from development to production and pushing content back from production to QA) in Drupal has always been a pet peeve of mine.  To put it simply, there is no good or standard way to do it.  The core issue is that Drupal stores a lot of configuration in the database and there is no good way to move a configuration from one instance to another.  A second component of the problem is that IDs are overly important in Drupal because most developers use IDs in their application logic but these IDs are randomly assigned by database sequences.  I think these configuration management issues will keep Drupal from being adopted by large development teams building huge sites.  I sat through a [session on this topic](http://boston2008.drupalcon.org/session/drupalcon-tutorial-best-practices-development-environments-staging-build-management-and-prod) and a Birds of a Feather discussion only to learn that everyone is doing some hack or another.    
  
The hacks break down into two categories: use a macro tool like the Devel module or a third party application to record and replay the clicking of options in the admin forms; use ranges of IDs for settings that are owned by different environments.  The latter is the preferred  
method by advanced developers.  They do things like start the sequence of dev at 1 and the sequence of production at 5,000 so there are no collisions.  Or they use odd numbers for development and even numbers for production.  Neither approach is straight-foward or scalable.  Developers talked about all these database scripts and diff'ing processes that they have created.  I would really like to see some fundamental improvements in this area like using the file system to store these settings and best practices in coding to avoid using IDs.  
  
__\[Update: Jean-Baptiste Ingold was kind enough to record the BoF session and post [it on Blip](http://drupalstaging.blip.tv/%23725427)\]__  
  

#### Related links

*   [Drupalcon 2008 website](http://boston2008.drupalcon.org)  
    
*   [Eckman on Drupalcon](http://www.openparenthesis.org/tag/drupalcon2008)  
    
*   [Ben Finklea tweeted like crazy on Drupalcon](http://twitter.com/benfinklea)  
    
*   [Twitter Feed](http://twitter.com/drupalcon)  
    
*   [Flickr](http://flickr.com/photos/tags/drupalconboston2008)  
    
*   [Audio from Keynote](http://sgluskin.podomatic.com/)  
    

  
  
