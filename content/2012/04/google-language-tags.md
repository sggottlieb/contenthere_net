Title: Google Language Tags
Date: 2012-04-11T10:02:00Z
Modified: 2015-01-06T12:30:24.251Z
Category: misc
Tags: localization, Global Marketing Operations
Slug: 2012/04/google-language-tags
Authors: Seth Gottlieb

If you were not able implement a [host-based strategy for your Global Business URLs](http://blog.lionbridge.com/marketing/2012/01/31/url-management-for-a-global-business/), you might be able to implement [Google's rel-alternate-hreflang tag](http://support.google.com/webmasters/bin/answer.py?hl=en&amp;answer=189077&amp;topic=2370587&amp;ctx=topic). This article, [Giving Google better instructions about language and country](http://www.dot-connection.com/2012/03/giving-google-better-instructions-about-language-and-country/), provides a good explanation.  

The basic gist is that if you are hosting multiple localized sites on the same host and using paths to keep them separate, Google is going to think that your UK site is just a duplicate of your US and just index those pages once. This will send UK traffic to your US site and undermine the value of your localization. Putting this link tag in the HTML head

  
<code><br/>    &lt;link rel="alternate" hreflang="en-GB" href="http://www.example.com/en-GB/about" /&gt;<br/></code>  

will tell Google that there is a UK version of your US about page under /en-GB/about.  

Reading through the Google documentation, it is probably a good idea to use this tag even if you have your different localized sites under different hosts. It can't certainly hurt.
