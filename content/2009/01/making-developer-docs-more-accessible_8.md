Title: Making developer docs more accessible
Date: 2009-01-08T09:12:00.001Z
Modified: 2015-01-06T12:15:40.767Z
Category: misc
Tags: 
Slug: 2009/01/making-developer-docs-more-accessible_8
Authors: Seth Gottlieb

<div class="thumbnail"><a href="http://skitch.com/sggottlieb/by1yu/java-ee-crxdeploy-build.xml-eclipse-sdk-users-sethgottlieb-documents-projects-clients-time-interactive-development-crx-clean-ab"><img alt="Java EE - crxdeploy/build.xml - Eclipse SDK - /Users/sethgottlieb/Documents/projects/clients/time_interactive/development/crx-clean-ab" src="http://img.skitch.com/20090108-tesidbny4jp3i354npbddpajy6.preview.jpg"/></a><br/><span style="font-family: Lucida Grande, Trebuchet, sans-serif, Helvetica, Arial; font-size: 10px; color: #808080">Uploaded with <a href="http://plasq.com/">plasq</a>'s <a href="http://skitch.com">Skitch</a>!</span></div>

  
  
What do developers hate more than writing documentation? Writing documentation that nobody will read.  I think everyone has been in a meeting and heard someone complain about needing some information that they didn't even bother to search the wiki or document repository for.  But what if the documentation was already in the developers face?  
  

<div class="thumbnail"><a href="http://skitch.com/sggottlieb/byqie/new"><img alt="New" src="http://img.skitch.com/20090107-x5sbxed6ngrum73f9jcstww2i3.preview.jpg"/></a><br/><span style="font-family: Lucida Grande, Trebuchet, sans-serif, Helvetica, Arial; font-size: 10px; color: #808080">Uploaded with <a href="http://plasq.com/">plasq</a>'s <a href="http://skitch.com">Skitch</a>!</span></div>

  
  
A few weeks ago, a client turned me onto "Cheat Sheets" in [Eclipse](http://www.eclipse.org).  Those are the little instructions that appear on the right-most frame of the Eclipse IDE.  You may have used one of these Cheat Sheets before (and not known what they were called) but you probably didn't know how easy they are to create.  Simply choose the "File | New | Other" menu option and then, under "User Assistance," select Cheat Sheet.  This will give you a simple editing tool to create step by step instructions.  The underlying XML is very simple so you can also just use Eclipse XML editor if you want to.  
  

<div class="thumbnail"><a href="http://skitch.com/sggottlieb/byqi7/java-ee-crxdeploy-testing.xml-eclipse-sdk-users-sethgottlieb-documents-projects-clients-time-interactive-development-crx-clean-ab"><img alt="Java EE - crxdeploy/testing.xml - Eclipse SDK - /Users/sethgottlieb/Documents/projects/clients/time_interactive/development/crx-clean-ab" src="http://img.skitch.com/20090107-qt7at1q93ubrftcu4ri5bk3tj4.preview.jpg"/></a><br/><span style="font-family: Lucida Grande, Trebuchet, sans-serif, Helvetica, Arial; font-size: 10px; color: #808080">Uploaded with <a href="http://plasq.com/">plasq</a>'s <a href="http://skitch.com">Skitch</a>!</span></div>

  
  
This form of documentation is best for things like development environment setup.  It is not so great for API or architectural documentation.  It assumes that the developer is using Eclipse and has been able to check the appropriate source tree out of the source code repository because the documentation is stored within the project.  I would use this in conjunction with a README and INSTALL file.  README would be used for information about the application (version, usage, recent changes, open issues).  INSTALL would be for someone installing the compiled application.  The Cheat Sheet(s) would be for developers that are getting their Eclipse environment together.  
  
Is anyone else using this feature? If so, have you found it effective?
