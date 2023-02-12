# Content Here Source Code

[www.contenthere.net](www.contenthere.net ) is published using the static site generator [Pelican](https://docs.getpelican.com/en/stable/) and a slightly modified version of the [Blue Penguin theme](https://github.com/jody-frankowski/blue-penguin). Python dependencies are managed using [Pipenv](https://github.com/pypa/pipenv).  This is the source code for the posts and the publishing framework.

make html

# Adds Atom feed
make publish 

# Creates new post

invoke newpost 

# Syncs to server

s3cmd sync -r output/ s3://www.contenthere.net