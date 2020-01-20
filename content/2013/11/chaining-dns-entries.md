Title: Chaining DNS Entries
Date: 2013-11-25T08:44:00Z
Modified: 2015-01-06T12:30:25.417Z
Category: misc
Tags: Technical Strategy, Web Operations
Slug: 2013/11/chaining-dns-entries
Authors: Seth Gottlieb

Warning: geeky network admin post

  

I see a clear trend of marketing groups taking over [full responsibility for their organization's digital presence](http://contenthere.net/2008/07/product-it-vs-enterprise-it.html). This includes maintaining various publishing systems such as the web content management system and running the website hosting infrastructure. Once you go down this path, you need to get with IT and start dividing up ownership of the different systems. Some of these decisions are easier than others. But the hardest one is often the DNS — which maps domains and subdomains to actual servers. Both groups have a legitimate claim over the name server. IT needs to make sure that email and other back office systems are properly mapped. Marketing needs to be able to route external audiences to the right applications. Both groups are afraid of the other group accidentally causing an outage by deleting or updating domain records that they shouldn't be touching.

  

To work around this problem, I recommend chaining DNS entries across two sets of name servers like this:

  

<a href="http://www.flickr.com/photos/sggottlieb/10932850424/" title="Chaining DNS Entries by sggottlieb, on Flickr"><img alt="Chaining DNS Entries" height="158" src="http://farm4.staticflickr.com/3809/10932850424_44a9144f1d.jpg" width="500"/></a>

  

In this pattern marketing registers a domain for its private use. What the domain looks like doesn't matter because nobody will see it. Then marketing sets up DNS entries for public subdomains like www and points them to the IP addresses of the servers or other network infrastructure (like load balancers) that host the sites. Then the IT group create DNS (CNAME) entries in their name servers that point to the marketing entries. The end result is that a browser looking for the IP address behind www.example.com will be referred to get its answer from www.examplemktg.com, which will return the correct address. 

  

Why is this useful? If marketing wants to temporarily or permanently move a site onto different hardware, no coordination is needed. Marketing has full control over what the domain is mapped to. This may not sound like a big deal but imagine it is 3AM and your primary hosting infrastructure goes down. [Relief from your disaster recovery setup is just a DNS update away](http://contenthere.net/2013/01/monitoring-your-hot-standby.html). But the IT help desk is offline or can't reach anyone from network operations to make the change. Your urgent request would just have to wait as audience associates your brand with 500 or Server Not Found errors.
