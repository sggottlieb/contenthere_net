Title: OpenCms Eclipse Plugin
Date: 2007-06-19T10:39:00.002Z
Modified: 2015-01-06T11:32:50.560Z
Category: misc
Tags: 
Slug: 2007/06/opencms-eclipse-plugin_88
Authors: Seth Gottlieb

[Dave Schoorl](http://www.redstardevelopment.nl/opencms/opencms/en) just announced on the [OpenCms](http://www.opencms.org) mailing list his new [Eclipse plugin for OpenCms module development](http://www.redstardevelopment.nl/opencms/opencms/en/opencms/plugin/).  This plugin provides direct synchronization with OpenCms's virtual file system.  Lack of WebDAV support for the VFS has made developing code for OpenCms a little awkward because you develop locally and then need to figure out some way to push it to the server.  Dave's plugin handles the synchronization behind the scenes so you don't have to worry about it.  OpenCms Version 7 (currently in Beta) includes WebDAV support but there is still great value of having an Eclipse plugin because it sets the foundation for lots of other developer conveniences.  This is the strategy that many commercial CMS products are taking: rather than try to build your own stand alone IDE, sit on top of a solid foundation that is familiar to most developers.
