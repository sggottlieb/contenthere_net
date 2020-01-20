Title: Daniel Jacobson on de-coupled publishing systems
Date: 2009-10-13T10:27:00Z
Modified: 2015-01-06T12:16:00.681Z
Category: misc
Tags: architecture
Slug: 2009/10/daniel-jacobson-on-de-coupled
Authors: Seth Gottlieb

Daniel Jacobson, [NPR's](http://www.npr.org) Director of Application Development, has an excellent article on the philosophy of [de-coupling the content management tier from the delivery tier](http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere/). He calls this strategy COPE: Create Once Publish Everywhere. In particular, the diagram is particularly useful in showing how all the pieces fit together.

  

If you are in the content publishing business (like NPR is), this is absolutely how you need to think about your content technology stack. Your content repository, editorial systems, and distribution channels can get sophisticated and highly specialized so compromise and lock-in can be costly. The delivery tier that came with your content management system may not scale or may not allow you to push the cutting edge if an opportunity to innovate should arise. All of my big name publishing clients have adopted this strategy for their core publishing platform.

  

However, as I have warned in earlier posts, [the flexibility may not be worth the cost for all publishers](http://www.contenthere.net/2006/12/area-architect-dreams-of-model-architecture.html). Unless your business model depends on aggressively leveraging your content and you can afford to play on the cutting edge, a lighter weight "website in a box" style architecture may give you the flexibility you need without the additional complexity and cost of building and integrating these de-coupled systems. As an example, [Drupal](http://drupal.org) is rapidly becoming a popular platform for small to medium publishers and also for smaller initiatives in larger publishers. And you cannot get a tighter coupling of management and delivery tier than Drupal. One strategy that has been used by early Drupal adopters (that have grown out of their forked versions of the platforms) is to use Drupal to publish into a custom delivery tier. 

  

As an architect, I love the COPE model and I think that most successful, large scale content businesses will eventually converge on that strategy. However, as a pragmatist who also serves publishers in the lower and middle tiers of the industry, I know that the resources and expertise may not be available to go straight to that architecture. Still, at the very least, every publisher needs to start thinking on this level: creating and storing content in presentation neutral way to keep options open. 
