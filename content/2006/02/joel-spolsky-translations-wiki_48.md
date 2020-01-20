Title: Joel Spolsky&#39;s Translations Wiki
Date: 2006-02-14T11:28:00.002Z
Modified: 2015-01-06T11:32:17.138Z
Category: misc
Tags: 
Slug: 2006/02/joel-spolsky-translations-wiki_48
Authors: Seth Gottlieb

Joel Spolsky, author of the very popular technical blog [Joel On Software](http://www.joelonsoftware.com/), is [currently doing an experiment](http://www.joelonsoftware.com/items/2006/01/27.html) of using a wiki for translating his blog content into other languages. From his global readership, Joel definitely has the resources to do the translation, it was just the management and coordination that proved to be the problem:  

>  Sadly, I fell down in face of the effort needed to maintain 30-odd local language versions. Such a job can't be coordinated by one person, especially when that person is me.The [translation wiki](http://local.joelonsoftware.com/mediawiki/index.php/Main_Page) (powered by [MediaWiki](http://www.mediawiki.org/wiki/MediaWiki)) seems to be having some success.  Joel announced the wiki on January 27th and there are already 117 registered users generating a good amount of content.  The Spanish, Greek, Hebrew, Japanese, Polish, and Russian sections have the most translations.   

A wiki allows users to work directly with each other to sort out issues like "speakers of the Flemish dialect ask me to change it one way, then speakers of Netherlands Dutch suggest putting it back, and I have no idea what they're talking about!" What of the concern of vandalism? Joel feels confident that the community will work it out: "If you're feeling naughty, add some fart jokes to somebody's excellent translation. We'll see if the community spots it and fixes it." Fortunately, the Joel's readership is probably dedicated and smart enough to be up to the task. (BTW, there are two very good articles on [Wikipedia](http://www.wikipedia.org) in the Boston Globe [here](http://www.boston.com/business/technology/articles/2006/02/13/many_contributors_common_cause/) and [here](http://www.boston.com/business/technology/articles/2006/02/13/the_idealists_the_optimists_and_the_world_they_share/) that talk about the culture of the Wikipedia). There is also a [page](http://local.joelonsoftware.com/mediawiki/index.php/Clarifications_and_Explanations) that serves a place to discuss cultural reference and terminology questions. There is also a kind of [logistics page](http://local.joelonsoftware.com/mediawiki/index.php/Talk:Main_Page) and a [guidlines page](http://local.joelonsoftware.com/mediawiki/index.php/Guidelines_for_Translators) to mention best practices.

So what are the weaknesses of this format? The key one that I see is the lack of structure. However, it is really no worse than the source (blog entries) the only thing missing is a field for date and title. There is a guideline to link back to the source article so it may be possible for the translations to share this information with the original article through a very loose foreign key relationship. Using WikiText may make it easier to parse content than giving users HTML WYSIWYG editors. It is not too difficult to parse MediaWiki text. For example, "==" means a HTML heading level two (H2) tag. But in a WYSIWYG editor, you would most likely get some kind of font tag which would give you no clue that this was the heading of a section.

I will keep my eye on the Joel on Software translation wiki. It looks like it has all the ingredients for successful wiki: dedicated readership, good content, and community.   