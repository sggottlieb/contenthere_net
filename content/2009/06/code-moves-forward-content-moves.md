Title: Code moves forward. Content moves backward.
Date: 2009-07-01T06:54:00Z
Modified: 2015-01-06T12:15:59.618Z
Category: misc
Tags: architecture
Slug: 2009/06/code-moves-forward-content-moves
Authors: Seth Gottlieb

One of the primary functions of a web content management system is separating content from layout.  Authors create semi-structured content in a display-neutral format and then the presentation templates transform that content to web pages for regular browsers, mobile browsers, RSS feeds, email, and print.  As most readers of this blog know, this separation introduces big efficiencies in re-use: content is managed in one place and appears in many places and in many formats.  But this magic does not come for free.  Someone has to build presentation templates that render the content and that person needs to have developer skills.  The template developer needs to know HTML and the special templating syntax to retrieve and format content from the repository.  The developer also needs know how to test software for all the different conditions that it will encounter: different browsers; content with extreme values in any of its elements (like a really long title or a missing summary); and even high traffic load.  Because one piece of code can potentially affect every page on the site, testing is important and it needs to be done in a safe place.  The same thing goes for all sorts of other software configurations.  
  
Essentially, the role of the static webmaster has been broken into two: the content contributors (that no longer need to be technical) and the developer (who needs to be more skilled than your average DreamWeaver jockey).  It also breaks up the management of the site into two lifecycles: the content lifecycle and the code/configuration lifecycle.  The production instance of the CMS itself is designed to support the content lifecycle.  CMS have workflow functionality to manage the state of an asset from draft through published and to archived.  They have preview functionality so that only contributors can see content that has not been published.  Some CMS are designed sot that the development lifecycle can also occur in the production instance.  This is usually done by creating workspaces or sandboxes — essentially treating code like another category of content.  To be sure, you still want to have a QA instance of the system so you can test software upgrades (of the core) before applying them to your live site.  In most CMS, however, developers work on separate environments (either individual developer environments and a code staging area or a shared development environment) and not the live, productive instance of the CMS.  
  
While the content and the software lifecycles are de-coupled, they are interdependent.  Developers need realistic content to develop and test code.  The content relies on the code to define and display itself.  There are lots of situations where these aspects get tangled.  For example, when a new field is added to a content type it needs to be populated (sometimes manually) and the presentation templates need to be modified to display it.  There are also cases where the line between content and code starts to blur: contributors style their content with CSS classes that are defined in style sheets; contributors can embed a tag that calls some additional display logic (like inserting a re-usable display component); contributors can build web forms that need to be submitted to code that does something with the information.  
  
![](http://media.contenthere.net.s3-website-us-east-1.amazonaws.com/blgimages/code-content.png)  
  
The standard approach for managing these interdependencies is what I call "code forward, content backward." Code and configuration is developed in a development environment and tested in a QA environment.  When it is ready, it is deployed to production.  Content is developed and previewed in the production instance that contains the staging (or preview) and live content states.  Periodically, content should be published backwards to the development and QA instances so that testing can be realistic as possible.  In cases where the code/configuration and content are so tightly coupled (like when you need to break one field into two), you may need to export production content to the QA instance where you do some content transformation and test it with the newest code and then push that content and code back to production at the same time.  When you do this, just make sure that you don't have anyone adding content to production because it will be overwritten or (worse) cause some kind of corruption.  
  
Different CMS handle the migration of code and content in different ways.  Some provide nice graphical utilities to export configurations from instance of the application to another.  In other products, there are ways to manually transfer the settings as a collection of files.  Some products don't support this at all so you have to manually repeat the same steps on each environment you are managing.  When you are evaluating CMS products, keep these requirements in mind.  Otherwise, you will be in for a surprise as you near the launch date of your new website and you need to fix bugs on live content.