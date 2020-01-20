Title: WCM needs a new name. Or, perhaps, an old one.
Date: 2009-12-18T11:36:00Z
Modified: 2015-01-06T12:16:16.002Z
Category: misc
Tags: commentary
Slug: 2009/12/wcm-needs-new-name-or-perhaps-old-one
Authors: Seth Gottlieb

This post was originally written as a comment on Jon Mark's excellent post [Visions of Jon: WCM is for Losers](http://jonontech.com/2009/12/16/visions-of-jon-wcm-is-for-losers/) but it got out of hand and I suspect that it is too long for a comment so I am re publishing it here. 

  

Thanks for the great post Jon! I have to agree with you that the term Web Content Management System is misleading because of its diverse focus on multiple publishing channels. You probably remember that in the old days (~1996), the term "CMS" was first used to describe products like Vignette and what are now called ECM systems were just called Document Management Systems, Records Management Systems, etc. When the big DMS vendors started to covet the term "content," the (then) smaller WCM vendors had to slide over a bit and qualify their category with a "W." Then some of them started to ruin themselves by trying to expand into document, management, records management, etc. - but that's another story.

  

But enough about the Ghosts of Christmas Past... I agree with the point that a WCMS has multiple aspects. I would name three: a management tier to edit semi-structured content, a repository to store the semi-structured content, and a rendering tier to render the content. Usually the repository is more tightly coupled to the management tier so it is often tucked into the management application. In fact, [the three components are often bundled for convenience.](http://www.contenthere.net/2006/12/area-architect-dreams-of-model-architecture.html "coupled architectures")

  

In my mind, what sets WCM apart from the other forms of CMS is the C. I still think of Content as having more structure (and less embedded formatting) than what you typically find in an ECM repository. In the ECM world, the structured information is called metadata and is not considered part of the asset (a MS Office file that jumbles together information and presentation). A WCM asset needs to be rendered (given a format) to be useful to a consumer. This is why a WCMS needs a good rendering system. 

  

Most ECM assets can just be downloaded but the range of formats they can take is limited. You can get a different file format (like a PDF) or a different scaling or cropping of an image but the output looks essentially the same. ECM has tricks to add structured information like metadata and embedded tags but that is going against the grain. WCM, which is inherently structured, knows what each of the different elements of an asset mean. I like to say that _ECM is documents pretending to be content and WCM is content pretending to be documents_. That is, ECM starts with a document and tries to pull information out of it while a WCM starts with structured information and renders it into a .html, .pdf, .xml, or any other kind of document. 

  

So, at the end of it all, I would say that WCM should be renamed back to CM and ECM should be renamed to EDM: Enterprise Document Management. 
