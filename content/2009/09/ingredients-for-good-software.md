Title: Ingredients for a good software development project
Date: 2009-09-02T20:54:00Z
Modified: 2015-01-06T12:16:00.517Z
Category: misc
Tags: development
Slug: 2009/09/ingredients-for-good-software
Authors: Seth Gottlieb

While nearly all of my consulting work is in software selection and technical strategy, I try to have at least one implementation project in the works so that I can stay relevant as a technologist. For my current project, I am building the technology infrastructure for a new web based startup. The project is going really well and I thought I would share some reasons why.  

  

  
*   __Great Client.__ My client is totally non technical and this is his first startup. He found me through a mutual friend that we both think very highly of. His lack of technology experience means he has not picked up any of the bad habits of technology owners. He didn't force a detailed Gantt chart with a bunch of imaginary dates and tasks. His trust in me helped us to collaboratively prioritize and plan work around his schedule. I have followed through on all of my commitments so the trust has only gotten stronger. 
  
*   __Fluid Design.__ The concept has evolved substantially since its original inception. A critical part of the design process involves going through the application with prospective customers and then talking through how to incorporate their feedback. We have done a really good job of keeping things flexible without adding complexity. Some of the more speculative ideas are faked a bit until we get an indication of their viability. The underlying machinery is only reworked when we are really onto something. We have plans to do a holistic refactoring once the design is frozen and we are ready to start preparing the application for beta customers.
  
*   __Strong Frameworks.__ Building the application on top of the [Django](http://www.djangoproject.com/) web application framework makes development incredibly fast. Python has a great unit test system where the tests are written in the comments of the code. This makes them easy to maintain. All of the data administration interfaces are provided for free and, because everything is data driven, the client has a lot of control over what he shows potential investors.
  
*   __Simple Tools.__ All of the work is planned using tickets and milestones in a service called [Unfuddle](http://unfuddle.com/) (looks a lot like [Trac](http://trac.edgewall.org/)). The information is very accessible and email notifications keep everyone up to date. I am probably going to bring another developer on board to help with the beta and I think that setting him or her up with a development environment is going to be really easy. Just pull everything down from Subversion and launch the text editor of choice. 

  

I am not fooling myself into thinking all projects can be like this. You don't always get to choose your clients or your tools. Often other constraints are forced upon you. But you can make some adjustments to achieve incremental improvements. For example, on another project for a very large, established client, I used to say "we are going over a waterfall in an agile barrel" meaning that the upper management saw a [waterfall model project plan](http://en.wikipedia.org/wiki/Waterfall_model) but internally, we were being as agile as possible. We tried to be vague rather than guess and commit. We made decisions that didn't preclude other options. We made opportunities to refactor code. So, rather than throwing up your hands and accepting a recipe for failure, think of how you can get the ingredients for success.
