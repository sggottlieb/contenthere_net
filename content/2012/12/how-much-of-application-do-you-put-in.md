Title: How much of an application do you put in source control?
Date: 2012-12-17T16:10:00Z
Modified: 2015-01-06T12:30:24.817Z
Category: misc
Tags: development, Web Operations, wordpress
Slug: 2012/12/how-much-of-application-do-you-put-in
Authors: Seth Gottlieb

Warning: geeky coding post

  

One of my responsibilities at [Lionbridge](http://www.globalmarketingops.com) is running infrastructure for our many marketing sites and applications. Like all good technical organizations, our development and deployment processes revolve around a source code management (SCM) system (in our case Git). Because we are running on a CMS (Wordpress - hold the religious war on whether Wordpress is a CMS), our websites are a combination of platform (Wordpress), customization (plugins and themes), configuration, and content. The question is: how much of this do you put into your SCM? Let's start with the obvious. You don't put content in your SCM. With configuration, it depends. Some frameworks allow you to tier your configuration options between global and environment-specific. For example, [this is how I handle Django settings.](http://www.contenthere.net/2012/04/keeping-django-settings-generic.html) I haven't come up with a clever way to do this in Wordpress so, for now, I am keeping wp-config.php out of the SCM.

  

As for platform and customizations, my tendency has always been to _keep the platform out of the SCM_. In this model, your build process is to install the platform than then deploy the themes and plugins from source control. I have done many projects in this way and it worked quite well. But another developer set up our Wordpress infrastructure for these sites and his preference was to put the whole Wordpress install into SCM and do a "git pull" to update the whole site. I also didn't love the idea of using Git to deploy. I like to pull the code to some alternative machine (my workstation or a server), (compile/)package it, and then _push_ it to the web farm. [Fabric](http://docs.fabfile.org/en/1.5/) is an excellent tool for this. You can still use Fabric in this scenario to execute Git commands on the remote servers but it still doesn't feel right to me. I prefer that runtime servers have as little software running on them as possible.   

At first I hated this set up. I missed a developer being able to install our themes and plugins into any old Wordpress instance. I had doubts about the complexity of administration settings and the potential of editing source-controlled files trough the web. But I kept an open mind and I have come around. Here are the reasons:

  

  
2.   __The upgrade process is a lot tighter__. Now I just upgrade Wordpress on a development instance, test, and then deploy the upgrade through the normal code deployment process. Plugins are handled the same way.  
    
3.   __Customization compatibility issues just go away__. When we have an outside contractor work around the system by working in his/her own Wordpress we run into issues where the new code is incompatible with versions of Wordpress and our installed plugins. This simply doesn't happen when you check out the whole platform.  
    
4.   __Your SCM provides diff'ing functionality.__ Suspect that one of your environments does not conform to the rest? Worried that you have been hacked? Simply do a "git status" and see what files are different from the repository.   
    
  

  

One thing to keep in mind: in this model you don't do any upgrades or plugin installation through the web. You also need to turn off the ability to edit theme and plugin code through the web. We needed to do this anyway because we have a clustered infrastructure and those changes need to be propagated across every web server in the farm.  

It took me a really long time to come around to liking this setup. I think a big part of that is my Java background. Java makes a big deal about packaging and deployment. Pulling directly from Git seems more common in the PHP world, which never had a build process. But now, I am pretty happy with this setup. The best part is ensuring against compatibility issues (\#2 on my list above). I still prefer deploying code _to_ servers rather than pulling code _from_ them but my conviction is steadily eroding. It's kind of nice not needing scripts to move around files and avoid overwriting files that are managed independently on each environment.

  

Just out of curiosity, I would love to know what source code management and deployment processes other PHP developer use. Let me know.
