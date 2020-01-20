Title: Jeff Potts explains the difference between Alfresco&#39;s DM and AVM Repositories
Date: 2009-09-01T07:02:00Z
Modified: 2015-01-06T12:16:00.505Z
Category: misc
Tags: alfresco
Slug: 2009/09/jeff-potts-explains-difference-between
Authors: Seth Gottlieb

Jeff Potts has written an excellent [article explaining the functional differences between Alfresco's two different repositories](http://ecmarchitect.com/archives/2009/08/31/1038) (the original DM and the WCM). The enclosed chart is a useful cheat sheet that belongs on any Alfresco developers cubicle. Nice work Jeff!

  

For those of you who are new to Alfresco, the WCM repository (or AVM: Advanced Versioning Model) was introduced to the platform when Alfresco added web content management. The AVM is designed for managing structured XML content and does very cool things like snapshots and contributor "sandboxes." But the AVM is slower than the original DM repository and has less powerful metadata capabilities. Typically, web content will be managed as XML in the AVM and then pushed over to a cluster of DM repositories to power a dynamic website.
