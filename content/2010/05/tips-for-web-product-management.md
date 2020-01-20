Title: Tips for Web Product Management
Date: 2010-05-11T14:01:00Z
Modified: 2015-01-06T12:16:17.002Z
Category: misc
Tags: development, Product Management, Content Strategy
Slug: 2010/05/tips-for-web-product-management
Authors: Seth Gottlieb

I am currently providing web product management services for two clients. One client is a start-up launching a new web-based product. The other is a 100 year old newspaper. While at face value these two clients couldn't appear to be more different, they are actually quite similar. Both are trying to innovate a viable product. The startup is building a new concept. The newspaper is a trying to re-imagine an old concept. In both cases the development backlog is a chaotic mess of items that range from little tweaks to major features. There is impatience for progress; but that urgency needs to be balanced with the need to build something that is scalable and sustainable if the business succeeds. The truth is most websites operate under these conditions to some degree. It is just the ambition of these two businesses raises the stakes and the stress level.  

To be successful in these projects, I have had to draw on lots of different skills and experiences. Many of the concepts and techniques come from agile methodologies like [Scrum](http://scrummethodology.com/) and [Lean software development](http://en.wikipedia.org/wiki/Lean_software_development). What follows is a list of principles and practices that I have found to be effective.

  

*   
    
    __Establish a regular (2-3 week) release cycle__. Everyone benefits from a regular release cycle. Stakeholders get the satisfaction of seeing progress. They don't panic if one of their requests doesn't get into the current release if there is a chance that it will be addressed in a subsequent release. The sooner a new feature hits the production site, the sooner it can be measured and improved. Shorter development cycles also mean smaller releases that are easier to test. Site visitors perceive a constantly improving site as being vibrant.  
    
    
    
*   
    
    __Define and communicate prioritization criteria__. In order to keep releases small, you need a clear and open scoping process. Enhancement requests need to be evaluated against the site goals (such as creating new revenue opportunities, cutting costs, maintaining credibility, etc.). Without this kind of guidance, development gets chaotic. Developer time is not concentrated on work that matters. The pipeline tends to get clogged with small tweaks; larger, more substantial improvements never get done.  
    
    
    
*   
    
    __Make each release a blend of stakeholder-focused improvements and code maintenance__. When code is not regularly optimized and refactored, entropy takes over and it becomes less maintainable. Development teams that are exclusively driven by stakeholder requests don't have time to keep the codebase clean. A [broken window effect causes messy code to beget messy code.](http://pragprog.com/the-pragmatic-programmer/extracts/software-entropy) For this reason every release milestone should contain a balance of improvements that stakeholders see (new functionality, presentation template changes, etc.) and maintenance tasks (refactoring code, improving management scripts and infrastructure, etc.). By maintaining this discipline, the quality of the application improves (rather than degrades) over time.  
    
    
    
*   
    
    __Don't forget the HotFix queue__. Even though you might have a methodical development plan, emergencies happen. In addition to regularly spaced released milestones, I typically create a "HotFix" milestone with a rolling due date of "yesterday." Emergency requests go into the HotFix queue and get addressed and deployed immediately. Of course, only I can put things into the HotFix queue and I base that decision on very specific criteria: current functionality is compromised, inaction is costing money (or some other measure of value like reputation), and it is a quick fix.  
    
    
    
*   
    
    __Write good tickets__. Every change request gets entered in a ticket tracking system. Bug requests should be extremely descriptive: URLs, screenshots, steps to reproduce. Feature requests take the form of a full specification complete with annotated wireframes or mockups. Every new element shown needs an annotation describing the source of information and behavior. It is also a good idea to put in test conditions so that the QA staff know how to verify it is working.  
    
    
    
*   
    
    __Use your source code control system effectively__. Create tags to remember milestones in the development history. Use branches only when you are simultaneously working on two versions of the application. The most likely reasons for branching are:
    
      
     
    
    *   Having a production branch for hotfixes while development for the next release is done on trunk.  
         
    *   Using an experimentation branch for functionality that may or may not make it into the main code line.  
         
    
    
      
    
    
    Don't use branches for personal work areas or to manage environment-specific configurations. Merging will be a pain and it will delay any integration testing you will need to do.
    
      
    
*   
    
    __Automate deployments__. Deployments should be simple and mindless. There should be one step to push the same exact code that was tested on the QA environment to the production environments. If someone needs to manually copy individual files, you are doing it wrong. At a previous client (a very large magazine publisher), we used [AnthillPro](http://www.anthillpro.com/html/default.html) for [continuous integration](http://martinfowler.com/articles/continuousIntegration.html) and deployments. Each build of the application was stored in an build artifact library where it could be deployed to different environments with a push of a button. There were cool reports that showed you want build number was deployed where. But that was for managing 50+ applications across hundreds of servers. Now I am using lighter weight tools like [Fabric](http://docs.fabfile.org/0.9.0/) to script builds and deployments.  
    
    
    
*   
    
    __Build a talented and committed team__. I strongly believe that there is no room for mediocrity on an agile development team. Working in this way requires a lot of trust. Stakeholders need to trust that developers are working efficiently and doing necessary things. Developers need to rely on each other to communicate and make good decisions. You don't get that trust unless developers know the technology and are passionate about their craft.  
    
    
    

  

If the website or web application that you manage _is your product_ (or is critical to deliver your product), you need to manage it with this level of discipline and rigor. Otherwise the site will stagnate and you will be unprepared to respond to new market challenges and opportunities.
