Title: Evolutionary Software Development: A Model for Maintaining Web Sites and Applications
Date: 2013-12-17T12:35:00Z
Modified: 2015-01-06T12:30:25.430Z
Category: misc
Tags: DevOps, agile
Slug: 2013/12/evolutionary-software-development-model
Authors: Seth Gottlieb

Since I got into software development back in 1995, I have been exposed to many different software development methodologies. I started out with a highly structured waterfall model (which is hard to avoid with fixed bid projects). Whenever possible, I have advocated agile approaches and I have been on teams that have practiced agile methods like Scrum with varying degrees of fidelity. Overall, I love [the values of agile](http://agilemanifesto.org/) but the agile methodologies that I know of don't quite feel right for the kind of work I do now.  
  
These days my job focuses on managing several different web sites and applications. Officially, you could say that these applications are in "maintenance mode" but the truth is that they were always in maintenance mode. All of these applications have been built on the philosophy of a [minimum viable product](http://en.wikipedia.org/wiki/Minimum_viable_product). That is, we developed a minimal solution to test a) that the problem actually exists and b) that our idea is an effective way of solving it. The initial solutions were just complete enough to answer these questions and create a foundation for an evolutionary process towards continuous improvement. Everything since has been "maintenance."  
  
The agile development methodologies that I know of don't quite fit because they all seem to focus on a notion of defining a 2-3 week "release" or "sprint" and putting the entire team onto cadence that begins with planning and ends with some kind of review. But my teams do not work that way. We release one feature at a time. We don't wait for some large milestone to push new code into production. In fact, we push a new feature as soon as it is ready. We see an un-published feature as a huge liability. Worse than simply not being able to get the benefit of the feature or see how the audience responds to it, unpublished code is a risk. When code sits in an unpublished state it needs to be maintained like working code. Otherwise, when you deploy it, you are likely to break other things. Also, large deployments are riskier than small deployments and make problems harder to diagnose.  
  
We try to define features to be small as possible. Some features are "below the waterline." That is, they are not visible to the end user and are only deployed to support another feature in the future. A very common example of this pattern is that we usually do our database work up front. For example, if we need to build a new page design, we will start by deploying the new fields that the design requires. Then our content team can add the data. Later, once the data is in place, we can deploy our page templates and other application logic that relies on the new data. We also commonly deploy infrastructure upgrades ahead of the features that they support. We also try phasing in features with an initial simplistic implementation to test out the concept and then a series of enhancements to reach the full potential.  
  
When you are maintaining a live application, the line between a bug and enhancement is blurred and the same team should responsible for both. Anyone on the team needs to be able to pull herself away from the feature she is working on to fix an urgent issue. This is another reason why keeping things small is very important. It is also why it is so important to have a very clearly defined prioritization protocol. Ours is:  

  
 2.   Site down
  
 4.   Feature broken with no work around
  
 6.   Feature broken with work around
  
 8.   Revenue opportunity
  
 10.   Customer Usability
  
 12.   Operations Usability
  
 14.   Brand consistency
  

  
The product manager is in charge of setting the priorities and assigning high priority issues that need to get taken care of ASAP.  
  
The lines between coding, content, infrastructure, and support are also blurred. Sometimes an issue is noticed and the cause is not immediately apparent. For example, let's say a customer cannot download a file. It could be that the file was not added in the first place. The code to retrieve the file could be broken. The server could be out of space and the file could not be saved. It could be a usability issue and the customer was clicking on the wrong link. Triaging and coordinating this work is critical needs to be core to the methodology.  
  
Refactoring is another big part of the methodology. You often run into situations where a feature gets a lot of traction but not in the way that you expected. You might need to change how it was built to allow it to evolve in the right direction. You will also need to refactor your successful experiments to support active use. The concept of a "user story" (common in agile methodologies) does not lend itself well to code refactoring.  
  
As you can see, traditional agile methodologies do not accommodate the day to day activities required to maintain and extend an actively used web application. This is because they are designed at their core to support software development _projects_ where the team has the luxury of ignoring the operational aspects of running the application as a service. But that luxury comes at a price: alienation from critical feedback by actual consumers of the application. In agile, a "customer" role filters and simplifies end user needs and tastes. This customer makes a lot of guesses about what the end customers want. The guesses tend to be big and there is no process for correcting the wrong ones. The agile approaches that I know of seem better for building packaged software or for integration companies that are brought in to build something and leave. These are cases where you cannot or don't want to be told that you need improve something right after you thought you built it to specification.  
  
Here is a very real world example to illustrate that point. We use LivePerson to chat with customers who are on our sites. Sometimes there are cases when a customer gets stuck because he does not notice or cannot understand an error message — such as one telling him that he needs to enter something into a certain field. If it is common enough, we will use that feedback to design, implement, and deploy a fix that makes the validation message more visible and understandable. Fixing this issue could be hugely important to conversions. But think about how this problem might be solved in Scrum. A "user story" would be added to the backlog. At some point, this story makes it into the next sprint. It needs to wait for the rest of the sprint to finish before it is deployed. If you do two-week sprints, that could be up to a four-week turn around. You might say that you would handle this in a maintenance track that runs in parallel to your _real_ development. But I would counter that tweaks like this are where applications succeed and fail and should be the focus of (not the exception to) your process. In fact, I think you should think of everything as a tweak.  
  
Despite the fact that lots of organizations are maintaining sophisticated web applications and want to experiment with new features as fast as possible, I have found little writing on formal methodologies to support this. The best writing comes from the DevOps community but they don't directly often address the actual software development as much as I would hope. I like Eric Ries's chapter on continuous deployment in [Web Operations: Keeping the Data On Time](http://www.amazon.com/gp/product/B0043M4Z34/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B0043M4Z34&amp;linkCode=as2&amp;tag=contenthere-20)

<img alt="" border="0" height="1" src="http://ir-na.amazon-adsystem.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=B0043M4Z34" style="border: none !important; margin: 0px !important;" width="1"/>

. Speaking of Eric Ries, lean startup literature is also a very good resource. But this community emphasizes customer development and doesn't explore the architecture/implementation side as much as I would like.  
  
What really inspired me to write this post was this relatively obscure research paper called "[An Online Evolutionary Approach to Developing Internet Services](http://www.cs.berkeley.edu/~brewer/papers/online-evolution-draft.pdf)." This fit the bill when I was looking for a term to describe how we work. The word "evolution" is perfect. It captures the idea that development is a series of small modifications that respond to stresses and opportunities. Each modification is tested in the real world. The ineffective ones die off. The good ones are the foundation for future progress. It is true natural selection. We just try to be a little less random than biological evolution.  
  
I would love to hear your feedback on this. I go back and forth between thinking that we are outliers for working in this way to thinking that this process is so universal that nobody thinks about it. I also think there is a lot to discuss with regards to testing, communicating changes to users, and localizing the solution.
