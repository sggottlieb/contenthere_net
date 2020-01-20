Title: What to do when that Wordpress welcome email doesn&#39;t get to the new user
Date: 2013-03-14T09:00:00Z
Modified: 2015-01-06T12:30:24.995Z
Category: misc
Tags: wordpress
Slug: 2013/03/what-to-do-when-that-wordpress-welcome
Authors: Seth Gottlieb

When inviting a new user to a Wordpress site, the default behavior is for the system to put that user into a pending state and only activate her when she clicks through on an invitation email. However, if that user never receives the email, you are kind of stuck. You can't activate her because she doesn't show up on the users list. You can't re-create her because she is in that limbo state. I am told that the invitation expires and you can re-invite after that point. But who wants to wait?  
  
The work around that I use is to simply delete the record from the wp_signups table:  

<pre>delete from wp_signups where user_login = 'username';</pre>

  
Where username is the username you set when you tried to invite the user.  
  
If you don't have direct database access, I would recommend ticking the box that says "Skip Confirmation Email." After that, you can manually set the password and send it through a secure service like [Lockify](https://lockify.com/e), or you can send instructions to the user to use the password recovery system to set their own password.
