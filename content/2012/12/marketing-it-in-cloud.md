Title: Marketing I.T. in the Cloud
Date: 2012-12-20T09:16:00Z
Modified: 2015-01-06T12:30:24.854Z
Category: misc
Tags: Global Marketing Operations, Web Operations
Slug: 2012/12/marketing-it-in-cloud
Authors: Seth Gottlieb

For a long time, I have been advocating that marketing organizations build technology capabilities. [Marketing I.T. and Enterprise I.T. have totally different mindsets](http://www.contenthere.net/2008/07/product-it-vs-enterprise-it.html). Marketing I.T. is more like product development with an emphasis on opportunity and innovation. Traditional I.T. prioritizes stability and cost control. Increasingly I have seen ownership of digital marketing technology moving from I.T. to marketing. Now I have a front row seat.

  

One of the unexpected aspects of my job here at [Lionbridge](http://www.lionbridge.com) is that I run Marketing I.T. In particular, I manage our hosting infrastructure and work with teams developing new sites and applications on it. Given that many marketing organizations are inheriting this responsibility, I figured I would share some of the tools/services that I have found useful. I am going to talk about a lot of different products here. I am not endorsed by any of these companies and I am only mentioning products that I like.  

  

*     
     
    
    ## Hosting: Amazon Web Services (AWS) and Rackspace Cloud
    
      
     
    
    We do everything in the cloud. We set up a multi-server infrastructure on AWS using Elastic Compute Cloud (EC2: virtual servers), the Elastic Load Balancing service (ELB), and Relational Database Service (RDS). Both ELB and RDS span multiple physical data centers which is good for availability. We have EC2 instances in multiple data centers too. Our sites are also replicated to infrastructure hosted on Rackspace Cloud so that if AWS has a major problem, we can re-route traffic over to Rackspace. We test our sites on Rackspace weekly. Both AWS and Rackspace are great. AWS has many more features but the tech support is very limited. You need to pay extra for support and it can take a while to get an answer. Rackspace support is amazing. If you don't have a decent sysadmin, I would go with Rackspace.
    
      
    
    
    [Ylastic](http://ylastic.com/) makes administering AWS services much easier. The UI is not pretty but it is much better organized for doing specific tasks like managing backups and migrating and configuring servers. Ylastic also gives some insight into the health of the overall AWS infrastructure. The mobile UI is a big step up over the AWS management console on the little screen. We just use the basic level. At higher levels, you get some functionality to help manage your spend.
    
       
      
    
*     
     
    
    ## Monitoring and Alerting: ServerDensity, CloudWatch, and PagerDuty
    
      
     
    
    AWS comes with its own monitoring service called CloudWatch. We have set up notifications to fire if the load balancer removes one of our servers because it isn't responding. We also wanted to have external monitoring services running so we could look at our RackSpace servers. Plus, it's a good idea to have your monitoring service independent from your hosting infrastructure in case your hosting infrastructure is too compromised to send an alert. We learned this the hard way when an AWS outage took out our monitoring as well. Most of our monitoring is done with a service called [ServerDensity](http://www.serverdensity.com). This keeps track of internal server health metrics and we have it pinging the sites to make sure they are responding. [Pingdom](https://www.pingdom.com/) is also useful for checking if a site is up. We would use that if we didn't have ServerDensity
    
      
     
    
    We do all of our alerting through a service called [PagerDuty](http://www.pagerduty.com/). While all monitoring services can send out pages and emails, the nice thing about PagerDuty is that you can set up on-call schedules and escalation pathways. This is important because I have a really small team and everyone has other jobs (which can require travel). Even a non-techie can be on the "site may be down" alert. Usually this is a false positive because one of the servers in the cluster bounced in and out of the load balancer. Whoever gets the notification checks the site and texts a resolution code back (resolve, acknowledge, or escalate). I have trained non-techies to update the DNS to send traffic to Rackspace in the case of an emergency.  
     
    
      
    
*     
     
    
    ## Code Management: BitBucket
    
      
     
    
    We have lots of different people building sites for us. Some are on staff, others are contractors or external agencies. We use BitBucket (with Git) for source code management. This allows me to easily bring in a contributor but thoroughly review his/her code before merging it into our code base. We follow the classic ["Fork/Pull Request model"](https://confluence.atlassian.com/display/BITBUCKET/Fork+a+Repo%2C+Compare+Code%2C+and+Create+a+Pull+Request). Some developers/agencies get it better than others. I am weeding out the folks who don't get it because it makes my life harder. I don't want to deal with zip files of directories and worry about coordinating the changes from different people. With a pull request, I can see every change and easily merge.  
     
    
      
    
  
*     
     
    
    ## People
    
      
     
    
    While all of this technology is great, it's the people that make it go. As I mentioned earlier, my team is small. We get a lot of design and development help from outside contractors and agencies. I share sysadmin work with a really good contractor that knows much more than I do about managing servers. Having a "virtual team" is nice for scalability but it sometimes presents challenges for scheduling. I found a web project manager (with the help of my [one field job application](http://www.contenthere.net/2012/08/an-unconventional-approach-to-recruiting.html)) who can handle a lot of basic tech tasks like running deployments and migrating sites. She has SSH access to all of our servers and can do things like restart Apache. She only started a couple of weeks ago and she is already making a huge contribution.
    
      
    
  
*   
    
    ## Process
    
      
     
    
    We track all of our work in a ticket tracking tool called DOT (which we also use for our [GMO](http://www.globalmarketingops.com/) clients). We also use DOT for tracking time so we can see how much effort we spend on various development projects. We group infrastructure projects into milestones that represent maintenance windows. Leading up to a maintenance window, we prepare the fixes and test them on a QA environment. We defer tickets that we are not confident that we can complete. Once the milestone is locked down, we send out an email to stakeholders explaining what we are doing, when we are doing it, and how it could possibly affect them. Then, after we complete the maintenance window, we send out a completed email, reminding of any relevant changes.
    
      
    
  

  

Overall, I am impressed with what a small team can do on a limited budget. By using cloud-based technologies, we can afford levels of redundancy and sophistication that would be prohibitively expensive to buy up-front: multiple data centers, generators, alerting systems, source code management… People-wise, we probably have around .5 FTE spread across several people (internal and external) managing and extending this infrastructure. These people have other responsibilities such as building and managing our services and products.   

The best part of this whole arrangement is that we can be ultra-responsive. If something is important to a marketing initiative, we can act on it immediately. Our work does not go into a larger queue, where it may be misassigned or assigned to someone who doesn't have the complete context to do the work properly. The social dynamic is different as well. We are part of the team. Our motivations are aligned and we don't have those defensive postures that I.T. needs to fend off the entire organization. When we push back, we do so as peers and can explain why in terms that our peers can relate to. I think all mid to large sized organizations need a marketing I.T. team and this seems like a good way to structure it.
