Title: Snow Leopard Issues
Date: 2009-09-10T08:13:00Z
Modified: 2015-01-06T12:16:00.528Z
Category: misc
Tags: python
Slug: 2009/09/snow-leopard-issues
Authors: Seth Gottlieb

For some reason, I upgraded to Snow Leopard at my first opportunity. To tell the truth, the end-user improvements are pretty modest and it is difficult to perceive Snow Leopard's slight speed improvements. That is not to say that the upgrade did not have impact. Some software that I regularly use stopped working. I am all up and working now and here is now.  

<style type="text/css">table.padded-table td { padding:10px; text-align:left } table.padded-table th { padding:10px; text-align:left; font-weight:bold }</style>

  
  

<table class="padded-table"><br/><tr><br/> <th width="50%">Problem</th><br/> <th width="50%">Solution</th><br/></tr><br/><tr><br/> <td><strong>Oxygen 9.3 stopped working<strong></strong></strong></td><br/> <td>I upgraded to Oxygen 10.3 for $147</td><br/></tr><br/><tr><br/> <td><strong>My macport MySQL, Apache, PHP setup broke<strong></strong></strong></td><br/> <td>I tried to do port upgrade of MySQL and PHP and it failed.  Compiling my own PHP didn't work either.  I wound up installing the MySQL package from the MySQL site and using the Apache and PHP (5.3) that comes with Snow Leopard.</td><br/></tr><br/><tr><br/> <td><strong>My <a href="http://ez.no">eZ Publish</a> development environment broke<strong></strong></strong></td><br/> <td>This was because I upgraded to PHP 5.3.  This was easily fixed by re-installing eZ Publish because eZ Publish is compatible with PHP 5.3</td><br/></tr><br/><tr><br/> <td><strong>My <a href="http://ez.no">Drupal</a> development environment broke<strong></strong></strong></td><br/> <td>Drupal is not compatible with PHP 5.3.  Until it is, I am running it on <a href="http://www.mamp.info/en/index.html">MAMP</a>.  </td><br/></tr><br/><tr><br/> <td><strong>Python MySQL did not easy_install for Python 2.6<strong></strong></strong></td><br/> <td>This is the problem that I struggled most with.  I followed the instructions <a href="http://cd34.com/blog/programming/python/mysql-python-and-snow-leopard/">here</a>.  The compile and build worked but I could not import the library.  I finally solved the problem by re-installing the 32 bit version of MySQL, setting Python to run in 32 bit, and following <a href="http://www.zen-hacking.com/2009/09/01/python-mysql-under-snow-leopard/">these simple instructions</a>.  </td><br/></tr><br/><tr><br/> <td><strong><a href="http://agilewebsolutions.com/products/1Password">1Password</a> 2.x is incompatible with Snow Leopard<strong></strong></strong></td><br/> <td>I pre-purchased version 3 and enrolled in the 3.0 beta program.  The UI looks really slick and I am happy that I upgraded.</td><br/></tr><br/><tr><br/> <td><strong><a href="http://www.zennaware.com/">Cornerstone</a> is incompatible with Snow Leopard<strong></strong></strong></td><br/> <td>I am waiting for the next release of Cornerstone (due this month) that will be Snow Leopard compatible and also support Subversion 1.6.  </td><br/></tr><br/></table>

  

Looking back, it would have made more sense to wait on the upgrade and see what other people on the mailing lists said about their experiences. But, since I figure I would share what I learned. 
