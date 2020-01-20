Title: Plone Symposium Notes
Date: 2006-03-14T18:01:00.002Z
Modified: 2015-01-06T11:32:17.296Z
Category: misc
Tags: 
Slug: 2006/03/plone-symposium-notes_66
Authors: Seth Gottlieb

I just got back from the Plone Symposium in New Orleans. At first I thought I was going as a spectator but due to a last minute scheduling conflict, I was asked to do a presentation on the world outside of Plone. What follows are my notes and thoughts about the conference. Apologies for the detail and roughness. These are half notes to myself but I figure they might be interesting/useful to others so here they are.  

First of all, the venue. I commend Plone co-founder Alan for supporting the resurrection of New Olreans by holding the Symposium there. Probably most are interested in knowing what The Big Easy is like post Katrina so I will say a few words. The symposium was held at the Astor Crowne Plaza, which has not yet returned to its (I am told) usual splendor. The hotel is still hosting many storm refugees and there is a FEMA registration desk in the lobby. Housekeeping was hit or miss (either not at all or at 9:45 PM) and every once in a while the carpet seemed a little sticky. I didn't get much opportunity to venture outside of the French Quarter so I saw very little remaining damage or debris that I was certain was not related to Mardi Gras which happened just a few weeks before. The primary noticeable difference was the lack of people and energy that I remember from my last visit to New Orleans back in 1991. Bourbon Street still has loud music and drunken tourists wandering around and making out at the bar Ã‚? just a lot less of it. I read a copy of the Times Picayune and every article was either directly or indirectly related to Katrina or Katrina recovery. The overall impression that I got was that the city was tired and still a little bit in a state of shock. OK, enough with the travel log. Onto the conference.  
  

The attendance was decent for a Plone Symposium, which are generally smaller than the Plone Conferences. Many of the big names were there and there was a very nice feeling of community and openness. The program was packed with good content and I frequently found myself torn between two concurrent sessions. Generally the technical sessions got the majority of the audience.   

  
__Best Practices: Plone Development__  
  
By Joel Burton  

If you are looking for a good Plone trainer, call Joel. I am told that Joel is doing a week long Plone Boot Camp in Seattle soon and that the cost is amazingly low. If this 3 hour session was a representative sample, then the Boot Camp should be excellent. Some of the best tips:  

*   Make a Product for each distinct grouping of functionality and one Ã‚?site productÃ‚? to hold the skin. This will make your feature code more portable across projects.  
    
*   Use ArchGenXML to generate classes. It will also generate the scaffolding and directory structure that is required for Plone Products.  
    
*   Use VERSION.txt. It will cause Plone to remind you to reinstall the product if anything changes.  
    
*   Read the MySite and RichDocument tutorials.  
    
*   Have a routine that packs your ZODB every week.  
    
*   Configure your text editor to automatically create a .metadata file for your code. The .metadata file holds settings like cache, security, that you might be setting through the ZMI.  
    
*   Use the form controller framework which is configured throuth the .vpy (for validation rules) and .cpy file (for request processing sequences).  
    
*   Use SpeedPack for perfomance. This caches lookup of where to find skin assets.  
    
*   When skinning Plone, consider three strategies:   
    
    
    *   CSS Only. Don't touch the zpt code. Just use CSS. You can do a surprising amount with just styles. The next day Alexander Limi walked through he did Plone.net all with styles.  
        
    *   Modify the existing Page Templates and CSS. Do this when you want to make deep modifications to the UI and you have total control over the HTML. Example: http://usepropane.com  
        
    *   Replace the normal view framework entirely. Rather than have the normal main\_template.pt and macros, just use the HTML that you are given and use TAL syntax to reference content. Use this when you are given complex generated HTML and you don't have time to break it up into the Plone page rendering framework. This model makes the management view totally different from the Ã‚?retailÃ‚? or public view. The HTML code may be more difficult to manage (if it starts out messy) but render times might be a little faster.  
        
    
    
    
*   Leverage documentation generators. DCWorkflowGraph makes a nice picture of the workflow that you defined. EpyDoc generates Javadoc style documentation for your Python classes.   
    
