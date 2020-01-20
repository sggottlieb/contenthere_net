Title: Deployment Timing for a Global Business
Date: 2013-07-23T10:00:00Z
Modified: 2015-01-06T12:30:25.324Z
Category: misc
Tags: DevOps
Slug: 2013/07/deployment-timing-for-global-business
Authors: Seth Gottlieb

Global businesses operate on a 24 hour workday. No matter what time it is, somebody is trying to get something done - whether it be a customer trying to interact with you or it could be an employee trying to do her job. This can make system maintenance (such as deploying new website functionality or upgrading some business application) a challenge. Of course, we do our best to minimize or eliminate the amount of downtime a deployment causes. In fact, my team regularly deploys new code across our applications several times day (yay, automation!). However, there are also deployments that you try to schedule outside of peak load. Perhaps, there will be brief periods when the system is unavailable or in an awkward transitional state. So the question is, when do you do these deployments? We look at three factors:  

  
 *   The first thing we look at is the business calendar to make sure we are aware of any events that might drive traffic. For us, this could be a marketing campaign or, for our business applications, it could a peak in workload (like a deadline). It's a good idea to have a mailing list of primary users and announce upgrade plans to them. They will tell you if there is an issue with your schedule.
  
 *   The second thing we look at is daily load patterns. All of the systems that I manage are running on Amazon Web Services using Elastic Load Balancers so my favorite tool for this is a CloudWatch ELB Request Count report. That shows nice regular daily spikes of traffic to your sites.
  
 *   The third, and possibly most important, thing we look at is our own work patterns. While the load patterns may tell you to do your deployments at 3AM, __don't do it__. You could be tired and careless at that time of night. Plus, you will probably want to go to bed right after and that would be the worst time to be sleeping. Configuration errors usually take a little while to surface. &nbsp;You don't want to wake up the next morning to find an inbox full of frustrated users who lost large chunks of productivity.
  

  
Using this logic, we typically find our best upgrade windows to be at unexpected times like 2PM Eastern on a Wednesday. During this time: most of Asia is sleeping; Europe is enjoying dinner; and most of the Americas is having lunch or in a post-meal coma. At this time, we have our full team on hand for testing and remediation if anything goes wrong. And we get to sleep well that night knowing if anything were to go wrong, it would have done so hours ago.  
  
One caveat: this strategy probably won't work for you if you are delivering a high traffic service with a ridiculously stringent SLA. But if that is your business, you should probably have an around-the-clock, 3-shift dev-ops staff and lots of people planning and managing deployments.
