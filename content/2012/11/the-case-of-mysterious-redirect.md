Title: The Case of the Mysterious Redirect
Date: 2012-11-08T12:47:00Z
Modified: 2015-01-06T12:30:24.784Z
Category: misc
Tags: development, Apple, OSX
Slug: 2012/11/the-case-of-mysterious-redirect
Authors: Seth Gottlieb

Like most technical people, I have many development environments running on my local workstation. &nbsp;I use a configuration of Apache virtual hosts and my /etc/hosts file to keep them sorted out. &nbsp;It normally works great but yesterday I solved a vexing issue and &nbsp;I thought I would share.  
  
The issue was that whenever I hit a specific development environment, it would redirect me to my blog (<http://www.contenthere.net>) with a path that was based on the location of the Apache doc root. &nbsp;I hadn't used this environment in a while and so a lot of things could have caused the problem. &nbsp;At first I thought it was a DNS issue. &nbsp;Then I was certain it was an Apache configuration issue.  
  
After trying all sorts of things, I realized that I had accidentally saved some .htaccess file to the root of my home directory. &nbsp;The doc root of this particular development environment (which was inside my home directory) didn't have its own .htaccess so Apache traversed up the directory structure to find one and applied the rewrite rules within it. &nbsp;Deleting this file made the problem go away.  
  
I suspect that I accidentally copied the errant .htaccess file from a server by double-clicking on it in my FTP client. &nbsp;I had no idea that Apache would behave in that way. &nbsp;I spent ages searching through Apache configurations and the doc root. &nbsp;I looked into issues that might have been caused when I upgraded to Mountain Lion. &nbsp;But I didn't look in the root of my home directory until I searched for all of the .htaccess files on my machine.  
  
One thing that I learned from troubleshooting (in addition to .htaccess behavior) was about [DNSMasq](http://blog.philippklaus.de/2012/02/install-dnsmasq-locally-on-mac-os-x-via-homebrew/). &nbsp;It allows you to create wildcard entries like .dev, which saves a lot of effort editing the /etc/hosts file. &nbsp;Pretty cool! &nbsp;So it wasn't a total loss of time.  
  
Hopefully someone will learn from my experience.
