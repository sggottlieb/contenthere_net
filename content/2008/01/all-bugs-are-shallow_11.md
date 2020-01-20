Title: All bugs are shallow
Date: 2008-01-14T13:17:00.002Z
Modified: 2015-01-06T11:32:51.398Z
Category: misc
Tags: 
Slug: 2008/01/all-bugs-are-shallow_11
Authors: Seth Gottlieb

[Information Week](http://www.informationweek.com) recently published an [article about an ongoing study of software bugginess](http://www.informationweek.com/news/showArticle.jhtml?articleID=205602186). In 2006, a Homeland Security sponsored [Coverity](http://www.coverity.com/) study of the major open source projects (Linux Kernel, Apache HTTP, etc.) found these projects to have a similar defect rate to analoguous commercial products (although commercial software defect rates are not made public). I am not surprised by this finding since these large institutional projects have professional developers (employed by major software companies like IBM and Oracle) working on them.

  

What is interesting about this article is that a new code analysis tool by Stanford University, called Prevent SQS, runs on a periodic basis and has discovered that bugs are being fixed at an extremely rapid rate. To quote the article:

  
>    
>  
> A total of 7,826 defects have been identified and fixed through the Homeland Security review, or one every two hours since it was launched in 2006. Bugs and vulnerabilities have been found in most open source projects, which isn't surprising. What is surprising is the speed with which some projects resolve the issues as Coverity airs them on its Web site, versus other projects that lag behind.
>   
>   

By putting vulnerabilities out in the open, a project with a large community is able to mobilize and respond to risks that users of the software are not willing to tolerate. However, commercial software products tend to be less open about their bugs and prioritize the addition of new features where they hope to achieve competitive advantage in acquiring new customers. That is not to say that these bugs do not get fixed. Anyone who has run a Microsoft IIS environment knows about all the security updates and packages you need to keep up with. However, the commercial patch probably comes _after_ the bug has been exploited on a customer installation and has become a customer relationship liability.

  
  
