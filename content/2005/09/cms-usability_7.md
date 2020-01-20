Title: CMS Usability
Date: 2005-09-08T18:11:00.002Z
Modified: 2015-01-06T11:32:15.134Z
Category: misc
Tags: simplicity, usability
Slug: 2005/09/cms-usability_7
Authors: Seth Gottlieb

While catching up on my Blog reading, I noticed [this post](http://www.cmswatch.com/Trends/507-CMS-without-early-user-testing:-%22disaster%22) on [CMS Watch](http://www.cmswatch.com) which links to an [InfoWorld](http://www.infoworld.com) case study of a project that was almost ruined by lack of user testing. I very much agree with Tony Byrne's point that usability is one of the biggest issues in the CMS industry and I am happy that Tony is being so vocal ([one article](http://www.econtentmag.com/Articles/ArticleReader.aspx?ArticleID=7732&amp;Query=usability), [another article](http://www.econtentmag.com/Articles/ArticlePrint.aspx?ArticleID=7936)) about defining the problem and challenging the industry to fix it. James Robertson, of Step Two Designs, has also added his respected opinion to the discussion with a [fine article](http://www.steptwo.com.au/papers/cmb_moreequalssimpler/index.html) on the importance of simplicity in large CMS deployments.   

A CMS is one of those applications like a word processor where many users, often non-technical users, need to become proficient with no little or no training to get their job done. Frequently CMS users are under time pressure and, if it is quicker to misuse the tool than to use it properly, the tool will be misused - or, if possible, not used at all. Content Management is a very broad term but I think this applies to everything from this blogging software that I am using right now, to a Web CMS, to a document management application. A CMS user wants to publish what needs to be published with as little overhead as possible. As a matter of personal pride, author's want their content to read well and look good. But other than that, the less time spent with a CMS, the better.  

Producing content is also a creative process and content creators don't like to feel like data entry people. CMS users don't like to waste time tagging their content with metadata. They frequently rebel when forced to fill in structured forms and give up the artistic license to determine how their content will be displayed.  

But on the other side, are the consumers of the content. They are important users too. They want to be able to find the information they need (which requires good metadata) and get in a format that is accessible to them. The latter requires separation of content and layout so that content can be re-purposed to different formats. As Yair Dembinsky eloquently put it in a post on the [CM Professionals](http://www.cmprofessionals.org/) mailing list:  
>  Our main focus should be the target audience - how they want to consume the content: In some cases - they want a well written article, and in others they want to be able to retrieve small but relevant chunks of information. Writers and editors must adapt to supply the specific need of their target audience.  

So, the CMS is stuck in the middle between the content contributors and managers and the content consumers. Both sides want their jobs to be easier and simpler. Some of the answer lies in automation adding information (metadata) and structuring a content asset for better reuse. But that only takes you so far. We don't want to rely on the system too much to interpret our content and make false assumptions. Workflow helps too by creating an opportunity to divide responsibility between those who create content and those who organize and classify content. However, companies typically under-invest in this area and do not dedicate editors to this task  

At the end of the day, the CMS will always be a compromise between the efficiency of creating content and the utility and re-usability of the content. Content Management is a challenging problem. So what can we do to make it better?  

One initiative that is just starting a new project on [Open Usability](http://www.openusability.org) called [CMS User Interface Guidelines](http://www.openusability.org/projects/cms-uig/). I hope that this project gets some traction because I think there is a lot of potential here. Unfortunately the cards are somewhat stacked against it because usability is such a nebulous thing and people are more likely to complain about usability than to do something about it. I think success will lie in the ability to set down some common metaphors and idioms that users are familiar with so that they can quickly get their bearings in the application.   

Like Microsoft Windows or hate it, there are some conventions that make all Windows applications familiar enough so that a new user does not get totally lost. For example, the File Menu is always on the left, Help is on the right. Ctrl-C is Copy, Ctrl-V is paste (except when you are using Intuit Quicken where they are "Categorize" and "Void". Grrr. How can you people call yourself Intuit!?). Microsoft also achieved high level of adoption for its Office applications Word and Excel by copying the UI functionality of then market leading applications WordPerfect and Lotus 1-2-3. Consistency is the key. An application does not have to be intuitive if all the users are familiar with it. Remember going to a travel agent not so long ago and watching him or her zip around the SAABRE terminal with two character codes?  

Another area where things can be improved is the standardization of terminology. Different CMS products have different names for things. For example, in response to another CMS list request for different names for sub-components of content, Tony Byrne of CMS Watch listed the following:  

*   Elements  
    
*   Snippets  
    
*   Objects  
    
*   Placeholders  
    
*   Pagelets  
    
*   Styles  
    
*   Chunks  
    
*   Briicks  
    
*   Parts / Fragments  
    
*   Nodes / Fields  
    
*   Components

  
Standardization in naming, design, and behavior will not only help CMS become easier to learn; it will also create a community that crosses organizational boundaries and includes both developers and users that can work together to solve this very difficult problem.  

While standardization will help improve "out-of-the-box" functionality and the underlying framework of the application, in reality, CMS are usually heavily customized to work within the business context (perhaps more than they need to be, but that is another story). This is where the CMS is not a build vs. buy, it is a build vs build AND buy. Most CMS projects spend 2 to 3 times the license cost on integration. To get these customizations right, I would say usability testing is an understatement.   

The worst thing you can do is spend a lot of time on gathering abstract requirements and creating abstract designs, then select a product, then do detail design with the users, then implement it, then test it and _finally_ run it through usability testing. Any issues found that late in the process will be too expensive to fix - too expensive because you are at the end of the project and you are out of time and money. When you test this late in the game, you are basically just hoping that the users just rubber stamp what you did. And if that is the case, why test at all?  

What I would recommend is have usability testing _drive_ the design rather than validate it. Select a product, install it and show it to the users in its out of the box state. Ask them what is wrong with it. Prioritize a bunch of modification requests, implement them, then show the application to the users again. Repeat this cycle until the benefit of the modification is outweighed by the cost of implementing it. This approach, which, for lack of a better name, I call "change driven development" (a nod to Peter Coad's "Feature Driven Development"), gives business users a chance to experience the default behavior which may not be that bad - especially if not modifying the feature leaves more budget for improving another feature. In  
 addition to helping business users make better choices in design, involving the users at this stage of the project builds their comfort level and ownership of the application and leads to less complaints after it is deployed.   

Business users know their job. They know the tools that they use. But one of the things they have the hardest time with is imagining something new and thinking abstractly. They are too immersed in the concrete of their day to day to think outside of their box. They are even worse at understanding the scope implications of their requests. So the result of waterfall approach to CMS customization is that we force users to think blue sky and, just when they get comfortable, we slam them down with admonitions of scope creep. Then we ask them to test the application for usability and we ignore their feedback. This is a recipe for failure and disappointment.  