*   Use setup scripts rather than through the web configuration. The code goes in the setup directory of your project. Put it in a file called CustomSetup.py.  
    
*   Check out the commercial but cheap Python editor Wing. In addition to having nice IDE functions, there is a great debugger that will allow you to visually step through your code with breakpoints and watches.   
    
*   Use PTProfiler to debug your template code: http://debris.demon.nl/ptp  
    
*   Use Zelenium (http://www.zope.org/Members/tseaver/Zelenium) for functional testing.  
    

  
  

  
__Make Plone Go Fast__  
  
By Geoff Davis  

Geoff Davis talked about his CacheFu product which aggregates and simplifies all the various caching settings that you need to support a high traffic site. Plone.org runs CacheFu and Wichert Akkerman, who administers and was in the audience, testified to its effectiveness. Plone.org serves 100,000 pages per day from a single low powered machine without the help of clustering. Geoff demonstrated a performance increase from 4 requests per second to up to 300. One of the keys to the solution is to have as much content served up by Squid (a web proxy that caches images, styles, javascript and page content) and add some intelligence as to how long Squid should hold onto things. CacheFu overrides the default Plone HTTP headers which are read by Squid to determine what to cache and how long. CacheFu also sends Squid purge commands when things change.  

CacheFu thankfully comes with a simplified sample configuration file that replaces the daunting default configuration file that comes with Squid. In the wild, Squid is used both to relieve the load on a dynamic website (as in this case) and to cache requests from an internal network to reduce the amount of bandwidth needed as in the case of a hotel. If you are not using Squid for the latter, the configuration file does not have to be so complicated.  

Geoff also covered some of the subtleties of the HTTP spec and how to optimize browser behavior through the use of HTTP headers. For example, telling the browser not to re-request an image or to use ETags that allow a quick check to see if the cached version is out of date.  

Resource Registries do things like merge CSS files and give the merged result unique identifiers which enables you to set an HTTP Header to tell the browser to cache the CSS file forever. When the CSS is updated, it is given a new name so you don't have to worry about a stale browser cache.  

Other performance strategies introduced include optimizing code with a profiler such as Zope Profiler, Call Profiler, and Page Template Profiler. If possible, Cache portlets that are slow (such as the calendar portlet) by wrapping the portlet in a macro and caching the string it outputs using RAMCacheManager.

  

  
__State of Plone__  
  
By Alan Runyan and Alexander Limi  

In the annual State of Plone speech, Alan and Limi talked about their vision for Plone and what is happening in the community. One of the interesting points made is that they think of Plone as the Ã‚?middle classÃ‚? of the Python community. The Plone community is large and the majority of users just know enough about Plone and Python to do their job. That is the  
attractive thing about Plone. It is simple, usable and has a wide range of capabilities. Zope was described as the Ã‚?J2EE Liberation Front.Ã‚? Plone won several awards and press mentions over the year. There are currently 50 translations of Plone and over 300 add-on products.  

Alan has been thinking of defining Plone's place in the world as a tool for content production. This is somewhat at odds with the view of many who see Plone and it's many add-on modules as a Universe unto itself. In a later talk, Alan talked about how the future of Plone development should be integration with other technologies rather than building more functionality onto the Plone platform. In fact, Runyan's company Enfold makes a product called Entransit that allows Plone content to be delivered through other presentation tiers. Alexander Limi's vision is very usability focused. From watching his presentations and a couple of one on one conversations, I really get how Limi drives the Plone UI (He almost got me to buy a Mac to BTW).   

The next release, 2.5, is going to be a major architectural release. It will not be as bad a migration path as 2.0 to 2.1 where all the content types were migrated to Archetypes and much of the UI was optimized. 3.0 is going to be a UI release and Limi has lots of ideas for improvement. One possibility is to move CMFEditions, which provides version control, into the core. In my opinion, that will open up Plone to much broader usage because lack of versioning has been a barrier for some companies that I have talked to. The history feature which was removed temporarily due to a bug will be back too.  

There was discussion of the relationship between Plone and Zope 3. Alan Runyan described how Zope 3 is now being thought of as an R&amp;D project where useful innovations and improvements would be merged into the Zope 2 line or made available through the Five project. There are solid efforts being made to coordinate the development of Plone and Zope such as Goldegg.   

  

  
__Alternative Templating with Zope__  
  
By Chris McDonough  

Chris McDonough introduced his new templating system <a ?="" href="http://www.plope.com/software/meld3">Meld3</a>. The design is a large departure from typical templating frameworks where the template pulls in and renders content. Meld3 Ã‚?pushesÃ‚? content into simple HTML view files using the DOM library ElemenTree. The advantage is that you do all your programming in straight Python classes. There is a very clear separation between the code and the format. This could lead to better division of labor between the programmer and the web designer. There is even a diff tool that shows you what nodes in the DOM tree have changed. The downside is that there are more files to keep in sync and there is not yet a production system running Meld3. Managing HTML forms is also a little more complicated than the traditional Pull model but there are some work-arounds.

  
  

  
__Introducing CMF 2.0__  
  
By Tres Seaver  

Tres Seaver talked about what is happening with Content Management Framework now that much of the functionality is folded down into the Zope stack. Goldegg financed Zope and CMF developers to harmonize where in the stack various services belong and clean-up or re-implement code to leverage Zope 3 technologies. There was also an interest int mending the gap between Plone/CMF and Zope. Part of that is to push some of the things that Plone does down the stack to increase the potential for reuse and also get more people involved with the maintenance and testing of this code.   

Some cool things that you can expect to see are more use of Python eggs which will make installing various configurations of Plone a little like Red Hat RPMs which will walk through, download and install additional dependencies; use of Zope 3 events, use of Zope 3 views which is a MVC implementation; cleaning up Zope Page Templates by moving Python (such as all the tal defines) out (this will have the added benefit of making ZPTs render faster because they will no longer be untrusted code which has a bigger security overhead); and better content export/import to the point where it could be used for data replication services. 

  
  

  
__Putting a new look on Plone and keeping accessibility __  
  
By Alexander Limi  

This was a talk that you really had to see to appreciate. Limi walked through how he skins sites. He did almost the whole things just using styles. He recommends strategy because the HTML generated by the existing templates is very well optimized for accessibility and search crawlers. The code and notes were promised but I have not been able to find them yet.

  
  

  
__Compliance Management using Banyan__  
  
By Munwar Shariff  

Munwar Shariff did a nice demo of a Plone based system called Banyan that is useful for solving problems like managing engineering documentation, configuration management, and strategic planning. One of the strengths of the application is that it maintains references between documents for things like traceability. The tool looked very flexible and would be useful for many business processes. It is being used effectively at Lars Livermore National Laboratory (http://www.llnl.gov/) for managing engineering documents.

  
  

  
__Integration not Isolation__  
  
By Alan Runyan  

Alan Runyan started the talk with the premise that most open source developers prioritize writing new code over integration with existing code. The problem is especially bad, he says, in the Python world because developing is so efficient and fun. However, most enterprises care the most about integration and how the various components within their architecture fit together.   

Alan wants to get make Zope less of an island. The example that he uses is that CMFBoard (an add on bulletin board that can be added onto a Plone instance) is a dead project but there is no good reason to write another one in its place. The Zope platform is not optimized for the kind of thing that a bulletin board is designed to do. Bulletin boards are write-intensive whereas the ZODB is more efficient with reads. Instead, Alan recommends integrating with an external BB software built in something like PHP. He did this using Simple Machines Forums (SMF: http://www.simplemachines.org/) for the OXFAM site. All that they needed to do was make some modes to SMF to enable single sign-on.   

Alan wants to create a repository in the Plone collective (which is used to store add-on products) for integrations with external systesm. These integrations could be patches that can be applied to external systems or adapters. Zope could be a very good platform to support this integration based architecture because of its strong support of XML-RPC. I really like this idea and I hope the dialog continues.

  
