Title: Good story about metadata capture
Date: 2006-01-25T20:50:00.002Z
Modified: 2015-01-06T11:32:16.797Z
Category: misc
Tags: 
Slug: 2006/01/good-story-about-metadata-capture_81
Authors: Seth Gottlieb

Lars Plougman's story [about a lawyer's scheme to work around a document management system](http://www.mindthis.net/mindthis/2006/01/feeling_good_ab.html) points out a huge issue in content management. The natural tension between creators and consumers of content. Content creators create content for their own purposes and don't like to spend the extra effort to add metadata that is only useful to other users and systems. In fact, I often distrust voluntary metadata because, as [as I mention in an earlier post](http://contenthere.blogspot.com/2006/01/gsa-meta-data-not-essential-for-search.html), users either neglect or abuse metadata. Consumers of content, however, benefit from good metadata because they allow readers to quickly identify content that is useful to them.  

It is interesting that the solution that Lars' story presents uses a third party intermediary to take the content and properly enter it into the system with the correct profile information. The more I think of it, the more I am thinking that this is a good idea and it actually maps to something that I do at Optaros.  

We use [Subversion](http://subversion.tigris.org/) as our source control system and have set up a SVN commits mailing list (more about that [here](http://contenthere.blogspot.com/2005/03/managing-projects-open-way.html)). As I read the checkin emails, in addition to seeing what people check in, I can see who has been naughty and nice with their checkin comments (which are metadata!). If someone gets lazy with the comments, I give them a friendly reminder. Otherwise, it would not be until much later, when we need to roll back some code, that we would realize that the comments were not helpful (I know whoever is reading this is thankful that they don't work with me!). Usually just the knowledge that people are looking makes contributors more meticulous about their comments.  

 

The most common way to enforce metadata is through input validation (like in the case of the lawyer's document management system). Users hate it and that is the first thing people point to when they talk about how unusable their system is. It strikes me that making content creators write their own metadata is relatively new and maybe it doesn't work. Formal publishing environments typically have authors write stories and editors compose headlines and place stories. Lawyers are usually pampered with admin staff so they historically have been removed from the mechanics of creating documents and metadata (although that is changing). The librarian profession specializes in metadata and organization. Is it unrealistic to expect content creators to manage their own metadata? Or should we return to inserting metadata specialists into the process after content creation, either as police like me with my commits list, or as metadata editors like the secretary in Lars' story. Can we afford to do that? Can we afford not to?

I am looking forward to seeing your comments.  

 

  
