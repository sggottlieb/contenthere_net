Title: CMS Deployment Patterns
Date: 2007-06-11T20:02:00.002Z
Modified: 2015-01-06T11:32:50.441Z
Category: misc
Tags: selection, architecture
Slug: 2007/06/cms-deployment-patterns_26
Authors: Seth Gottlieb

One of my favorite terms in the world of Web Content Management is "baking vs. frying," which refers to <span style="font-style: italic;">when</span> presentation templates are applied to render pages out of structured content.  Baking style rendering systems generate pages when content is published.  Frying systems generate pages on the fly when they are requested by the end user.  Whether a system bakes or fries content tells a lot about its architecture and what it is good at.  Baking systems are great for high volume sites that do not need to personalize content.  Frying systems excel when requirements include personalization, access control, and other presentation logic that uses information about the user in order to decide what to show and how.  
  
While "baking and frying" does a great job of describing how a system is designed, there are lots of slight variations on how to implement a WCMS that are repeatable enough that they deserve names too.  Here are a few.  
  
<span style="font-weight: bold;">Web Content Application Framework  
![](http://media.contenthere.net.s3-website-us-east-1.amazonaws.com/blgimages/WCMWAF.png)  
</span>When a frying style CMS has a decent templating language and a other good web application framework functionality (such as user sessions and profiles, a controller to manage URLs, and the ability to import custom and third party libraries) it is very tempting to start building applications on top of it.  In the open source world, you see this happening all the time with projects like Drupal and Plone where you can download and install application like modules (for instance a [shopping cart](http://mamboxchange.com/projects/mambo-phpshop/) or an [issue tracking system](http://plone.org/products/poi)).  Products like FatWire position themselves as tools for building dynamic content centric applications.  There is nothing inherently wrong with this strategy but it does run the following risks:  

  
 *   Lock-in. Most of the code that you write on a CMS is not portable to another web application framework. You can mitigate this by writing as little logic as possible in your page templates. Code in classes is easier to reuse.
  
 *   Sub-optimal application design. CMS presentation tiers are designed for displaying information. While they may have some transactional capabilities, they may not be as good as a pure web application framework designed for transactions. You might find yourself doing funny things like making dummy pages in the CMS so you can have a URL that a form can post to.
  
 *   Depending on the licensing model, scaling up the architecture for high traffic and fail-over redundancy may be very expensive.
  

  
<span style="font-weight: bold;">Published Static HTML</span>  
Static deploy is the classic baking style presentation pattern of generating static HTML files.  Nothing special to talk about here other than the fact that this design does not support any server side interactivity. No server side activity means that you can deploy the site across a farm of inexpensive web-servers, making your website infinitely scalable.  If your site serves 200 million content-rich pages a day, this model is probably your only option (unless you are Google).  You can do things like add AJAX libraries to third party services for features like comments, record site traffic, and pulling in dynamic content.  Companies wanting to get a little more interactivity into their managed pages will often use their baking style CMS in a Published View Code pattern.  That is next.  
  
<span style="font-weight: bold;">Published View Code</span>  
![](http://media.contenthere.net.s3-website-us-east-1.amazonaws.com/blgimages/publishViews.png)  
Also called "[parbaked](http://www.cmswatch.com/Feature/91-The-GRUPA-Gremlin)," Published View is when your baking style CMS writes out un-executed scripting or templating code rather than just static HTML.  This code is then executed at request time for a dynamic user experience.  At the very low end, this could just be server side includes or simple show/hide conditional logic.  At the high end, it could be the View component of an [MVC pattern](http://en.wikipedia.org/wiki/Model-view-controller).  This hybrid model has some performance advantages over a fully dynamic site and gives the architect some flexibility as to what presentation technology she can use.  There is also less lock-in because most of the complicated application logic is written into a presentation tier that will not necessarily be replaced when the CMS is swapped out.  This design is also great for when you want to slowly phase in a CMS to manage a site that is already written in a scripting language because dynamically generated scripting code (from the CMS) can coexist with hardcoded scripting code.  Keep an eye out for the following risks:  

  
 *   This design complicates the MVC pattern a bit because part of the "model" is baked into the "view." Once the MVC pattern gets kind of broken, it is a slippery slope to start baking more and more model type stuff into the view.
  
 *   If you are layering CMS generated views into an MVC architecture with its own controller (that takes in requests and routes them to the appropriate pages), the CMS is going to have less control over the website than it thinks it does. URLs are going to be different so links may break. Preview can (and probably will) be a problem.
  
 *   The developer may need to work on two systems that require different kinds of skills. Different departments may even need to get involved.
  
 *   Because there is application logic being executed at request time, the delivery environment will require more computing power. However, you will not need to buy CMS licenses for all the servers on your web farm.
  

  
<span style="font-weight: bold;">Structured Publishing</span>  
![](http://media.contenthere.net.s3-website-us-east-1.amazonaws.com/blgimages/structuredPublish.png)  
Structured Publishing is when your CMS publishes content as XML or rows in a relational database rather than pages on a website.  A totally decoupled presentation tier then reads from this "presentation repository" to deliver the website.  Structured assets can also be delivered at request time through a web services or a ReST style API but this requires a lot of computing power on the CMS and some good caching technologies on the delivery tier.  In this model, the CMS has little or no control over the organization or behavior of the website.  I wrote a [blog post](http://www.contenthere.net/2006/12/area-architect-dreams-of-model.html) about this design a while ago so I won't repeat myself here.  This design tends to work the best when content authors are not writing with one presentation channel in mind (for example if they are writing for print, web and sms, they tend not to get too wrapped up in the display on any one channel) and there is a separate group of people that are solely focused on the layout and behavior of the website.  
  
Depending on the WCM product that you are working with, these patterns may be more or less obvious but still possible.   For example, frying style WCM systems are designed for the Web Content Application Framework model.  However, I have seen plenty of customers use a tool like [wget](http://www.gnu.org/software/wget/) to take a static HTML image of a dynamically generated website to deploy to a simple web server farm.  The [Enfold Entransit ](http://plone.org/products/entransit)product allows content to be produced in Plone (a frying style system) and then publish structured content to another delivery tier.  
  
I have seen all of these patterns succeed and fail to varying degrees. The biggest driver of success is knowing when to use a pattern and when not to. You need to look at your requirements - both the immediate ones and the long term vision.
