Title: Django Action Item Follow Up
Date: 2010-04-05T11:40:00Z
Modified: 2015-01-06T12:16:16.928Z
Category: misc
Tags: django
Slug: 2010/04/django-action-item-follow-up
Authors: Seth Gottlieb

While moderating a comment on my "[10 Django Master Class action items](http://www.contenthere.net/2009/11/10-django-master-class-action-items.html)" post, I was inspired to evaluate how I am doing on these action items and whether they are helping. Below is a brief summary of my progress; but first a little background. Recently, I had the rare opportunity to rebuild (from the ground up) an application that I wrote for a client. The context was that the first version of the application was a prototype that I built to help demonstrate an idea to potential investors and customers. The prototype served its purpose excellently. It was able to evolve alongside the idea as my client got feedback and refined the value proposition. We came out of the prototyping phase with a strong vision and an excited group of investors and beta customers. To minimize costs I avoided refactoring the application and cut a lot of corners. By the end of the prototype phase, the idea had changed so much that we were really faking functionality by overloading different features. Still, for a ridiculously small investment, my client was able to develop and market test an idea. And now I get to build the application for real and apply the best practices that I learned about in the Django master class. Here is what I am doing and how it is working out.

  

1.   __Use South for database migrations (adopted).__ I have grown so attached to South that I find it hard to imagine life without it. This is especially important because I am managing different environments and the object model is changing as I add new features.  
    
2.   __Use PostgreSQL rather than MySQL (adopted).__ I am steadily getting more comfortable with PosgreSQL. [pgAdmin](http://www.pgadmin.org/) has been really helpful as I get up to speed with the syntactical differences from MySQL. So far, the biggest differences have been in user management and permissions.  
    
3.   __Use VirtualEnv (adopted).__ VirtualEnv + [VirtualEnv Wrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) has been great. For a little while I was working on both the prototype and the actual application. VirtualEnv made it easy for me to switch back and forth. This will also be helpful when I upgrade to Django 1.2.  
    
4.   __Use PIP (adopted)__. I really like how you can do a "pip freeze" to create a requirements file that you can use to build up an environment.  
    
5.   __Break up functionality into lots of small re-usable applications (adopted)__. The prototype had one app. The production app that I am building has 6. One of the apps contains all the branding for the application and some tag libraries. Templates in other apps load a base template from my "skin" app. The best part of using this strategy is in testing and database migrations because you can test and migrate a project one app at a time. The hardest thing for me to figure out is how to manage inter-dependencies and coupling. One strategy that has worked well for me is to focus dependencies on just a couple of applications. For example, I have profile application which manages user profiles (extended from the base django.contrib.auth.User model.). I have other apps that relate to people but I am careful to create foreign key relationships to the User model rather than my profile model.  
    
6.   __Use Fabric for deployments (adopted).__ One word. AWESOME! I have scripts to set up a server and deploy my project without having to ssh onto the server. The scripts were not that hard to write. I took inspiration from some great posts ([here](http://lincolnloop.com/blog/2009/sep/22/easy-fabric-deployment-part-1-gitmercurial-and-ssh/) and [here](http://morethanseven.net/2009/07/27/fabric-django-git-apache-mod/wsgi-virtualenv-and-p.html)). Now I can reliably push code (and media) with one local command. I am managing the development of another site running a PHP CMS and I am strongly considering having the team use Fabric for that as well.  
    
7.   __Use Django Fixtures (adopted)__. Managing fixtures in JSON has turned out to be really easy. I typically have two fixtures for each app: initial\_data.json and &lt;app\_name&gt;\_test\_data.json. initial\_data.json mainly contains data for lookup tables. It is run automatically when syncdb (the Django command to update the database schema) is run. I typically create these files with the dumpdata command and then edit them manually.  
    
8.   __Look into the Python Fixture module (not adopted)__. I looked into this module but, to be honest, editing the JSON files is pretty easy so I don't see the need for it.  
    
9.   __Use django.test.TestCase more for unit testing (adopted).__ I have been doing a considerable amount of test driven development (TDD). It all started when I wanted to rewrite the core functionality but I needed to wait for someone else to re-build the HTML in the presentation templates. Now I have around 130 unit tests that I run before I commit any code. Focusing on unit testing has made me write code that is more atomic and easier to test. Now I think "how will I test this?" before I write any code.  
    
10.   __Use the highest version of Python that you can get away with (adopted).__ A big motivator for me here was when I upgraded my workstation to Snow Leopard which ships with Python 2.6.3. Getting 2.6.3 on my server was a little more complicated. I wound up using a host that comes with Ubuntu Karmic Koala which also comes with 2.6.3. I am really pleased with Ubuntu and it seems like most of the Django community is going that way.  
    

  

I feel really lucky for the opportunity to rewrite an application and apply lessons learned. Too often you are stuck managing code that you (or someone else) wrote before you knew what you were doing. That is, before the functionality of the application was fully understood; before a feature of the API was available or known; before a more elegant solution was discovered. I am sure that I will continue to learn new things and want to apply them and I plan to continually refactor as long as I am involved with this project. But this full-reset has been a great experience. 
