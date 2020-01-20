Title: Can Outages be Good for the Cloud?
Date: 2012-07-05T11:33:00Z
Modified: 2015-01-06T12:30:24.458Z
Category: misc
Tags: cloud
Slug: 2012/07/can-outages-be-good-for-cloud
Authors: Seth Gottlieb

I was just thinking about [the recent AWS outage](http://www.contenthere.net/2012/07/cloud-blues.html) and came to the conclusion that infrequent events like this probably help Amazon. While the first wave of response is usually criticism and doubt, the end result is probably increased adoption. Here is why. I don't think that events like these are chasing anyone away from the cloud. The reality is that technology occasionally breaks — especially under extreme conditions. No matter where you have a data center, bad events are going to happen. I was just talking to a friend who works in the Baltimore area and their self-hosted site has been down for days due to power outages. When people take a close look, they realize that most cannot provide better availability than cloud computing resources.   

Rather than abandon the cloud, I expect that most customers will do what I found myself doing: the opposite — increase their cloud investment. If they were in one availability zone, they will expand their cluster to get into multiple availability zones and even multiple regions (which I am doing). They will create warm standby servers to switch over to in the event of a catastrophic failure. All these changes increases their monthly AWS bill and leads to higher Amazon revenues. It's just like the insurance business. The best time to sell new policies is right after an unlikely disaster, which is also usually the least likely time for the disaster to happen again (especially when new controls are put in place to prevent it).
