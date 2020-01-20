Title: Open Source Governance within the Enterprise
Date: 2006-07-28T16:27:00.002Z
Modified: 2015-01-06T11:32:18.970Z
Category: misc
Tags: 
Slug: 2006/07/open-source-governance-within-enterprise_95
Authors: Seth Gottlieb

I recently spoke to a friend of mine, who works for a large financial services company, about their open source policies and practices.  The big financial services companies are, in general, slightly ahead of the curve in their use of open source.  That, and the fact that they are also highly regulated and have a potential high risk exposure, makes financial services a good place to look for open source governance models.  Why do you need an open source governance policy and procedures? Because open source software can be acquired differently than commercial software.   Unlike commercial software whose acquisition can be regulated as it goes through a budgeting and accounting process, open source can be freely downloaded and used without institutional awareness.  
  
Like it or not,  your company is probably using more open source software than you are aware of.   In fact, if you are building web applications in anything but [.NET](http://www.microsoft.com/net/default.mspx), I would be surprised if you didn't use some open source framework or development tool in your custom application.  You would be crazy not to.  Companies that have not adapted to the existence of open source usually have what I call a "flavor of the month" architecture where the next application is built on what was written about in the last post on [Slashdot](http://slashdot.org/)  or [The ServerSide](http://www.theserverside.com/).  I am not saying variety is a bad thing.   There just needs to be a reason to use something different - like different requirements.  
  
Here are some things that this company does to manage software in a world where open source exists.  I have heard similar processes at other major companies that I have spoken to so this company is not unique.  

*   Define what open source is. They exclude Linux (which they consume like commercial software with support contracts and all) and open source software bundled in commercial products.
*   Accept that open source is out there and has potential value.
*   Sponsor a cross line of business open source review board. This organization is responsible for responding requests to use a new open source application.
*   Manage a list of all usages of open source software within the firm. If you want to use an open source application, for research or production purposes, you consult the list for the software and version that you want to use. If you find it being used, you communicate your use to the "open source librarian." If it is not currently being used, you submit a request to the open source review board. They will tell you if there is a preferred alternative or put it on the list.
*   Publish a handbook explaining the policy and processes around open source software.

Does this type of program scale down to smaller size companies with less technology discipline than a large financial services company?  I would say yes and, in some ways, it should be easier.  There does not have to be a dedicated review board.  An enterprise architect or architecture group should have an awareness of what software is running on the network: commercial and open source.  This knowledge will help them:  

*   Standardize on some core frameworks. This will reduce maintenance costs and help with interoperability. Again, homogeneity is not the goal. Especially in a web services world, applications do not have to be built on the same platform. You just need a better excuse to deviate from the standard than "I wanted to see what all the hype was about for [Ruby on Rails](http://www.rubyonrails.org/)."
*   Get to short lists of components quicker. It is easier to select from a list of pre-qualified options than comb [source forge](http://sourceforge.net) or [Freshmeat](http://freshmeat.net/) every time you want to use a component.  
    
*   Reuse your understanding of licensing implications. There are many open source licenses and some play better together than others.
*   Identify internal experts. If you know that an application was built on a technology, you can ask the developer who built it what they thought of the technology and best practices.  
    

  
So, if your company is using open source software (and, chances are, it is) it is best to get a handle on what is being used and how.
