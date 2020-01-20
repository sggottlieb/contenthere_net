Title: Monitoring your hot standby
Date: 2013-01-11T16:17:00Z
Modified: 2015-01-06T12:30:24.876Z
Category: misc
Tags: wordpress, Web Operations
Slug: 2013/01/monitoring-your-hot-standby
Authors: Seth Gottlieb

As I mentioned in "[Marketing I.T. in the Cloud](http://www.contenthere.net/2012/12/marketing-i-t-in-the-cloud.html)," we maintain a hot-standby infrastructure on another hosting service. We automatically refresh this standby setup at a regular interval so that, if something really bad happened to our primary infrastructure, we could just re-point our domains and relatively recent versions of our sites would be back up.  
  
Because this backup infrastructure is so critical, we monitor it just like our production infrastructure. One thing we have not been able to automate, however, is the check to make sure the front page is loading properly. The problem is that Wordpress forces a redirect to a primary host name. That is, if you try to hit the IP address of the backup server, it will redirect to the primary domain of the site (like <http://www.globalmarketingops.com>) which is still running on the primary servers. The fact that the redirect even happened told you Apache is running and Wordpress is able to read from the database. But you wouldn't know if the pages were broken. This is a little like driving around with a flat spare tire. You know you have it but you don't know it is useless until you try to use it.  
  
Our work-around has been to manually edit our hosts file (which overrides the DNS) and browse the site on a regular basis. But that is a drag. I couldn't find a ping service that allowed me to override the public DNS with temporary mappings. So I came up with something much simpler.  
  
I edited the /etc/hosts file of the backup server to map the supported domains to itself (localhost). With that setting in place, we can run a script on the backup server that loads the home page of each of the sites and verifies that each homepage contains certain text. The script sends out a pass or fail notification. If the server was too broken to run the script we would not get the pass notifications and other alerts would sound. If we get a fail notification, we know that we need to fix the backup site.  
  
This is a pretty common challenge so I hope others can benefit from this simple solution.
