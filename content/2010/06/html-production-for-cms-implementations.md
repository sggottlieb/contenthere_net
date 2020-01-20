Title: HTML production for CMS implementations
Date: 2010-06-28T08:24:00Z
Modified: 2015-01-06T12:16:17.092Z
Category: misc
Tags: Web2.0, social networking, Content Strategy
Slug: 2010/06/html-production-for-cms-implementations
Authors: Seth Gottlieb

Most new site CMS implementations (as opposed to site migrations from one CMS to another) start off with a set of HTML mockups. This can be a convenient starting place because, in addition to showing how the pages should look and informing the content model, having the HTML gives a good head start to presentation template development. Ideally the template developer just has to replace the sample "Lorem Ipsum" text with a tagging syntax that retrieves real content from the repository. There are even some graphical tools that help a developer map regions on the mockup with content from the repository. However, often moving from HTML mockups to presentation templates isn't so smooth. Sometimes the HTML has to be re-written from the ground up.  

The most common source of problems is when the HTML is too specific. This usually occurs when the designer/developer who produces the mockups is accustomed building static HTML websites where she has full control over everything. HTML and CSS for an CMS implementation has to account for the fact that control is shared between the template and the content contributor. While the template controls the overall layout, the control contributor controls the navigation, text, images, and (with the help of a rich text editor) can even style body content. HTML code that is rigid and brittle breaks when stretched by unanticipated content. Here are some things to look out for.  

  

*   __Hard coded height and width dimensions on image tags__. Most content contributors don't know the first thing about aspect ratios. They upload a picture and don't understand why it is squished on the page. While most CMS these can automatically scale images (and even if they can't the browser will), they can't all reshape them. While some CMS support cropping functionality for thumbnails, few content contributors know how to use it to precisely shape an image. I usually recommend setting only one dimension (usually width) and then letting the other dimension (usually the height) do what it needs to do. If you really need to control both, you can use this little background image trick:  
    
    
    <pre><br/>   &lt;div class="picture" style="background: url(&lt;&lt;horizontally scaled image path&gt;&gt;) no-repeat; height:150px;"&gt;&lt;/div&gt;<br/></pre>
    
      
    This uses the image CMS's image scaling to set the width and vertically crops the image after 150 pixels by making it a background image.  
    
*   __Overusing element ids__. When you are only building a few pages and you want very direct control over elements, there is a temptation to code CSS to reference specific element ids rather than classes. In some cases, this makes sense. For example, when there is only one global left navigation component. However, it makes less sense for anything that a content contributor might have control over — like items in that navigational menu or anything else that repeats. I haven't used DreamWeaver (DreadWeaver, as I like to say) in years but I suspect that the HTML/CSS auto-generation generation prefers using IDs over classes because that is where I see it the most. The worst case I have seen was a sample search result page with every search result individually styled with element ids.  
    
*   __Over-complicated HTML.__ HTML is only going to get more complicated when it is infused with template syntax. It is best to start with HTML code that is as simple and terse as it can be. If a designer is still using nested tables to position things, have him work in photoshop. The more styling you can do in CSS the better. This will make templates cleaner, more efficient, and easier to manage. Plus, your CSS will survive a migration to another CMS better than your template code will.  
    
*   __Using images rather than text headings__. While the font control afforded by images is nice, avoid using images for anything dealing with the navigation or page names. Otherwise content contributors will not be able to create new pages or re-organize the navigation without a designer to produce images. If you have a top level navigation that is unlikely to change, you can compromise by building images just for the top level page names. A decent strategy is to code the HTML like  
    
    
    <pre><br/>    &lt;h1 class="section-heading &lt;&lt;dynamic section name in lowercase &gt;&gt;"&gt;&lt;&lt;sectionname&gt;&gt;&lt;/h1&gt;<br/></pre>
    
      
    for example:  
    
    
    <pre><br/>    &lt;h1 class="section-heading about"&gt;About&lt;/h1&gt;<br/></pre>
    
      
    This way, if a content contributor introduces a new section that doesn't have an image or style yet, there is a decent fallback of styled text.  
    
  
*   __Too many layouts__. Most web content management systems prefer you to have an overall page layout template (also known as a master page) that is used for nearly all of the pages of the site and then content-type-specific templates that render in the "content area" in the center of the page. Things like the header, footer and global navigation components go in the page layout template. In many systems these two templates are not very much aware of each other because they are rendered at different times within the page generation process. The trick is to determine what portions of the page to put in the global template and what to put in the content-type specific templates. The more you put in the content-specific templates, the more flexibility you have but you also wind up having redundant code that adds management overhead. You also want to make sure that the design does not specify too many options for content presentation templates. In addition to adding to maintenance overhead, this also confuses the user. When lots of variability is required, it is a good technique to design the implementation to allow contributors to build pages with blocks of content. This way, the presentation template just has to define "slots" that contributors can fill (or not fill) with content.

  

Most of these tips will come more naturally to an advanced HTML that really knows his stuff than a pure designer with design tools that can create HTML. However, even the best HTML developers can have mental lapses when they get into a production groove. It is a good idea to understand the HTML producer's skill-set before assigning the task of HTML production and set expectations. Otherwise, you will probably get a rude awakening when template development is scheduled to start. If this type of HTML production is new to your team and you would like them to learn it, account for this learning by holding frequent reviews of the HTML code as it being produced. Start with the most simple content type (like a generic page) so you can focus on the global page layout and get alignment on static vs. variable components. Over time, your team will instinctively notice HTML code that works for the mockup but will be problematic in a presentation template. 
