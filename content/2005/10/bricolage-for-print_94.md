Title: Bricolage for Print
Date: 2005-10-03T08:30:00.002Z
Modified: 2015-01-06T11:32:15.203Z
Category: misc
Tags: 
Slug: 2005/10/bricolage-for-print_94
Authors: Seth Gottlieb

There was a recent thread on the [Bricolage](www.bricolage.cc) mailing list about using Bricolage to support print as well as web publishing. Given Bricolage's history and focus on publishing magazines and other periodicals, I am not surprised that there were some good anwers. One of the respondents recommended creating presentation templates that write to an XML format that can be imported into [Adobe InDesign CS](http://www.adobe.com/products/indesign/). In InDesign, you can create style sheets where you map incoming XML tags to InDesign layouts. If you don't have Adobe InDesign, another option is to use [Apache XML:FOP](http://xmlgraphics.apache.org/fop/) (pronounced Pho as in the Vietnamese food or Faux as in fake) which stands for Formatting Objects Processor. XML FOP is a very cool technology which takes an XML format and can output to different print formats with an emphasis on PDF.   

By using this technique, you can get excellent re-use between your print and web content and you will also be able to leverage Bricolage's powerful workflow functionality.
