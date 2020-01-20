Title: Zope Development Tools
Date: 2005-12-01T11:38:00.002Z
Modified: 2015-01-06T11:32:15.437Z
Category: misc
Tags: 
Slug: 2005/12/zope-development-tools_38
Authors: Seth Gottlieb

I just got a chance to view the automatically generated Plone API documentation site: <http://api.plone.org/>. As someone with a Java background, I was really happy to see such a familiar [Javadoc](http://java.sun.com/j2se/javadoc/) style format. Of course, since Python is a dynamically typed language, the documentation cannot tell the data type of a method's arguments (one of the primary thing I use Javadoc for). In order for that to happen, the documentation generation tool would have to run the program and record what variable types are successfully used as method arguments. The main advantage that the API documentation has over looking at the actual code is that it shows a full inheritance tree and lists methods that are inherited from super-classes.   

Another tool that might be useful for Java programmers looking for a friendly, familiar face is [PyDev](http://pydev.sourceforge.net/), a Python plugin for [Eclipse](http://www.eclipse.org/). PyDev does source tree navigation, text completion, method definition lookup, auto-indent, parentheses matching, code search, and automatic, real-time error checking just like what you get when you use Eclipse for Java. I find the error checking especially useful because it shows you immediately if your indents are wrong.  

For debugging a Zope application, I was recently introduced to the Python debugger [PDB](). It is not a visual tool integrated into the your IDE, but if you run Zope in the forground (zopectl fg), and you add the line import pdb;pdb.set\_trace() into your code, you enter an interactive session where you can step through the code, write code statements, and check variable values. Here is some good documentation to help you out: [http://plone.org/documentation/how-to/using\_pdb](http://plone.org/documentation/how-to/using_pdb)  
