Title: Keeping Django Settings Generic
Date: 2012-04-04T12:13:00Z
Modified: 2015-01-06T12:30:24.229Z
Category: misc
Tags: development, django
Slug: 2012/04/keeping-django-settings-generic
Authors: Seth Gottlieb

__Warning: Geeky Coding Post__

  
  

I have worked on a number of Django projects and settings.py is always a problem. This is the configuration file with information like how to connect to the database and what Django apps to install. Some of this information is sensitive (like your database password or an API key) and you don't necessarily want it in your source code control system. Other information is instance-specific like the host that your database is sitting on.   

In the past, I have managed the production settings in the core settings.py file and then imported an override file at the bottom that overwrites certain settings with my local settings. The code looks something like this:

  
<code><br/> <pre><br/>    try:<br/>        from settings_local import *<br/>    except ImportError:<br/>        pass<br/>    </pre><br/></code>  

Then all you have to do is ignore your settings\_local.py from your source code management system and exclude the file when bundling up a deployment package. This works pretty well except when you don't want to store a password in your SCMS or if you have lots of different settings for different environments that you are deploying to.

  

What you want to do is have those settings living permanently as part of your target environment(s) and just deploy a neutrally configured application. Last week I stumbled on a good technique for this that I thought I would share. The strategy comes from an article on [Tim Sawyer's Drumcoder blog](http://drumcoder.co.uk/): [Apache Environment Variables and mod\_wsgi](http://drumcoder.co.uk/blog/2010/nov/12/apache-environment-variables-and-mod_wsgi/). The article shows how you can access environment variables from settings.py.

  

After following these directions, I was able to do things like:

  
<code><br/> <pre><br/>    DATABASES = {<br/>        'default': {<br/>            'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>            'NAME': 'APP_DBNAME' in os.environ and os.environ['APP_DBNAME'] or 'dbname',<br/>            'USER': 'APP_DBUSER' in os.environ and os.environ['APP_DBUSER'] or 'dbuser',<br/>            'PASSWORD': 'APP_DBPASS' in os.environ and os.environ['APP_DBPASS'] or 'password',<br/>            'HOST': 'APP_DBHOST' in os.environ and os.environ['APP_DBHOST'] or 'localhost'<br/>        }<br/>    }<br/>    </pre><br/></code>  

I am surprised that I limped along so long before using this technique. An alternative method would be to install a python package on the server (in the python libraries) that just contains these constants. But this just seemed easier to me.  
