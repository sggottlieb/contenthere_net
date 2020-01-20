Title: Complex Systems
Date: 2013-02-28T16:20:00Z
Modified: 2015-01-06T12:30:24.956Z
Category: misc
Tags: simplicity, Web Operations
Slug: 2013/02/complex-systems
Authors: Seth Gottlieb

I have been loving the book [Web Operations: Keeping the Data On Time](http://www.amazon.com/gp/product/1449377440/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=1449377440&amp;linkCode=as2&amp;tag=contenthere-20)

<img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=1449377440" style="border:none !important; margin:0px !important;" width="1"/>

. It is indispensable reading for anyone responsible for hosting a web application or any important website. As the editors say, web operations is an emerging field with little in the way of training programs or officially sanctioned best practices. Nobody is classically trained. The best web ops people grew up in the field and learned from other greats and being faced with tough challenges.

  

One of the book's chapters is a reprint of an academic article called [How Complex Systems Fail](http://www.ctlab.org/documents/How%20Complex%20Systems%20Fail.pdf) by Richard I. Cook. Interestingly, this article wasn't written about Web Ops at all. Richard Cook is an MD and he was writing about hospitals and healthcare. But the similarities with web ops are striking. It's a quick read and it's free. The points that were especially salient to me were:

  

*   
    
    ### "Complex systems contain changing mixtures of failures latent within them."
    
      
     
    
    The more fault tolerance you add, the more unnoticeable little failures become. And even when you notice them, issues can be fleeting and too difficult and/or not important enough to fix. You just live with them. Even if you have a very simple set up, the cloud hosting service that you are running it on is incredibly complex — so complex that it can suffer from living organism diseases like [auto-immune vulnerabilities](http://blogs.gartner.com/lydia_leong/2011/04/21/amazon-outage-and-the-auto-immune-vulnerabilities-of-resiliency/). When adding yet another layer of complexity to make your system more resilient, sometimes you introduce more potential for failure that may reduce the health of the overall system. Our hosting infrastructure has lots of redundancy built into it. But sometimes I yearn for simpler times when I had one physical server that I just rebooted when things got ugly.
    
      
     
*   
    
    ### "All practitioner actions are gambles."
    
      
     
    
    There are a few points in the article that deal with post accident analysis. As frantic as it feels to have a site outage, the author is talking about much higher stake failures (he's a doctor, remember). But his analysis is right on. Whenever we do anything, we are making a gamble — no matter how much we test. Sometimes the risk of the gamble is much less than the risk or opportunity cost of doing nothing. But you can't always tell. It is easy to get down on yourself or your team when a mistake is made or a failure occurs. But as the article says: "That practitioner actions are gambles appears clear after accidents; in general, post hoc analysis regards these gambles as poor ones. But the converse: that successful outcomes are also the result of gambles; is not widely appreciated." In other words, system improvement depends on gambles.
    
      
     
*   
    
    ### "People continuously create safety."
    
      
     
    
    The point here is that you can't make anything totally idiot-proof. In the world of web ops, you can script things but you always need experienced people thinking about what they are doing and keeping an eye on things.   
     
    
    
*   
    
    ### "Failure free operations require experience with failure."
    
      
     
    
    This point really extends the previous point. The only way people get experience is by facing failure. In the early days of my career (amazingly, nearly 20 years ago), I worked in a tiny I.T. department serving a large and rapidly growing company. Our team was brilliant but inexperienced and we were constantly faced with new problems that we had to solve under pressure (my favorite was our "total network crash" that was actually the folding card table that held all of our servers collapsing). We all learned so much and everyone on the team went on to a successful career. But we wouldn't have learned anything if everything went smoothly. As a side note, I experienced more appreciation from the user community during those years than since. People saw that we were creative, dedicated, humble, and fearless. We didn't have that dysfunctional I.T. v.s. business dynamic. We were all in it together. 
    
      
    

  

I know that the message I have been sending is that marketing I.T. is complex and messy and you just need to deal with it. To an extent, this is true. But it also means that whenever there is an opportunity to simplify something, you need to take it. I see every piece of unjustified complexity as a risk with unknown cost. It is easy to relate to the added up-front cost of adding a little flourish that makes an application more interesting. It takes experience to understand the long term cost of maintaining something that is more complicated than it needs to be. Even if that clever code is lucky enough not to break when something else changes, it will perpetually need to be circumnavigated by others who barely understand how it works. Before long, [you have a culture of people who are afraid to touch things and cruft is inevitable](http://www.tvagile.com/2013/01/29/cruft-and-technical-debt-a-long-view/).

  

If there is a way to do something in a more direct way, take that approach. When thinking of development costs, budget for the cost of maintaining that code. Prioritize refactoring and refinement over adding new features. [Make is suck less](http://www.codesimplicity.com/post/suck-less/). Most of all, don't let your complexity outgrow your capacity to manage. it.
