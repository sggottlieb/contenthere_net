Title: The CMS Decorator Pattern
Date: 2009-07-22T08:03:00Z
Modified: 2015-01-06T12:16:00.132Z
Category: misc
Tags: development, architecture
Slug: 2009/07/the-cms-decorator-pattern
Authors: Seth Gottlieb

Web content management systems are very good at capturing, managing, and rendering semi-structured content. They give the contributor tools for controlling the organization of a web site and the layout and composition of pages. However, when it comes to strictly relational, tabular data, all those features like versioning and preview tend to get in the way. You wouldn't build a customer relationship management (CRM), enterprise resource planning (ERP), or accounting system on top of a content repository designed to stage and deploy content. There are better tools for that.  

A common pattern when you want to present highly structured, relational data on a website alongside managed content is to manage those data outside the CMS and then use the CMS to organize and augment them. I have seen this pattern used for years but it didn't occur to me until Will Ezell (from [dotCMS](http://www.dotcms.org/)) mentioned that this was a direct application of the [Decorator Pattern](http://en.wikipedia.org/wiki/Decorator_pattern). Until that point, I had mainly used the decorator pattern at the object oriented class level. Since then, I have been using the phrase "use the CMS to decorate your \_\_\_\_\_\_\_ data." This description seems to resonate with people even if they are not familiar with the book [Design Patterns: Elements of Reusable Object-Oriented Software](http://www.amazon.com/gp/product/0201633612?ie=UTF8&amp;tag=contenthere-20&amp;linkCode=as2&amp;camp=1789&amp;creative=390957&amp;creativeASIN=0201633612)

<img alt="" border="0" height="1" src="http://www.assoc-amazon.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=0201633612" style="border:none !important; margin:0px !important;" width="1"/>

. 

  

Here is a concrete example. Lets say that your ERP system is the system of record for your core product data: price, dimensions, materials, manufacturer, weight, distributor, availability, sku and size options. But these data are dry and not at all compelling to the consumer browsing an e-commerce site. You can use the CMS to add additional information like a description and photos of the product. You can also use the CMS to control where the product appears on the website: within a collection of promoted items on the home page; as a featured product on a department page; as part of an email newsletter. When designing the shopping experience of your customers, the features of a web content management system really come in handy. You can preview and stage the pages so you can see what they will look like. You can use scheduled publishing to make the pages go live on a specific date.  

From an architectural perspective, the integration does not have to be that complex. Essentially the content items that decorate your catalog data just have to be aware of a primary key that is managed in your ERP system. Most web content management systems allow to configure a content editing form to use a database to populate a dropdown box or a more complex browsing interface. So a user might go into the CMS, create a new "Product" asset and select a Product ID from a dropdown list and then add content to "decorate" that product. Most CMS rendering engines can read from external data sources. Once you have that shared key, the assembling of content and data happens at rendering time.  

This is one of those approaches that is so obvious that it is frequently ignored and overlooked. Once you are aware of this pattern and keep it in mind as an option, it becomes much less tempting to overload your CMS implementation to manage data that it was not designed to manage. The user interfaces can be optimized for specific purposes and your architecture becomes cleaner. When a content type gets complicated to manage, you should always ask yourself "am I using the right system to manage this data?"
