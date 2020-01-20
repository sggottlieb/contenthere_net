Title: SiteChecker Plugin for ServerDensity
Date: 2013-02-11T08:15:00Z
Modified: 2015-01-06T12:30:24.913Z
Category: misc
Tags: Web Operations
Slug: 2013/02/sitechecker-plugin-for-serverdensity
Authors: Seth Gottlieb

A couple of weeks ago I wrote a post describing [how to make sure that your fail-over sites are running properly](http://www.contenthere.net/2013/01/monitoring-your-hot-standby.html). At the time, I was sending the results via email. Since then, I improved the process by turning the logic into a ServerDensity plugin (I mentioned that we use ServerDensity here: [Marketing I.T. in the Cloud](http://www.contenthere.net/2012/12/marketing-i-t-in-the-cloud.html)). It was pretty easy to do. The only thing even remotely clever that I did was cache the results in a file so that I didn't have to check the sites every 5 minutes (which is the ServerDensity agent run frequency). [Here is the code](https://gist.github.com/4709892)

  

<script src="https://gist.github.com/sggottlieb/4709892.js"></script>
