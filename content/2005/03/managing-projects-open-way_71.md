Title: Managing Projects the Open Way
Date: 2005-03-08T13:34:00.002Z
Modified: 2015-01-06T11:32:13.930Z
Category: misc
Tags: 
Slug: 2005/03/managing-projects-open-way_71
Authors: Seth Gottlieb

One of the things that we try to do at Optaros is leverage some of the best practices of open source projects in our own work with clients. There are many great articles about applying open source development principles to internal software development projects. Here are some very simple practices and tools that I find useful.  

We use the source control system [subversion (svn)](http://subversion.tigris.org) to manage all of our file-based deliverables (code and documentation). Windows users connect via <a hef="http://tortoisesvn.tigris.org/">Tortoise SVN</a>, which integrates into Windows File Explorer and exposes svn functionality from a right click menu, or the Eclipse plugin [subclipse](http://subclipse.tigris.org/). \*NIX users can also use subclipse but many prefer just to use the command line client.  

One great configuration in svn is to hook it up to a mail list so subscribers get an email whenever anyone checks in their work. Subscribing to the svn commits mail list keeps everyone in sync. You know what has changed and why with the check-in comments.   

Subversion is primarily designed for managing text files and handles concurrency between users by merging rather than the locking checkout model. This does not work so well for binary files such as MS Word documents. However, svn will recognize and notify you of the conflict so you can use the compare documents feature in MS Word to merge documents.   

When possible, we write our documentation in HTML with a simple style sheet that applies a common style to all of the deliverables. These HTML pages are easily converted to PDF to make them more portable. Using HTML avoids problems like different versions of Word or Open Office mangling formatting.  

We use a Wiki ([Media Wiki](http://wikipedia.sourceforge.net/)) for information sharing such as ramp up materials and tips. Media Wiki has an RSS feed of edits so it is easy to keep up to date with changes. One very cool use that we have found for a Wiki is to have multiple users work on a document (such as a proposal) together. The way to do it (in Media Wiki at least) is to create the outline of the document using Wiki headings (==heading==) and save it. Doing this breaks up the page into multiple editable sections. Then each team member can work on his/her section by clicking on the edit button for that section. Once every section is complete, you can click on the edit page link and copy all of the text into a document. This technique allows a group of people to work rapidly on a document without getting in each others way.  

I like to use bug tracking software (such as [bugzilla ](http://www.bugzilla.org/)) for more than just recording bugs found in software during QA. Usually projects start using a bug tracking system once code starts getting delivered. I like to capture defects, enhancements, dependencies, and issues through the analysis and design of the software as well. I think this is better than the typical spreadsheet for several reasons. First of all, there is no concurrency issue: with a spreadsheet, only one person can edit it at a time and you never really know whether you are looking at the latest version. Second, a bug tracking system can capture the dialog around an issue in addition to the status. Third, bug tracking systems send emails to the owners and they have the power to update the task (rather than having a bottleneck at the project manager).   

These little tactics really help with the coordination of work and communication within our teams. They do not require huge process or methodology changes, just the introductions of some (free) systems that automate communication and collaboration so they don't fall through the cracks. There are many more tips on the development side but I will save those for another post
