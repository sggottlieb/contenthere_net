Title: CMS Architecture: Managing Content Type Configurations
Date: 2010-01-19T16:54:00Z
Modified: 2015-01-06T12:16:16.147Z
Category: misc
Tags: architecture
Slug: 2010/01/cms-architecture-managing-content-type
Authors: Seth Gottlieb

Warning: this post is highly technical. Non-programmers, please avert your eyes.

  

[Deane Barker](http://gadgetopia.com/) (from [Blend Interactive](http://blendinteractive.com/)) and I have a running conversation about CMS architectures. One of the recurring topics is how content models and other configuration is managed. There are two high-level approaches: inside the repository and outside the repository. Both have their advantages and disadvantages.

  

*   __Managing content types outside the repository__
    
    My preferred approach is to manage content type definitions in files that can be maintained in a source code management system. This way you can replicate a content type definition to different environments without moving the content. Developers can keep up to date with changes made by their colleagues. [Configuration can be tested on Development and QA before moving to production.](http://www.contenthere.net/2009/07/code-moves-forward-content-moves-backward.html) There is no user-interface to get in the way. No repetitive configuration tasks. Everything is scriptable and can be automated. I especially like it when content types are actual code classes so you can add helper methods in addition to traditional fields. Of course, when you get into this, it is a slippery slope into a tightly coupled display tier that can execute that logic.  
    
    
    
    
    On the downside, it is often difficult to de-couple the content (which sits in the repository) from the content model (which defines the repository). When you push an updated content type to a site instance, you might need to change how the content is stored in the repository. This is more problematic in repositories that store content attributes as columns in a database. It is less of a problem in repositories that use XML or object databases (or name-value pairs in a relational database) where content from two different versions of the same model can coexist more easily.  
    
    
    
    
    If you do manage content type definitions outside of the repository, a good pattern to follow is [data migrations, which was made popular by Ruby on Rails.](http://guides.rubyonrails.org/migrations.html) I am using a similar [migration framework for Django called South](http://south.aeracode.org/). Basically, each migration is a little program that has two methods: forward and back ("up" and "down" in RoR. "Forwards" and "backwards" in South) that can add, remove, and alter columns and also move data around. The forward updates the database, the backward reverts to the earlier version.
    
      
    <li><strong>Managing content types within the repository</strong><p>Most CMSs follow the approach of managing the content type definitions inside the repository and provide an administrative interface to create and edit content types.  This is really convenient when you have one instance of the application and you want to do something like add a new field.  There is no syntax to know and application validation can stop you from doing anything stupid.  Some CMSs allow you to version content type definitions so that you can revert an upgrade.<br/></p><p>When you have multiple instances of your site, managing content types can be tedious and error prone if you need to go through the administrative interface of each instance and repeat your work.  Of course, you can't copy the entire repository from one instance unless you want to overwrite your content.  If your CMS is designed in this way, you should look for a packaging system that allows you to export a content definition (and other configurations) so that it can be deployed to another instance.  Many CMSs allow an instance to push a package directly over to another instance.  The packaging system may also do some data manipulation (like setting a default value for a required new field).<br/></p></li>

  

Unless you are building your own custom CMS, this all may seem like an academic question. It really is quite philosophical: is configuration _content that is managed inside the application_ or does it need to be managed _as part of the application_. The same thing goes for presentation templates (but that is another blog post). However, if you intend to select a CMS (like most people should), it is important to understand the choice that the CMS developers made and how they work around the limitations of their choice. If you are watching a demo, and you see the sales engineer smartly adding fields through a UI, you should ask if this is the only way to update the content model and if you can push a content type definition from one instance to another. If the sales engineer is working in a code editor, you need to ask how the content is updated when a model update is deployed.  
