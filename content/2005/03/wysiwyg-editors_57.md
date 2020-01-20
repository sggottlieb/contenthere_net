Title: WYSIWYG Editors
Date: 2005-03-16T09:13:00.002Z
Modified: 2015-01-06T11:32:13.983Z
Category: misc
Tags: 
Slug: 2005/03/wysiwyg-editors_57
Authors: Seth Gottlieb

WYSIWYG editors are a key feature in most CMS products: both commercial and open source. These components add HTML controls to a web form field so that a non-technical user can apply their own formatting to the text that they enter. I think of WYSIWYG editors as being [The Great Compromise](http://www.cyberlearning-world.com/nhhs/amrev/begin.htm) of content management. WYSIWYG editors balance the needs of the authors, who would rather use something like MS Word to enhance their prose with formatting, and systems people who want structured data to store and reuse.  

In the commercial world, the leader is [Ektron's eWebEditPro](http://www.ektron.com/ewebeditpro.aspx) which is OEM'ed in [Interwoven Teamsite](http://www.interwoven.com/) and many other commercial CMS products. On the open source side, there are many projects including [htmlArea](http://www.dynarch.com/projects/htmlarea/), [Kupu](http://kupu.oscom.org/) and [BXE](http://www.blogger.com/%20http://bxe.oscom.org) and [Xopus](http://xopus.com/). Both BXE and Kupu are hosted on [OSCOM](http://www.oscom.org/) and there is some code sharing between them. Most WYSIWYG editors are based on Javascript to be cross browser compatible although not all are tested on both IE and Gecko based browsers.  

A couple of weeks ago I was setting up [Bricolage](http://www.bricolage.cc/) to work with htmlArea (which is integrated with Bricolage and several other open source CMS) and was surprised to see that the latest version (3.0) was no longer available on the [htmlArea](http://www.htmlarea.com/) website. I learned from the list that [InteractiveTools](http://www.interactivetools.com/) is no longer maintaining the code and the project has moved to [DynArch.com](http://www.dynarch.com/projects/htmlarea/) (thanks, Bret Dawson for the answers).   

Then last week, there was an interesting discussion on the OSCOM mailing list about htmlArea losing momentum and other emerging editors. Drupal has shifted from htmlArea to [TinyMCE](http://tinymce.moxiecode.com/) and has a [module](http://drupal.org/node/16118) to integrate [FCKEditor](http://www.fckeditor.net/). [XOOPS](http://www.xoops.org/) is now using [Kiovi](http://www.koivi.com/WYSIWYG-Editor/). Some simple editors such as [widgeEditor](http://www.themaninblue.com/experiment/widgEditor/) and [Cross-Browser Rich Text Editor](http://www.kevinroth.com/rte/demo.htm). Unfortunately, all of these WYSIWYG editor projects (like many Javascript projects) are pretty small and it is hard to tell where they are going. On the plus side, it is not a great risk to maintain these Javascript libraries on your own if you find one that meets your needs today.   

If you want a list of HTML Editors and the the browsers they support, check out the HTMLArea [website](http://www.htmlarea.com/directory/WYSIWYG_Editors/index.html). 
