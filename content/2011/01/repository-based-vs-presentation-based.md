Title: Repository-Based vs. Presentation-Based Search
Date: 2011-01-10T08:24:00Z
Modified: 2015-01-06T12:16:17.708Z
Category: misc
Tags: search, architecture
Slug: 2011/01/repository-based-vs-presentation-based
Authors: Seth Gottlieb

Search is probably the most common visitor-facing requirement in web content management system implementations. Usually the requirement is written in terse form such as "basic search" or "advanced search." But there are many nuances that need to be accounted for. There are essentially two approaches to implementing search requirements: repository-based search and page-based search.  

A repository-based search indexes content items in the content repository. A page-based search indexes the pages of the site. This distinction is more important than you might think — especially if the site design heavily re-uses content. Here is an example. Let's say your site has pictures that are presented in slideshows. The picture content type has a caption that is searchable. A page-based search for a word in the caption of a picture will return the slideshow(s) where the picture is used. A repository-based search will return the picture item itself — but what if there is no detail page for the picture content type? You might have to do something like create a fake detail page that redirects the user to a slideshow page. Another difference is that a page-based search will index text that is hard coded into the presentation templates. For example, you might have your hours of operation in the footer of every page of the site and a "Visit" page that contains the hours plus directions. If a visitor types "hours" into a page-based search engine, he will get every page on the site in the results. A repository-based search engine will return the "Visit" page.  

  
Generally speaking, the search functionality that comes out of the box in a CMS is repository-based. This is necessary because content contributors need a repository-based search to navigate the repository and find content to work on. Some of this content has not yet even been published on the site. Whether you need a page-based search engine for your visitors to use will depend on the nature of your site. Most types of websites do better with a page-based visitor search because a page is a good enough proxy for a piece of content and page-based search engines are generally easier to set up (look how easy it is to set up Google Custom Search). However, page-based search doesn't work well for all sites. In an eCommerce site that has a product catalog, you want to index the products themselves, not all the pages where the products are promoted. If you have requirements for a fielded search, like finding calendar events that occur within a date range, you will also need a repository-based search that indexes individual fields.  

So, next time you are thinking about search, think about whether you want the search engine to index the pages on your site or the content that is being presented in those pages. As with all requirements, the best way to capture search requirements is through scenarios that present real-world examples.
