Title: Time Machine Restore
Date: 2008-06-23T06:20:00.001Z
Modified: 2015-01-06T12:15:38.781Z
Category: misc
Tags: 
Slug: 2008/06/time-machine-restore_22
Authors: Seth Gottlieb

Although few people do it, restoring from backup is the only way to ensure that your backup and recovery system works.  Since upgrading to Leopard, I have been using Time Machine to back up my laptop over the network (onto a and external hard drive connected via USB to my [Airport Extreme](http://store.apple.com/us/product/MB053LL/A?fnode=home/shop_mac/mac_accessories/airport_wireless&amp;mco=MTA4NDM2)).  What better way to test a restore from Time Machine than to put in a bigger hard drive and restore?  I figured if it didn't work, I would still have my old hard drive (still working but too small).  
  
I am happy to report that the restore went perfectly.  The general instructions are to be found [here](http://duncandavidson.com/2008/01/restoring-from-time-machine.html).  The only difference is that I restored from the network rather than directly through the USB port.  The one little hitch I ran into was that it took a couple of times for the utility to see my new local hard drive.    
  
I am the kind of person who is frequently shocked when things work as advertised so I was in awe that, after I swapped out the hard drive and ran through the process, it was like nothing happened but the free space of my hard drive grew.  All the software was as I left it.  Even my BASH history was intact.  The only thing missing was my "Downloads" - I had to recreate it.  I guess this is because Mac regards this as a temporary space and not worth recovering.    
  
So, don't hesitate to set up Time Machine.  It could help you recover from a massive hard drive failure, a stolen laptop, or any other disaster - as if it never happened.
