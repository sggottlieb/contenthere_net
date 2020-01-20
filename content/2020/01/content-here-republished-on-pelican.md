Title: Content Here Republished on Pelican 
Date: 2020-01-04T19:46:00Z
Modified: 2020-01-04T19:46:00Z
Category: misc
Tags: blogging
Slug: 2020/01/content-here-republished-on-pelican
Authors: Seth Gottlieb

I have been steadily reducing my Google footprint over the past year. I switched from gmail. I no longer use Google drive or photos. And, most recently, I migrated this blog from Blogger to a statically generated site hosted on Amazon S3. 

I use a framework called [Pelican](https://github.com/getpelican/pelican) to generate the full site from content files written in [Markdown](https://daringfireball.net/projects/markdown/). I am writing this post using a Markdown editor called [Typora](https://www.typora.io), although most text editors have very good Markdown support. Then I run a command that generates HTML files and pushes them to S3.

Migration was incredibly easy. [Google Takeout](https://en.wikipedia.org/wiki/Google_Takeout) allows you to export all your posts as an [Atom](https://en.wikipedia.org/wiki/Atom_(Web_standard)) file. Then I wrote a script that turned the Atom feed into Markdown files. It was easy to keep the same URLs thanks to the "blogger:filename" elements in the Atom file. For a template, I chose a theme called [Blue Penguin](https://github.com/jody-frankowski/blue-penguin).  After changing a couple of colors, I was done! 

I am still working out the finer points of the workflow. So far, the main limitation I see is that I can't post from any computer like I was able to do with Blogger (and before that Wordpress). Before being able to generate the site, you need to set up a local environment -- not hard thanks to GitHub and Pipenv, but not something that I would want to do on my work computer. Probably the next time I get inspired to blog while traveling, I will email myself a post to publish later.

Overall, I am pretty happy with this setup!



