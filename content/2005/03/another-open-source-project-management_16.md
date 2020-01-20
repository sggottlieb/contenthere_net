Title: Another Open Source Project Management Tool
Date: 2005-03-25T15:28:00.002Z
Modified: 2015-01-06T11:32:14.053Z
Category: misc
Tags: 
Slug: 2005/03/another-open-source-project-management_16
Authors: Seth Gottlieb

A few months ago I was looking for a project planning tool (a la Microsoft Office) that would run on Linux. I found [Planner by Imendio](http://www.imendio.com/projects/planner/) and have been using it for a while now. Here is what I think:  

Positives  

*   The application is very simple to use and does not try to "outsmart" you like MS Project.  
    
*   The actual project plan is stored in a very easy to read and simple XML format. If you know a little bit about XSLT, you can do some cool things with the data.  
    
*   You can output the plan into an HTML document (the application uses XSLT to this) that you can distribute to people that don't have Planner. The output looks great in the browser but does not print very well. The Gantt section has a horizontal scroll that gets lopped off during print. To correct the problem I just edited the XSL files to remove the Gantt chart section.   
    
*   The application is very stable. I have had no crashed or file corruptions.  
    
*   Because the data file is plain text XML, you can actually use a source code system to manage it, see the differences and actually understand what is going on.   
    

  
Negatives

  
*   Planner does not run on Microsoft Windows. Gnome only.  
    
*   Planner is not Microsoft Project and, therefore, is usually not the company standard.  
    
*   Planner does not export into MS Project format. Although, you could set up xsl transforms to output to other formats (I think MS Project imports CSV). I doubt most project managers would be into tinkering with XSL. Come to think of it, most project managers would not be running Linux on a 12 pound laptop with the horsepower of a server.   
    
*   Planner only allows Finish to Start and Start to Start dependencies. I am a big fan of Finish to Finish dependencies.  
    
*   At first I thought the Lag feature did not work but then I noticed that it is done in hours. Surprise! I didn't expect that.  
    
*   You need to open the properties window to edit most fields of a task (such as resources). This can really slow down data entry.  
    
*   The "Work" column is deceptive for super-tasks. It is really duration. So if you have two concurrent sub-tasks or have multiple resources working on a sub-task, the work column of the super-tasks will not total the work of the sub-tasks. This makes various time estimation exercises difficult.  
    

  
   
Overall, I think Planner is a pretty useful tool with some limitations which may or not be deal breakers depending on your environment.  I am looking forward to checking out [Open Workbench](http://www.openworkbench.org/), an open source version of Niku Workbench which is part of Niku Enterprise Project Management Suite.  It's Windows only which will make it easier to adopt - especially when working with clients.
