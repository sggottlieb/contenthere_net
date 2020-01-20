Title: PL Upload: a solution for uploading really large files into a web application.
Date: 2013-04-24T09:56:00Z
Modified: 2015-01-06T12:30:25.111Z
Category: misc
Tags: tricks, development, review
Slug: 2013/04/pl-upload-solution-for-uploading-really
Authors: Seth Gottlieb

I am working on this web application project that has a requirement for users to upload REALLY big files (as in 1 gigabyte plus). Given ubiquitous broadband (do people even call it broadband anymore?), and increased usage of video, I would not be surprised if lots of developers are seeing this requirement. The problem is that the basic HTML file upload field is horrible for very large files. It does not resume if there is a momentary interruption in transfer and the server gets stuck with one very large, resource-eating request. The traditional work-around is to use a flash application to upload the files. [SWFUpload](https://code.google.com/p/swfupload/) seems to be the most common implementation, but if you go to the home page, you will find that the project is no longer being maintained and is starting to break with new versions of Flash.  

I was feeling pretty discouraged until I discovered [PL Upload by Moxiecode](http://www.plupload.com/). If Moxiecode sounds familiar, it is because they make [TinyMCE](http://www.tinymce.com/), which has practically turned into the de facto standard rich text editor (WYSIWYG) for applications like content management systems. Sorry [CK Editor](http://ckeditor.com/).   

The best part of PL Upload is that it embeds multiple implementations and selects the right one based on the capabilities of the browser. Modern browsers get an HTML5 implementation. There are also Flash, Silverlight, Google Gears options. You set the order of options to try and some Javascript goes through your list until it finds one that works. Another really nice feature is that PL Upload chunks the data into bite size morsels so that your server-side code gets lots of small requests rather than one big one. This makes resource management much easier and prevents one large upload from compromising the overall performance of the site.  

I think the Moxiecode team is brilliant for seeing this problem and building such a nice solution. They seem to have used the same logic as when they came up with TinyMCE. Take a pervasive, nagging problem and build a clean solution that can become a de-facto standard. Their business model is to dual-license the software: [GPLv2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html) for websites like mine and a commercial license for embedding the component in non-GPL software applications. I expect to see PL Upload surfacing in lots of content management systems just like I see TinyMCE.
