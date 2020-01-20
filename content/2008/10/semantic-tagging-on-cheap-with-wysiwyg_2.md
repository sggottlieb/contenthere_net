Title: Semantic tagging on the cheap with a WYSIWYG editor
Date: 2008-10-02T08:44:00.001Z
Modified: 2015-01-06T12:15:39.659Z
Category: misc
Tags: 
Slug: 2008/10/semantic-tagging-on-cheap-with-wysiwyg_2
Authors: Seth Gottlieb

I am surprised by how few companies employ the little trick of using the WYSIWYG editor in their CMS to semantically tag rich text fields.  The general idea is that you overload the WYSIWYG CSS support by using the CSS classes with semantically meaningful names.    
  
Here is an example.  Lets say you are publishing a business journal and you write a lot about _companies_ and _regulatory agencies_.  You might have a sentence like   
<blockquote><p>Apparently, following an investigation into the hacking of several dozen customer accounts, the <em>SEC</em> found <em>LPL</em> negligent.<p><br/><p align="right"><a href="http://www.informationweek.com/blog/main/archives/2008/09/sec_fines_wall.html">source</a></p></p></p></blockquote>  
The terms "SEC" and "LPL" are italicized in compliance with your style guide.  To satisfy the style guide, your reporter probably just highlights the text and clicks the italics button.  But, what if your style guide changes to say that company names are bolded and your regulatory agencies are in red text?  Using style classes would give you much greater flexibility than "em" and "strong" tags.  Most WYSIWYG editors can be configured to have a drop down list of style classes.  When a user highlights the text and selects the class, the WYSIWYG editor writes it as a span tag with that class:  
  

<pre>&lt;span class="classname"&gt;LPL&lt;/span&gt;</pre>

  
  
Now what should you name your classes?  Here is the trick.  Rather than call them "italics" or "bold" or "red," give them names to indicate the _meaning_ of the text that you are styling: such as "company" and "regulator."  In addition to giving more flexibility in styling, you will be able to do some really interesting things with your content. For example:  

*   With a very simple XSL template you can have your rendering template put a list of mentioned companies and agencies on the page.  
    
*   You could extend the logic of your CMS to automatically create metadata about the article to help your search engine figure out that your article is about _Apple_ computers rather than _Motts_ Brand Apple Juice.  
    
*   You could have your rendering templates insert the stock symbol of the company or create a link to their ticker page.

  
The possibilities are really endless when your programming logic has access to the _meaning_ of your content.    
  
Using a WYSIWYG editor to do simple semantic tagging is not the only way to add meaning to your content.  You can have your authors write in an XML editor.  You can use a text mining engine match words against a centrally managed controlled vocabulary.  However, I have found that this approach is the least expensive, most practical way to get started.  They _want_ to have their article look nice.  This approach captures that intent and, with no additional effort, creates additional value that your author  (at first) is less aware of.  Once your content starts to have semantic tagging and your technology starts to leverage it, your authors will probably start to see the benefits and really get excited about the possibilities.    
