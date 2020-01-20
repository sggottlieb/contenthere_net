Title: Managing Projects with Trac
Date: 2006-08-22T08:23:00.002Z
Modified: 2015-01-06T11:32:19.203Z
Category: misc
Tags: 
Slug: 2006/08/managing-projects-with-trac_36
Authors: Seth Gottlieb

[This is a continuation of a sporadic series that started with [this post](http://www.contenthere.net/2005/03/managing-projects-open-way.html)]  
  
In open source projects, bug lists are not just to record of defects, they are often also the main organizing system for the project.  Bug lists are where new ideas for functionality are captured, releases are planned, and the vision of the project assembles.  Not everyone can contribute code, but they can report bugs and their needs.  I don't think corporate I.T. shops leverage issue trackers enough.  They mainly see them as a backward looking reactionary tool rather than a forward looking planning tool.  
  
We have standardized on the open source issue tracking software [Trac](http://trac.edgewall.org/) by [Edgewall Software](http://www.edgewall.org/).  Here is my system for using it....  
  
Usually my first engagement with a client is a short scoping/roadmap project.  During this time, I collect high level requirements and put them into a roadmap, recommend technologies, and do some estimation and planning around the initial release of the application.   During this phase, I usually work in a spreadsheet because it is quick for data entry and editing.   I try to organize functionality into phased releases that balance time to delivery and functionality.  I generally follow the practice of making the releases as small as possible.   It is also a good idea to organize releases into themes.  This makes it easy to communicate to stakeholders what is coming up next and when.  
  
I start using Trac at the start of the first release project.  Here is how I configure it:  

*   I create a component for each of the major functional areas of the application. Usually there is a "content" component.
*   I create version numbers for each of the releases. 1.0 is the initial release. Then 1.1 for the release after that and so on.
*   To the default ticket types (defect, enhancement, task), I add "port" to represent something that exists in legacy system that is being replaced; and "question."
*   In the Roadmap section, I create the following milestones for each release:

*   Infrastructure setup  
    
*   Design (e.g. 1.1 Online Calendar: 1 Design)  
    
*   Code Complete (e.g. 1.1 Online Calendar: 2 Code Complete)
*   QA Complete (e.g. 1.1 Online Calendar: 3 QA Complete)
*   Maintenance (e.g. 1.1 Online Calendar: 4 Maintenance)

Trac comes with some basic reports but you can add new reports through the user interface if you know SQL.  I create a report for each release (filtering on the version field).   The Roadmap page is a dashboard showing how many tickets have been assigned to each milestone and how many are outstanding.  When I think that I have a good idea of how to implement a feature, I add comments to the ticket.   I can also associate files such as screenshots when I want to show how the feature might look.   
  
So that is how I use Trac as an issue tracker.  But Trac does so much more.  Since we use [Subversion](http://subversion.tigris.org/), we set it up to browse the source code repository.   There is also a wiki feature which I use for project documentation.  In general, when documentation is on a wiki, I find that people become more concerned with the content than with the formatting.  That is a good thing because you want to reduce the effort to make documentation current.  Formatting puts up an unnecessary barrier because it sets the expectation that something has to be really polished before it is shown.   
  
The Timeline is a view of all that is happening on the project.  You can filter what to include from the following options:  milestones, ticket changes, repository checkins, and wiki changes.  The Timeline view also publishes to RSS so you can see all the information within your RSS reader.  However, I still like to get these notices over email which is another configuration option.   There is nothing like knowing immediately when someone checks in some code so that you can review and advise if there is a preferred way.  Our developers  usually  add the ticket number to their checkin comment so you can see why the code was checked in.   
  
And that is all there is to it.  Trac is a simple tool but extremely useful.   All of my clients that have used it so far have liked it although they hate it when I assign them tickets ;)
