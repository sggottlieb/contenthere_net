Title: Double International Snapshot
Date: 2015-03-23T15:32:00.001Z
Modified: 2015-03-23T15:32:17.784Z
Category: misc
Tags: Translation Proxy
Slug: 2015/03/double-international-snapshot
Authors: Seth Gottlieb

Last year I wrote a post about [two deployment patterns to prevent source language bleed through](http://www.contenthere.net/2013/02/preventing-source-language-bleed-through.html) when using a [transaction proxy](http://www.contenthere.net/2012/02/introduction-to-translation-proxies.html). If you don't want to click through on the link, source language bleed through can happen when a visitor views a page with text that has not been translated yet. Most translation proxies have an option to use machine translations for untranslated text but this is not always desirable. 

In our experience, the "International Snapshot" pattern works very well as long as the customer is willing to freeze their content while the site is being translated. Without a content freeze it impossible to make the site completely translated. You never know when a content editor is going to publish a new string. It is also inefficient because the translators might need to translate text that is only on the site for a few hours. For example, a translator might be sent a task to translate a sentence with a typo that will be corrected in a matter of minutes.

But not everyone is willing to interrupt their publishing flow. Thanks to the wonderful world of content management systems, people are used to being able to publish whenever they want. To accommodate customers who have no tolerance for bleed through or content freezes, we have started to apply a new pattern that I call the "Double International Snapshot." This pattern is identical to the "International Snapshot" pattern but has an added layer of a translation instance which effectively freezes the content for the translators.

<a href="https://www.flickr.com/photos/sggottlieb/16688734509" title="Double International Snapshot by Seth Gottlieb, on Flickr"><img alt="Double International Snapshot" height="333" src="https://farm9.staticflickr.com/8592/16688734509_102a7c3eb0.jpg" width="500"/></a>

In this pattern, you have three instances of the site:

1.   The Original Site that is serving your source language visitors today. This site can be updated regularly for the benefit of source language visitors. 
2.   A "Translation Snapshot" that is a point-in-time snapshot of the Original Site. This site provides a stable environment for new content discovery and staging translations.
3.   An "International Snapshot" that is a point-in-time snapshot of the Translation Snapshot. This is the site that your target language visitors will hit through the proxy.

The translation process works like this. When you think it is time to refresh the translated sites, you refresh the Translation Snapshot. This freezes the content for the translators so that they can complete their work without new content constantly appearing. The Translation Snapshot can be finalized and go through all sorts of testing to make sure that it as perfect as it needs to be. Once you are satisfied that the Translation Snapshot is production-ready, you refresh the International Snapshot from the Translation Snapshot. Because the translations for the new content are already in the proxy, there will be no bleed-through.

The Double International Snapshot allows content editors to constantly publish new content to the source language site without compromising the stability of the translation environment. The translated sites can be fully verified for translation completeness and quality before going live. This pattern is an ideal solution for companies that don't want to risk source language bleed through but are not willing to compromise publishing freedom. But these benefits are not without cost, you do need to host three versions of your website and you need to build mechanisms for maintaining these snapshots. The Translation Snapshot site can be relatively low powered because it will get only a limited amount of traffic. If your site is simple and does not have any runtime server-side logic, both snapshots could be static HTML files hosted on Amazon S3. This can be done pretty easily with [GNU wget](http://www.contenthere.net/2012/01/fun-with-static-publishing.html).
