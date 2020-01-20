Title: Have you modeled your content effectively?
Date: 2011-03-17T10:26:00Z
Modified: 2015-01-06T12:16:18.105Z
Category: misc
Tags: Content Modeling, Content Management Assessment
Slug: 2011/03/have-you-modeled-your-content
Authors: Seth Gottlieb

This is the second installment of a [series of articles on content management assessments](http://www.contenthere.net/2011/03/what-is-a-content-management-assessment.html).

  

Nearly all content management systems have flexible repositories that allow you to control how content is structured. This is important because every organization's content is different just like every website is different. But this flexibility can also be a liability because it creates opportunity for bad design as well as good design. Content can be under-structured, over-structured, or wrongly structured. Asking the right questions will help you assess how effective your content was modeled. 

   

  
 *   
    
    ### Do your contributors spend a lot of time formatting content?
    
      
     If your content contributors spend a lot of time formatting, it may mean that your content is not structured enough. Look out for "formatting patterns" where a content contributor repeats a format pattern to give the illusion of structure. For example, if the by-line and date-lines of articles are stored in the main body and distinguished by a particular font treatment, those should probably be fielded elements. The risk of letting this go is that it reduces flexibility. The only way to change how a by-line looks is to go into each article and change the formatting.  
     
  
 *   
    
    ### Do your content contributors feel like data the entry aspect is overshadowing the creative process?
    
      
     While structure is generally a good thing, too much can be stifling to the overall goal of content: communication. Most content contributors need a blank palette to rearrange and massage information until it tells the right story. Filling out endless form fields breaks that flow and never allows the creative process to take root. A good example is forcing a user to enter the body of a semi-structured content asset into a series of paragraph fields rather than one rich text field. A series of paragraph fields makes it hard for the author to re-arrange content and split and merge paragraphs. A good clue that your content entry interface is overly cumbersome is if content contributors wait until the very end of the editorial process to enter content into the CMS.  
     
  
 *   
    
    ### Do you frequently find yourself wishing for a global (as in site-wide) search and replace?
    
      
     On one CMS selection, I received a requirement for a global search and replace. The reason for this requirement was a recent episode where the organization's phone number changed and they needed to update every press release because the contact number was embedded in the body field below the rest of the article. Not everything that a visitor sees on the page has to be entered by a content contributor. Some of the page can be hard-coded into display templates. Other parts of the page can be managed as global content components. In this case, it would have been better to embed the phone number in the press release display template below the body copy. If the phone number was likely to change frequently, a global content component would allow a content contributor to edit this information in one place and without the assistance of a template developer.  
     
  
 *   
    
    ### Do content contributors find themselves duplicating the same text over and over again?
    
      
     A content management system is not doing its job if contributors are not effectively reusing content. The classic example is an article list and detail page. If content is structured properly, the article headline exists in only one place: in the article. The list page queries the articles and lists their headlines. If the headline exists in two places, it needs to managed in two places. Now, this is an obvious example and it is shown in nearly every CMS demo that I have seen. A less obvious example is a promotional element — some block of display that promotes some messaging or a product. You want to manage those as components that can be re-used in different places on the site. I call this [keeping your content DRY](http://www.contenthere.net/2010/07/keeping-your-content-dry.html). With better reuse, you can manage less content and still support the same visitor experience. The downside to reuse is that it makes specialization hard, you can't change the wording in one place without it affecting all other occurrences of that content. You need to make decisions about whether specializing a piece of content is worth the additional management overhead.   
     
  
 *   
    
    ### Do content contributors overload or misuse content attributes?
    
      
     A hallmark of an un-maintained content management solution is when content contributors start to get creative and misuse content elements to achieve the behavior that they want. [Deane Barker has an excellent presentation on this called "Just Put That in the Zip Code Field"](http://www.gadgetopia.com/post/6853). This warning sign means that the requirements for the solution have changed but the solution has not adapted. It is a big issue when your content contributors care more about the website more than the support team. On the plus side, this means that you have established ownership over the content. On the negative side, the organization as a whole is either unwilling or incapable of supporting that ownership. If you see these signs, you need to get in gear and honor content contributors' commitment by taking better care of the solution.  
     
  

  

The good news is that most content management systems will allow you to correct content modeling inefficiencies — but with certain limitations. First, content management systems tend to have [different strategies for managing content: page based or object based](http://www.contenthere.net/2009/06/pages-and-objects.html) and the extent of available data types varies from product to product (again, check out [Deane's presentation](http://www.gadgetopia.com/post/6853)). Second, going from more structure to less is easier than going from less structure to more. You can automatically concatenate multiple fields into one; it is harder to arbitrarily split large unstructured elements into multiple structured elements. Third, some content management systems have better utilities for doing bulk content transformations than others.  

As a quick little exercise, try to prototype and alternative content model and ask your content contributors to give feedback. They may feel like they have a whole new lease on their content.
