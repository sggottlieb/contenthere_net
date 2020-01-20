Title: CMS Architecture: Managing Presentation Templates
Date: 2010-01-25T06:38:00Z
Modified: 2015-01-06T12:16:16.197Z
Category: misc
Tags: architecture
Slug: 2010/01/cms-architecture-managing-presentation
Authors: Seth Gottlieb

Another geeky post...

  

In my last post, [I described the relative merits of managing configuration in a repository vs. in the file system](http://www.contenthere.net/2010/01/cms-architecture-managing-content-type-configurations.html) but excluded presentation templates even though how they are managed is just as interesting. Like configuration, presentation templates can be managed in the file system or in the content repository. Like with configuration, if you manage presentation templates in the repository, you need some way to deploy them from one instance of your site to another without moving the content over as well.  

There are plenty of additional reasons why you would want to manage presentation templates on the file system. In particular, presentation templates are code and you want to be able to use proven coding tools and techniques to manage them. Good developers will be familiar with using a source code management system to synchronize their local work areas and branch/tag the source tree. Development tools (IDE's and text editors) are designed to work on files in a local file system. If you manage presentation templates in the repository you have to solve all sorts of problems like branching and merging and building a browser-based IDE or integrating with local IDEs. The latter can be done through WebDAV and I have also seen customers use an Ant builder in Eclipse to push a file with every time it has changed. Still, the additional complexity can create frustrating issues when the deployment mechanism breaks.  

As much as it complicates the architecture, there is one very good case when you would want to manage presentation templates in the repository: when you have a centralized CMS instance that supports multiple, independently developed sub-sites. For example, lets say you are a university and each school or department has its own web developer that wants to design and implement his own site design. This developer is competent and trustworthy but you don't want to give him access to deploy his own code directly to the filesystem of the production server. He could accidentally break another site or, worse, bring down the whole server. You could centralize the testing and deployment of code, but that would just create a bottleneck. You could do something like put the CSS and JS in the repository and have him go all [CSS Zen Garden](http://www.csszengarden.com/), but sooner or later he will want to edit the HTML in the presentation templates.  

In this scenario of distributed, delegated development, presentation templates are like content into two very important aspects:  

1.   presentation templates need access control rules to determine who can edit what.  
    
2.   presentations templates become _user input_ (and [user input should never be trusted](http://www.cmswire.com/cms/web-cms/how-they-hack-your-website-overview-of-common-techniques-002339.php)).  
    

  
The second point is really important. Just like you need to think twice when you allow a content contributor to embed potentially malicious javascript into pages, you need to worry that a delegated template developer can deploy potentially dangerous server side code. Once that code is on the filesystem of an environment it can create all sorts of mischief. It doesn't matter if it was intentional or not, if a programmer codes an infinite loop or compromises security, you have a problem. Using templating languages (like Smarty or Velocity) rather than a full programming language (like PHP or Java in JSP) will mitigate that risk but you still have to worry about the developer uploading a script that can run on your server. With staging and workflow, CMSs are good at managing semi-trusted content like presentation templates from distributed independent developers. There is a clear boundary between the runtime of the site and the underlying environment.  

If your CMS uses file-system based presentation templates and you delegate sub-site development to the departments who own them, you should definitely put in place some sort of automated deployment mechanism that keeps FTP and SSH access out of the developers hands and reduces the potential for manual error. The following guidelines are worth following:  

*   Code should always be deployed out of a source code system (via a branch or a tag). That way you will know what was deployed and you can redeploy the same tested code to different environments.  
    
*   Deployments should be scripted. The scripts can manage the logic of what should be put where.  
    
*   Every development team should have an integration environment where they can test code.  
    

  
One of my clients uses a product called AnthillPro for deployments of all web applications and also presentation templates. It has taken a while to standardize and migrate all of the development teams but now I don't see how you can have a de-centralized development organization without it.  

The other dimension to this problem is the coupling between the content model and the presentation templates. When you add an attribute to a content type, you need to update the presentation template to show it (or use it in some other way). The deployment of new presentation templates needs to be timed with content updates. Often content contributors will want to see the new attribute in preview when they are updating their content. Templates also need to fail gracefully when they request an attribute that does not yet exist or has not been populated yet. Typically, presentation templates evolve more rapidly than content models. After all, a change in a content model usually involves some manual content entry. In my scenario of the university, there is a benefit of centralizing the ownership of the content model. This allows content sharing across sites: if one department defines a news item differently than another department, it is difficult to have a combined news feed. Centralizing the content model will further slow its evolution because there needs to be alignment between the different departments.  

Wow, two geeky posts in a row. I promise the next one will be less technical.
