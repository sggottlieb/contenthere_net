Title: Finally, Drupal Gets Deployment
Date: 2009-04-13T09:25:00Z
Modified: 2015-01-06T12:15:59.214Z
Category: misc
Tags: development, drupal, architecture
Slug: 2009/04/finally-drupal-gets-deployment
Authors: Seth Gottlieb

Greg Dunlap, over at [Palantir](http://www.palantir.net), has a post introducing [a new "Deploy" module for Drupal](http://www.palantir.net/blog/bringing-deployment-capability-drupal). Most of the site design and behavior in [Drupal](http://drupal.org) is controlled through configuration stored in the database (as opposed to files on the file system). The ability to move configurations from one Drupal environment to another (like development to staging to production) has been an achilles heel for Drupal. You can't just copy the database because then you would overwrite your production data with your test data. Assuming that you don't want to be developing on the live site, you had to choose between manually repeating your work on production or resorting to some awkward SQL scripting hacks to move database stored configurations from one database to another. These scripts were always brittle because of Drupal's reliance on an an ID field that is auto-incrememented - it is hard to keep those ID sequences synchronized across different databases. Deploy is a welcome improvement. 

  

Deploy works by allowing an administrator to create a "deployment plan" and extending other modules to give an option to add their configuration to the deployment plan. When the administrator executes a deployment, Deploy grabs all the configurations and content that have been associated with the deployment plan plus their dependencies and pushes them to a target environment. Greg's post has a nice screencast showing what it looks like to the user. Behind the scenes, Deploy adds a global unique identifier (GUID) field (in some companion tables) that is used to match up corresponding rows in the different environments.

  

It seems like Deploy falls short of addressing the common case where a deployment consists of a combination of configuration settings and content in the database and code in the file system. Deploy is for database-managed configuration only. For filesystem stuff, the handiest tool is a module called [Drush](http://drupal.org/project/drush) that allows you manipulate a Drupal instance from the command line. This allows you to create a script (preferably in [Ant](http://ant.apache.org/) or [Make](http://www.gnu.org/software/make/)) to move files around and update a Drupal instance. Maybe it would be possible to configure Deploy to _pull_ from another instance (rather than push). That way Deploy could be scripted in Drush for a comprehensive (database and file system) update.

  

These improvements are big steps in the right direction and reflect the impact of large companies running big and important Drupal sites. I expect this aspect of Drupal to be steadily improved and become standard practice by Drupal developers.
