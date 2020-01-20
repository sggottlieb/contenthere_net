Title: Another use for RSS
Date: 2005-12-05T21:25:00.002Z
Modified: 2015-01-06T11:32:15.520Z
Category: misc
Tags: 
Slug: 2005/12/another-use-for-rss_99
Authors: Seth Gottlieb

A little while back, [Charlie Wood](http://www.globelogger.com/moonwatcher/) [wrote](http://www.globelogger.com/item.php?id=521) about using RSS as a mechanism for Lightweight Enterprise Application Integration (EAI). The general idea is that if you need to synchronize data between two applications, you might be able to do it by having each application listen to the other's RSS feed. I like the simplicity of this idea and the fact that it is able to leverage something that many systems are already building in. However, since this is using a "pull" technology it will not support real-time synchronization unless there is some way for the source system to notify the target system to re-check the RSS feed. Otherwise the target system would have to check the source system at fairly frequent intervals. Still, for occasionally updated data (such content in a CMS), it seems very workable.  

Something to think about before investing in a heavy messaging architecture.
