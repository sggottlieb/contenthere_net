Title: Z3ECM
Date: 2005-11-01T08:58:00.002Z
Modified: 2015-01-06T11:32:15.368Z
Category: misc
Tags: 
Slug: 2005/11/z3ecm_35
Authors: Seth Gottlieb

I recently [wrote](http://contenthere.blogspot.com/2005/10/goldegg.html) about the [Goldegg](http://www.goldeggstack.org/) project and was interested to learn about another project related to arrival of [Zope 3 ](http://www.zope.org/DevHome/Wikis/DevSite/Projects/ComponentArchitecture/FrontPage): [Z3ECM](http://www.z3ecm.org/). Z3ECM is a project to build an Enterprise Content Management System (ECM) on Zope 3 and is being supported by France-based [Nuxeo software](http://www.nuxeo.com/en) which also manages [Collaborative Portal Server (CPS)](http://www.cps-project.org/) - an ECM framework built on Zope 2. Some Z3ECM components will be incorporated in CPS in release 3.6 (3.4 is due out next month) and CPS v 4.0 will be built entirely on Z3ECM.   

Projects like [Five](http://codespeak.net/z3/five/), Goldegg, and Z3ECM are critical to Zope 3's success because they will help products (like Plone and CMF), which made Zope 2 so successful, move forward in a Zope 3 world. Of course, even though Zope 3 is out and seems to be gaining momentum, there is nothing forcing Zope 2 users to upgrade. One of the great things about open source software is that users of open source are free to make decisions of if/when to upgrade. With the large install base of Zope 2, there is likely to be a Zope 2 community for quite some time.  

Zope 3 is nearly a total rewrite of the Zope platform. The overall goal is to make Zope easier to develop on by making the code more modular and incorporating some critical features into the core. The use of "interfaces" which are often used in Java applications to make software more object oriented ("polymorphism" is the OO term) Most notably, some aspects of Content Management Framework (CMF), a Zope "Product" (application that runs on Zope) which is used by most Zope based CMS applications, are being folded into the core. One of Goldegg's goals is to develop a new CMF, composed of the features that are not implemented in Zope 3 core, on top of Five (Zope 3 functionality running on Zope 2) and eventually Zope 3. If you want to learn more about Zope 3, there are two professionally published books available: [Web Component Development with Zope 3](http://www.amazon.com/exec/obidos/redirect?link_code=ur2&amp;camp=1789&amp;tag=contenthere-20&amp;creative=9325&amp;path=http://www.amazon.com/gp/product/3540223592?v=glance%26n=283155%26n=507846%26s=books%26v=glance)

<img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=ur2&amp;o=1" style="border:none !important; margin:0px !important;" width="1"/>

 and [Zope 3 Developer's Handbook, First Edition (Paperback)](http://www.amazon.com/exec/obidos/redirect?link_code=ur2&amp;camp=1789&amp;tag=contenthere-20&amp;creative=9325&amp;path=http://www.amazon.com/gp/product/0672326175?v=glance%26n=283155%26n=507846%26s=books%26v=glance)

<img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=ur2&amp;o=1" style="border:none !important; margin:0px !important;" width="1"/>

  
