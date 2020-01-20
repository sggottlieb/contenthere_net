Title: Variable control lists
Date: 2008-10-23T13:34:00.001Z
Modified: 2015-01-06T12:15:39.836Z
Category: misc
Tags: 
Slug: 2008/10/variable-control-lists_23
Authors: Seth Gottlieb

Your typical editor is conflicted.  On the one hand, he likes to have direct control over what articles are promoted on every page of the site.  On the other hand, he realizes that he may not have the time to exert this control.  When editors have to manually place articles in every promotional list, they risk letting the important pages (home pages and section front pages) get stale as they tend to other things.  When they allow the templating logic to automatically select articles to highlight, they get frustrated by the judgement of automated filtering rules ("why is that article promoted more than this more important article?").  They want to be able to override the automated logic when they have the idea that they could do better.  
  
Here is a classic trick to establish compromise between the extremes of manual control and automation. I have implemented this on many different web content management platforms and it should work on yours.  I call it "variable control lists."  The basic idea is that you allow an editor to select 0-_n_ articles to include in a promotional list that displays n items.  The template logic shows the articles that the editor selected and then fills in the rest of the positions with the results of a query.   So, if an editor picks 0 articles to spotlight, the template logic selects n.  If the editor selects 3, the template logic selects n-3 articles and lists them after the editors picks.    
  
A couple of nuances should be considered.  First, you want to make sure that supplemental list does not include any of the same articles that the editor selected.  Second, you might want to apply some additional rules like having the template disregard the editor's picks if they are past a certain age.  That really depends on the type of site you are running.   
  
Try it out and see how it works for you.  I am especially interested in learning of platforms that this would _not_ work on.   
