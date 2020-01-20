Title: The Apogee Project
Date: 2006-02-23T10:18:00.002Z
Modified: 2015-01-06T11:32:17.280Z
Category: misc
Tags: 
Slug: 2006/02/the-apogee-project_76
Authors: Seth Gottlieb

French systems integrator, [Nuxeo](http://www.nuxeo.com), makers of [CPS](http://www.cps-project.org), just announced a new project called [Apogee](http://apogee.nuxeo.org/). Apogee is an [Eclipse RCP](http://wiki.eclipse.org/index.php/Rich_Client_Platform) based thick client for ECM systems such as [CPS](http://www.cps-project.org), [Documentum](http://www.documentum.com/) and [Interwoven](http://www.interwoven.com). I think this project has a lot of potential.   

First of all, although everyone loves a web based client, there are some structural limitations of using a browser to manage files. For security reasons, browsers are designed to have very limited interaction with the underlying file system. Signed applets and ActiveX controls can circumvent this security system but users need to know what to trust and what not to trust. An installed thick client avoids this issue.  

Training is a key issue in rolling out any content management system. If you can standardize on a UI, you may be able to lower your switching costs from one ECM product to another. Most ECM products have standardized on Windows Explorer as the interface by exposing the repository as a file share. However, this model has its limitations because Windows Explorer does not expose metadata and other functionality that makes an ECM system more than just a file system. There are work arounds. For example, [Tortoise SVN](http://tortoisesvn.tigris.org/) and [Tortoise CVS](http://www.tortoisecvs.org/) both give right click menu options for source control functions such as dif, check out, commit, and history.  

For those who are not familar with Eclipse or Eclipse RCP, Eclipse is mostly used as an Integrated Development Environment (IDE) for building Java applications. However, it is designed as a framework for building many different other kinds of applications. Many big companies (such as [IBM](http://www.ibm.com), [BEA](http://www.bea.com), [Borland](http://www.borland.com)) that have their own IDE's contribute heavily to Eclipse. The idea is that there is core functionality that is common to many different kinds of business applications (navigation, editing interfaces, different views). Eclipse supports these basic services and the actual business applications are implemented as plugins. [RCP](http://wiki.eclipse.org/index.php/Rich_Client_Platform) is the core for building these plugins. For example, the open source reporting tool [BIRT](http://www.eclipse.org/birt/phoenix/) is implemented on Eclipse RCP. If you can get Eclipse installed on your users machines, rolling out Apogee and BIRT is very simple thanks to the Eclipse plugin manager.   

It will be interesting to see if the major proprietary ECM vendors get behind this initiative. They could take the view that Eclipse contributing companies do: cooperate to reduce the cost of the delivering the basic core functionality and compete on the value-add differentiators. Somehow, I don't think that the big ECM vendors will have this perspective. One can always hope though.
