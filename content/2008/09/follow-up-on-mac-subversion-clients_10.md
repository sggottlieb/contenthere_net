Title: Follow up on Mac Subversion clients
Date: 2008-09-10T22:12:00.001Z
Modified: 2015-01-06T12:15:39.443Z
Category: misc
Tags: 
Slug: 2008/09/follow-up-on-mac-subversion-clients_10
Authors: Seth Gottlieb

A few weeks ago I wrote a post [introducing two new Mac Subversion clients](http://blog.contenthere.net/2008/07/mac-svn-clients.html): [Cornerstone](http://www.zennaware.com/cornerstone/) and [Versions](http://versionsapp.com).  After the free trials expired I chose Cornerstone and have been pretty happy with it.  I tend to use Cornerstone as a file browser when I am working with a straight text editor (like [TextMate](http://macromates.com/)).  From there I can browse around my working copy, open files, and see changes against the most recent from the repository.  The user interface is very clean and presents useful information clearly.  When I am working in Eclipse, it is hard to resist the convenience of [Subclipse](http://subclipse.tigris.org/).   
  
Interestingly, the main reason why I switched from [TextWrangler](http://www.barebones.com/products/textwrangler/) to TextMate was its project browsing functionality.  Now Cornerstone plays that role for me - at least for anything I have in source control, which is everything.  However, I have gotten used to TextMate so I think I will stick with it.    
  
For a while, I struggled with Cornerstone's performance.  It seemed to consistently hang as it tried to scan the file system for changes.  This was resolved by changing a preferences setting: Preferences -&gt; Working Copy -&gt; Refresh Working Copy = "Manually."  Now it only checks the working copies when I ask it to (with command-r).    
  

<div class="thumbnail"><a href="http://skitch.com/sggottlieb/iur5/cornerstone-annotated"><img alt="Cornerstone-annotated" src="http://img.skitch.com/20080910-kj66wcwqfhib3149n5cpwr4ws2.preview.jpg"/></a><br/><span style="font-family: Lucida Grande, Trebuchet, sans-serif, Helvetica, Arial; font-size: 10px; color: #808080">Uploaded with <a href="http://plasq.com/">plasq</a>'s <a href="http://skitch.com">Skitch</a>!</span></div>

  
  
One thing you may notice in the screen shot above is that it shows Cornerstone looking at the source code from my website.  A lot of people ask me what web content management system I use.  Well, the answer is none.  Because my website is so small and I am comfortable with source control, HTML, and FTP, I really don't need one.  My website as 13 pages.  A web content management system is like a web page factory.  You don't build a factory to produce 13 units.  Of course, that may change when I hire that flashy marketing executive with the wafer-thin laptop.  
  
I use [Transmit](https://www.panic.com/transmit/) as my FTP client.  It has a nice little feature called "Drop Send" that allows you to drag a file onto the Transmit icon in your doc (from Cornerstone or your Finder) and it automatically puts it in the right place (thanks for the tip [dizzytree](http://dizzytree.com/2008/04/26/tip-textmate-and-transmit-ftp/)).   If you want an all-in-one alternative to the TextMate/Transmit/Cornerstone combo, you might try [Coda](http://www.panic.com/coda/), which seems to do it all like Adobe Dreamweaver (without the WYSIWYG but $300 cheaper).  The latest version of Coda (1.5) has a SVN client.   
  
