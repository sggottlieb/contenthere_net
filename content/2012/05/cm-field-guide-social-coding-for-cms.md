Title: CM Field Guide: Social Coding for CMS Geeks
Date: 2012-05-14T09:14:00Z
Modified: 2015-01-06T12:30:24.279Z
Category: misc
Tags: fieldguide, announcement
Slug: 2012/05/cm-field-guide-social-coding-for-cms
Authors: Seth Gottlieb

<img alt="" class="alignleft" height="172" src="http://www.cmfieldguide.com/media/img/logo.png" style="padding: 0px 10px 10px 0px" width="200"/>

Evil genius Deane Barker ([@gadgetopia](https://twitter.com/#!/gadgetopia), [gadgetopia.com](http://gadgetopia.com/)) approached me with this idea at a vulnerable time. My fingers were itching to code. I had recently transitioned out of all programming responsibility for a consulting client. I was managing a few development projects on which I forbade myself from coding. I was also feeling a little disconnected from the content management community. With this backdrop, Deane taps into our strange shared hobby of detecting what content management system is running a website. He shows me some working Django code that he wrote (a little smelly but excellent for a first attempt at Python and Django — I love Deane's fearlessness.); and before I can force myself to say no, I am refactoring.  
  
That's how [CM Field Guide](https://github.com/sggottlieb/cmfieldguide) got started. And it is shaping up to be a really cool project. While there are other applications that do the job of sniffing out what CMS a site is running on, CM Field Guide is unique in that it is a social coding project. We share the "tells" we know to look for and we invite people to submit theirs either as [code](https://github.com/sggottlieb/cmfieldguide/tree/master/cmfieldguide/cmsdetector/signatures) or as a [description that we can code](https://github.com/sggottlieb/cmfieldguide/issues?direction=desc&amp;sort=created&amp;state=open).  
  
[The code that examines a website is called a "signature" and they are really easy to write](https://github.com/sggottlieb/cmfieldguide/wiki/BuildingASignature). It's mostly metadata and a line or two of test logic. The foundation application and libraries do most of the work. We use [github's social coding model of forking and pull requests](http://help.github.com/fork-a-repo/). As of this blog post, we have 26 platform signatures. Steven Brent ([@stevenbrent](https://twitter.com/#!/stevenbrent)) submitted 2 of them as github pull requests. Adriaan Bloem ([@adriaanbloem](https://twitter.com/#!/adriaanbloem)) and Robb Winkle ([@robbwinkle](https://twitter.com/#!/robbwinkle)) shared their secrets over email and github issues.  
  
While I am already finding the application useful, the most interesting aspect of the project for me is around knowledge management. The discipline of Knowledge Management likes to say that knowledge is distinguished from information because it is actionable. Turning information into executable code seems to take this to a whole new level. There is also a social aspect, it's fun to share this information with people and build relationships on a common interest.  
  
A closed alpha of the application is running at [www.cmfieldguide.com](http://www.cmfieldguide.org). We haven't done any real user interface work yet (volunteers?) and we haven't optimized the application for any kind of load. At the moment, we are only giving out accounts to friends and colleagues. But you can quickly become a friend with your contribution!
