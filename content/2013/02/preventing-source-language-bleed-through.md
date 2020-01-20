Title: Preventing Source Language Bleed-Through
Date: 2013-02-04T13:55:00Z
Modified: 2015-01-06T12:30:24.902Z
Category: misc
Tags: Translation Proxy, localization, Global Marketing Operations, Technical Strategy, wordpress
Slug: 2013/02/preventing-source-language-bleed-through
Authors: Seth Gottlieb

When considering a [translation proxy](http://www.contenthere.net/2012/02/introduction-to-translation-proxies.html) to localize a website, people often ask "if we change the content on the site, what will visitors see while the translators are working on the new translations?" Unless you are using machine translation as a backstop for untranslated content, your source language is going to show through. This is because a translation proxy doesn't cache full pages. Instead, they apply translations one fragment at a time. If it doesn't have a translation for a fragment, the translation proxy will register it as a new string to translate and send the original text through. This is a necessary trade-off to support dynamic websites. You can shorten the period of bleed-through by increasing your translation responsiveness and throughput, but to prevent bleed entirely you need apply one of the following techniques.

  

These two techniques are really just variations on the same theme of pointing the proxy at two versions of your site: one for content discovery and another one for production.

  
  

## International Snapshot

  

The "international snapshot" approach is where you create a non-current snapshot of your production site for international audiences. Depending on your translation velocity, this could be anywhere from a day old to a month old or more. Content discovery and translation is still done on the live site. But when an external visitor browses the site, they are getting a proxy-translated view of the snapshot. There is no bleed-through from the snapshot site because by the time the snapshot is refreshed, all of the translation rules have already been published. Here is a picture

  

  
<a href="http://www.flickr.com/photos/sggottlieb/8413982487/" title="International Snapshot Model by sggottlieb, on Flickr"><img alt="International Snapshot Model" height="288" src="http://farm9.staticflickr.com/8515/8413982487_0a937e43e2.jpg" width="500"/></a>  

  

This is what we are doing for the new [www.lionbridge.com website](http://www.lionbridge.com). We wrote some scripts to do a full snapshot of the site (code, database, and other files) to another virtual host on the same servers. If you are using a more sophisticated platform than Wordpress, you could probably set up another publishing target and just publish there when you want to update your snapshot.

  

## Translate Staging

  

The "translate staging" option follows the same pattern as international snapshot. With translate staging, however, you do your content discovery and translation on the staging server (which has content which hasn't been published yet) so your translations are ready _before you publish your content_. Once your translation queue is down to zero, you can publish your source content to your live site and the translation rules will be waiting to be used. 

  

<a href="http://www.flickr.com/photos/sggottlieb/8414009345/" title="Translate Staging Model by sggottlieb, on Flickr"><img alt="Translate Staging Model" height="288" src="http://farm9.staticflickr.com/8358/8414009345_30c572a20b.jpg" width="500"/></a>

  

With "translate staging," you need to make sure:

  

1.   Your staging site is publicly accessible. You will not be able to view the site through the proxy unless it is available on the public internet. For security reasons, you can limit access with a firewall and also add authentication to the staging site.
  
3.   Your staging site only contains translation ready content. If you have are using your staging site for your editorial process, you might wind up discovering draft content that will never be published. Since this is obviously a waste of time and money, it's best to create a staging instance that only has content that is ready for publishing.
  

  

Here is a summary of the process

  

<a href="http://www.flickr.com/photos/sggottlieb/8445666404/" title="Lifecycle of a content update by sggottlieb, on Flickr"><img alt="Lifecycle of a content update" height="308" src="http://farm9.staticflickr.com/8371/8445666404_b6607263ca.jpg" width="500"/></a>

  

## What to choose?

  

Which approach is right for you depends on your requirements. If, because of regulations or communications policy, you are required to publish new content to all languages simultaneously, you need to go with the translate staging option. If, like it is with us, you can allow your localized sites to lag behind the primary site, the international snapshot option is usually most attractive. And, of course, letting source content leak through may be acceptable if your site is less formal. The most important thing is that you have options. 
