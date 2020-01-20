Title: Introduction to Translation Proxies
Date: 2012-02-16T10:47:00Z
Modified: 2015-01-06T12:30:24.160Z
Category: misc
Tags: localization, Translation Proxy, Global Marketing Operations
Slug: 2012/02/introduction-to-translation-proxies
Authors: Seth Gottlieb

Recently, I have been doing a lot of work with translation proxies. A translation proxy is a service that sits in front of your website and applies translations so that different audience segments can see your content in their local languages. You point various DNS entries to the proxy so that request goes through the proxy service to your native language website. On the return trip, the proxy applies translation rules to the HTML in the response. It’s a little like when Google Chrome asks you to run Google Translate on the foreign language page you are looking at. However, unlike Google Translate, these translations are done by professional translators and there is a multi-step workflow to ensure that the translations express correct information and tone. Of the three ways that [Global Marketing Operations](http://globalmarketingops.com/) can localize websites, translation proxy is the fastest growing option. 

  

<a href="http://www.flickr.com/photos/sggottlieb/6883196269/" title="Translation Proxy Architecture by sggottlieb, on Flickr"><img alt="Translation Proxy Architecture" height="415" src="http://farm8.staticflickr.com/7036/6883196269_af000bce86.jpg" width="500"/></a>

  

This approach has several benefits. Among them:

  
<ul><br/> <li><h3>There is no need for the core publishing platform to have multi-lingual capabilities</h3><br/> <p>The publishing platform behind the primary language site may not support localization features such as storing different localized versions of a piece of content or being able to easily localize display templates.  Many CMS implementations start with a localization-capable product but then cut corners, which prohibits adding alternate languages down the road.  Building a site for localization takes planning, skill, and investment that cannot be justified if localization is less than a drop-dead requirement at the time of the initial implementation.  Retrofitting is a lot of work. </p><br/> </li><br/> <li><h3>You can translate both content and template text in one place</h3><br/> <p>In a typical translation scenario, we need to translate both the content (which the content contributors manage) and the presentation templates (code that the developers manage).  See this screenshot for an annotated view (sorry for the color palette choice.  I understand if you have a sudden craving for a Big Mac).  </p><br/> <p><a href="http://www.flickr.com/photos/sggottlieb/6837888675/" title="Template vs. Content by sggottlieb, on Flickr"><img alt="Template vs. Content" height="337" src="http://farm8.staticflickr.com/7006/6837888675_18965fdf3c.jpg" width="500"/></a></p><br/> <p>With other localization approaches, you need to localize these aspects separately: the content through an editorial workflow and the template text through a software development life-cycle.  In the translation proxy approach, all of this text can be localized together. </p> <br/> </li><br/> <li><h3>You can leverage your main site’s interactive functionality.</h3><br/> <p>Because requests are proxied back to your primary language site, all interactive features (including search, contact forms, and even commerce transactions) will continue to be supported.</p><br/> </li><br/> <li><h3>Your content stays secure.</h3><br/> <p>Because the translation proxy only sees what regular visitors see, there is no risk to the security of the main site.  The one thing you want to watch out for is transactional functionality.  You want to make sure that the proxy service does not collect sensitive information that visitors submit to the website and also can create rules to ignore sensitive information coming back to the visitor.  </p><br/> </li><br/> </ul>  

Like with any technology, translation proxies are not ideal for every case. Here are some reasons why a translation proxy may not be right for you.

  
  

  
 *   
    
    ### Local markets cannot create original content in the proxy.
    
      
     
    
    A translation proxy only translates (or, in some cases filters) content from the main site. There is no clean way to add original content to a localized site managed by a translation proxy. This is perhaps the biggest show-stopper for some companies. If you have a local marketing team that wants the autonomy to develop original content for their local markets, a translation proxy is not going to help. They need to publish their content somewhere before it can be served through the proxy. Perhaps they could create areas on the main site for their specific regions but then they wouldn't be leveraging the proxy.
    
      
     
  
 *   
    
    ### A translation proxy will not allow you to neglect your localized sites.
    
      
     
    
    If you want to save money by putting up simple, (crappy,) static sites for local markets, a translation proxy is not a great solution. The translation proxy model is intended for managing localized versions of the primary site. Any new or changed content will display in the primary language until it is translated. You can contain translation costs by excluding certain sections from your localized websites (for example, you may not want to translate your blog or press releases). Still, with the proxy model, you need to consider the translation costs when you add new content to your website. One work-around could be to create a trimmed down, rarely-updated "international site" on your CMS and use the translation proxy to localize it for all your foreign markets.
    
      
     
  
 *   
    
    ### Translation volumes are difficult to predict.
    
      
     
    
    Unlike traditional translation projects, a translation proxy service is monitoring a constantly changing website so scope is going to be fluid. This is not an “invest and then rest” type of service. It requires a level of attention and planning commensurate with the level of work that is done on the main site. If you are serious about reaching into new markets, this investment should seem reasonable to you. It’s still cheaper than hiring in-country marketers to produce original content. Look for suppliers that offer a capacity model where you pay a fixed fee based on expected usage. This will protect you against a large per-word translation bill after your primary language authors have been particularly prolific.
    
      
     
  

  

While the translation proxy approach is not optimal for every business or website, its benefits are very compelling for many. A translation proxy may be worth considering if you learn that your sophisticated interactive website was not built with localization in mind and you want to serve new markets with the same level of experience that you serve your home market.
