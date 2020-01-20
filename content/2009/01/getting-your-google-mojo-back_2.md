Title: Getting your Google mojo back
Date: 2009-01-02T10:39:00.001Z
Modified: 2015-01-06T12:15:40.692Z
Category: misc
Tags: 
Slug: 2009/01/getting-your-google-mojo-back_2
Authors: Seth Gottlieb

<a href="http://www.flickr.com/photos/sggottlieb/3146525945/" title="Google, why do you hate me so? by sggottlieb, on Flickr"><img alt="Google, why do you hate me so?" height="459" src="http://farm4.static.flickr.com/3130/3146525945_46d85b57b2.jpg" width="500"/></a>  
  
When I migrated [Enter Content Here](http://www.contenthere.net) off of [Blogger](http://www.blogger.com), moving the content and comments was really easy - literally just the click of a button.  This was a nice surprise because my expectations were based on a typically painful CMS migration.  Because I use [FeedBurner](http://www.feedburner.com), my RSS readership experienced little disruption either.  I already had moved my Blogger blog to a custom domain and WordPress allows you to format your own permalinks so it was easy to map the old URLs to the new with a simple Apache Rewrite Rule.  Within my blog.contenthere.net virtual host of my hosting provider, I created the rule:  
>    
> RewriteRule .\* http://www.contenthere.net%{REQUEST\_URI}  
  
The one piece of the move that proved to be an issue was getting Google to update its index and move entries from blog.contenthere.net to [www.contenthere.net](http://www.contenthere.net).  This was particularly problematic because I wanted to use the [Google Custom Search Plugin for WordPress](http://aleembawany.com/projects/wordpress/google-custom-search-plugin/) so I could include [product pages](http://www.contenthere.net/products-page) and other content in my search results.  I submitted a dynamically updated [Sitemap](http://sitemaps.org/) (using the [Wordpress Sitemap Plugin](http://www.arnebrachhold.de/projects/wordpress-plugins/google-xml-sitemaps-generator/)), Google ignored all of my entries (see image on top).  
  
I learned from the support forum that Google probably thought that these new pages (under www.contenthere.net) were duplicates of the blog.contenthere.net pages and was skipping them.  I don't really understand why that is because there is no way that the rendered pages could be identical.  I just had to take it on faith.  The only way to get Google to update its index is to configure your rewrite to send down a status code of 301 (permanent redirect).  The updated rewrite rule looks like this:  
>  RewriteRule .\* http://www.contenthere.net%{REQUEST\_URI} \[R=301\]  
  
While I was at writing rewrite rules, I added a few more to handle the situations where WordPress's permalink algorithm was different than Blogger's.  The biggest difference is that Blogger omits "The" and "A" from a post title when building a permalink.  There were also discrepancies where I changed the title of the post after publishing.  
  
To improve my custom Google search in the short term, I added the site blog.contenthere.net to the list of indexed sites.  This way people using the onboard search can still find the pages that have not yet been re-indexed and, when they do, Google should get the 301 code.  
  
As for my old blogger blog (contenthere.blogspot.com), I did everything I could to make it as ugly and unappealing as possible.  I wrote messages explaining the move all over the template.  What I really wanted to do was have a link from each post to the new URL.  However, there is no path variable that would allow me to construct a new link by concatenating the new domain (www.contenthere.net) to the current path.  Blogger just has a tag for the full URL (data:post.url) and I couldn't find syntax for substrings.  I could have done it with Javascript but didn't want to bother.  Instead, I inserted a search form for my custom search in each post and preloaded it with the blog post title.  This approach has the additional benefits of potentially giving the visitor more recent content and also sending them through Google to give it another chance to update its index.  I have a free statcounter collecting traffic statistics on that site.  When it gets down to 0, I will probably delete the whole blog.  
  
Since making these changes, my search based traffic is back to its pre-migration levels.  Google still doesn't seem to take an interest in my Sitemap but that doesn't seem to matter.  Through the process, I have learned that originally hosting my blog on Blogger did not lock me into the platform.  Instead, it allowed me to focus on the content and quickly establish a voice in the blogosphere without worrying about infrastructure.  Blogger's support of custom URL's was critical to minimizing lock-in.  When I migrated to a custom domain, Blogger helped route traffic from the blogspot URL to the new one.  This put me in a good position to move to the blog to any platform I chose.
