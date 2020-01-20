Title: Retro-Fitting Your WCM System for Localization
Date: 2012-07-19T13:39:00Z
Modified: 2015-01-06T12:30:24.511Z
Category: misc
Tags: localization, Global Marketing Operations
Slug: 2012/07/retro-fitting-your-wcm-system-for
Authors: Seth Gottlieb

Not long ago, I wrote a post called [Planning for Localization](http://www.contenthere.net/2012/04/planning-for-localization.html) to give tips for enabling internationalization even if localization is not part of your initial launch requirements. As I mentioned before, internationalization is one of those requirements that gets de-scoped with much regret later on. How bad is it? In my experience, enabling internationalization post launch is often a non-starter.   

The work involved breaks down into 4 categories:

  

  
2.   __Presentation template localization.__ Swapping out static strings for references to resource bundles or creating language-specific variants of templates. The level of effort depends on the number of templates and the extent to which they have static text. Text within images is particularly bad because finding the source files can be a real challenge.  
    
3.   __Repository re-organization.__ There may be some work to re-organize the content hierarchy. For example, you might want to drop the primary language down from the root node to make room for other languages. This may affect the [URL structure](http://www.contenthere.net/2012/02/url-management-for-a-global-business.html) and you might need to do URL rewrites. Different platforms have different strategies for handling multi-lingual content. In the best case scenario, every asset has the built-in capability of being multi-lingual. In the worst case, the repository doesn't support internationalization at all.  
    
4.   __Workflow updates.__ This is work to update the workflows to add steps for localization or triggers to instantiate a translation workflow when the asset in the pivot language changes. There is also an organizational aspect here. Often you need to have someone with both the language.skills and access to the staging area to preview localized content before publication.  
    
5.   __Language fall-back logic and other multi-lingual configurations.__ This is kind of a catch all for any type configuration that you would skip on a mono-lingual website and only do for a localized website.
  

  

I asked around my network of systems integrators for their experiences and they are consistent with mine. Several of my colleagues said that an internationalization retro-fit often costs as much as a complete do-over. That can be in the __$200,000 to $400,000__ range. You might also need to __add another couple hundred thousand dollars__ to license a new WCMS if your current platform doesn't have strong internationalization support. Others came in a lower worst case scenario of around 50% of the initial implementation cost. Of course, the level of effort depends on the size and complexity of the site, the native internationalization capability of the platform, and the number of internationalization corners that were cut in the initial implementation.   

The problem is that you don't really know the extent of re-work involved until you start the project and dig into the code. Sites that have been around a while often have functionality or display templates that are rarely or never used. You still need to internationalize them just in case. Also, if you are working with a new systems integrator, they need to assume that the initial implementer didn't know what they were doing and buried [stinky code](http://en.wikipedia.org/wiki/Code_smell) all over the place. It's a bit like when you open up a wall for a small home project and you realize that some serious structural problems need to be addressed before you do anything else. So any fixed-bid proposal is going to be based on a worst case scenario of having to do extensive refactoring.  

The systems integrators in my network have started to plan for internationalization in all of their projects. They ignore their client's request for a U.S. English-only website because eventually someone is going to realize the market potential of U.S. Spanish or opportunities for global expansion. If you are building a new website, make sure that your systems integrator thinks this way. If you are considering internationalizing your mono-lingual site by adding a new locale, the most practical solution is to deploy a [translation proxy](http://www.contenthere.net/2012/02/introduction-to-translation-proxies.html), which hosts the translations _outside_ of your website. This means that no retrofitting is required and you can avoid all of that expensive and risky rework.
