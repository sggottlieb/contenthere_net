Title: Small Deployments
Date: 2013-08-21T12:38:00Z
Modified: 2015-01-06T12:30:25.349Z
Category: misc
Tags: DevOps, development, Product Management
Slug: 2013/08/small-deployments
Authors: Seth Gottlieb

Last week, when we released a new version of [Lionbridge onDemand](https://www.liondemand.com), I was reminded of a valuable lesson: keep your deployments small. Up to that point, we had been upgrading the production environment on a regular basis — nearly daily. When a new feature was ready, we deployed it. But this development iteration had some systemic improvements (new service types, enterprise features…) so we held off to release everything at once. That was a mistake. The problem was that lots of configuration changes had been building up (new settings, new libraries on the server, etc.) and that led to a lot more work at launch time. As you would expect, some steps were missed that compromised functionality. It wasn't a huge deal. Nothing was obviously broken. There were just some "Oh SNAP!" moments along the way.  

Thanks to that reminder, we are back on schedule with regular code deployments. Some of the updates will be "under the waterline" — invisible changes to the underlying architecture to support visitor facing features that we are still working on. The trick is to keep the back-log of un-deployed code to a minimum. In addition to reducing the risk of the actual deployment, smaller upgrades make it easier to troubleshoot issues because there are fewer potential causes. For further reading on this topic read Eric Reis's chapter on Continuous Deployment in [Web Operations: Keeping the Data On Time](http://www.amazon.com/gp/product/B0043M4Z34/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B0043M4Z34&amp;linkCode=as2&amp;tag=contenthere-20)

<img alt="" border="0" height="1" src="http://ir-na.amazon-adsystem.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=B0043M4Z34" style="border:none !important; margin:0px !important;" width="1"/>

. David Hobbs also has some great articles on this topic in relation to website launches. The one that springs to mind is [Site Launches: do as little as possible](http://hobbsontech.com/content/site-launches-do-little-possible). Also, to work in this way, it is also critical that you use a mature code management strategy. A couple of months ago my team adopted the [Git Flow branching strategy](http://nvie.com/posts/a-successful-git-branching-model/) and it has been a huge help.  

People getting used to this model of product management will find it counter-intuitive. They see upgrades as risky, scary things and the natural tendency is to avoid them. But the more you delay an upgrade, the scarier and riskier it gets. And that creates a vicious circle. Even if you know and agree with the small deployment approach, it is easy to justify delaying an upgrade because you want to do one more thing. That is what happened to me. 
