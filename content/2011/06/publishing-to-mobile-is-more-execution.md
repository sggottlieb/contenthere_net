Title: Publishing to mobile is more execution than platform
Date: 2011-06-09T09:41:00Z
Modified: 2015-01-06T12:16:18.318Z
Category: misc
Tags: selection, mobile
Slug: 2011/06/publishing-to-mobile-is-more-execution
Authors: Seth Gottlieb

Mobile publishing functionality is becoming an increasingly important requirement for web content management (WCM) selections and I am starting to hear more customers ask "can this product do mobile?" The fact is, most WCMS have that core functionality built into their DNA since multi-format publishing has been going on since the beginning of time. In the early days it was publishing "printer friendly" versions, PDFs, portlets, or RSS ([we only dreamed of mobile](http://www.contenthere.net/2011/03/designing-for-mobile.html)). Now we are talking layouts and navigation that are optimized for smaller screens. In fact, what differentiates a WCMS from a document management system is the "rendering" or "presentation" tier that takes structured content and applies a layout template to generate a formatted output. The specific purpose of the rendering tier is to be able to reuse content and publish to different formats.  

Just because nearly all WCMSs have the foundation to support a decent experience for a mobile user, it doesn't mean mobile will come easily to your solution. Why? Because WCMSs are also very flexible and give you plenty of opportunity to shoot yourself in the foot. WCMSs allow you to model your content with enough structure to make it reusable, but they don't require it. You can still use a single generic content type and turn your WCMS into a [6 million dollar WYSIWYG editor](http://www.contenthere.net/2006/10/the-6-million-dollar-wysiwyg-editor.html). You can fail to [keep your content DRY](http://www.contenthere.net/2010/07/keeping-your-content-dry.html). If you committed these sins, your mobile project is when they will come home to roost.  

While structured, reusable content is a key to success in mobile and nearly all WCMSs support some degree of content modeling, there are a few non-universal features that will make supporting mobile easier. Look out for these features when evaluating WCMSs.

  

*   __Configurable template selection rules.__ All WCMS should be able to associate presentation templates to content types. You should look for a platform that allows you to configure template selection rules based on criteria like the section of the site or the user agent (browser). Otherwise, you need to build complex switching logic into your display templates.  
    
*   __Themes__. A theme is a collection of templates that define a comprehensive style (layouts, behavior, font, palette, images, etc.) of the site. A theming model allows you to group templates that are used for a style. This makes themes interchangeable and selectable so you can manage a mobile theme (or multiple mobile themes for different devices). It is particularly helpful if the platform allows themes to override each other — similar to cascading style sheets. For example, you could have a base theme and specific themes that override selective elements of the base theme.  
    
*   __Multi-site content sharing__. Designing for mobile is not limited to layouts and styling. There is growing consensus around the value of having a separate site with content that mobile visitors are likely to want. This doesn't have to be fresh, mobile-only content. Rather, it is a subset of the main content with a simplified navigation. Some WCMSs will represent this mobile area as a different "site." Others will represent it as a folder in the hierarchy. Regardless of the semantics, you need to be able to have the same piece of content exist in both of those places at once. Different WCMSs use different metaphors to allow contributors to manage these placements: "locations," "aliases," "references." Some metaphors come more easily to contributors than others but all contributors need training to get it right.
  

<li><strong>True preview</strong>. Editors will want to see how the content is going to look on different devices before publishing. Some WCMS come with emulators that allow you to see a page as if it being accessed by a mobile device. I don't know how accurate these emulators are but they are probably good enough. If the WCMS does not have an emulator, you need some way to access that preview from another device. This can be complicated if the preview is not behind a readily accessible URL that you can point the device to. Some WCMS run preview off of the user's session data (the draft is not stored in the repository until it is deliberately saved). This will be a problem because mobile testing device will be in a different session. Some WCMS architectures (mainly baking-style systems) have a full site staging area. This makes it easier to run through a whole site of pre-published content from your mobile device.</li>  
  

Those are the key CMS features to look for. The rest is in the execution. In addition to content modeling, make sure you are working with a competent designer than knows mobile and web developers that know how to implement the design to make pages lightweight (for example: compressing HTML, CSS, and Javascript; using sprites for buttons and logos; and effective placement of script references to prevent blocking). Also don't forget to account for increased testing.
