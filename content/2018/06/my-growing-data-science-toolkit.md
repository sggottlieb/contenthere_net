Title: My Growing Data Science Toolkit
Date: 2018-06-20T14:24:00Z
Modified: 2018-06-20T14:24:08.288Z
Category: misc
Tags: data science
Slug: 2018/06/my-growing-data-science-toolkit
Authors: Seth Gottlieb

  

At Aberdeen, I am taking vast amounts of data and working them into a unified data model that encompasses company information, web traffic, survey results, etc.. The actual workflow is nicely summarized in this classic dataists post called “[A Taxonomy of Data Science](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/)”: OSEMN (Obtain, Scrub, Explore, Model, iNterpret).  

  

Here are the tools and tricks that I use on a daily basis.  

  

## Command Line Tools&nbsp;

Massive data files are troublesome for most editing programs (such as Excel or even VIM). It takes too much memory to hold all of that data in an editable state. Command line tools don’t have this problem because they work with data as a stream so they only need to load one line at a time.  

  

Kade Killary wrote an excellent article called “[Command Line &nbsp;Tricks for Data Scientists](https://medium.com/@kadek/command-line-tricks-for-data-scientists-c98e0abe5da)” . The tips range from simple to advanced. On the simple end, I learned about “wc -l” &nbsp;which is the fastest way to get the number of lines in a file. Split is also a simple but powerful command for doing things like breaking up a large file into smaller batches for things like [Mechanical Turk](https://www.mturk.com/) (more on that later).  

  

When working with CSV files (the lingua franca of data science), I couldn’t live without [CSVKit](http://csvkit.readthedocs.io/en/1.0.3/). It doesn’t do anything you can’t do with AWK but the syntax is optimized for working with CSV files and is much simpler. For example, “csvcut -n filename.csv” lists the names of each column in filename.csv. “csvcut -c 1,3,4 filename.csv &gt; newfile.csv” exports columns 1,3, and 4 into a new CSV file called newfile.csv. csvformat is useful for handling delimiters and escapes so that the file can be ingested by other systems.  

  

As an aside, I always work with plain text formats such as CSV because they are more accessible to different tools than binary formats such as Excel.  

  

## Mechanical Turk

Most data scientists throw away data that they can identify as bad. Unfortunately, I don’t have that luxury. For example, if I discover that the URL we have a company is incorrect, I need to fix it because I use domain to link to other data. But what do you do if you have over 100,000 missing or bad URLs? Automation can only take you so far. After a certain point, you need an actual human to do some research. &nbsp;I have found that Mechanical Turk is the fastest way to get help with these manual tasks. Using Mechanical Turk effectively is an art that I am just starting to get proficient with.  

  

## Git

When working with data files, there is a tendency to save copies in various steps in the process so you can compare what has changed, recover from a mistake, or take a different approach. Before long, you get directories full of cryptically named files. Some people have developed good systems for organizing and naming these files but I think the best approach is to use a source control system like GIT. &nbsp; With GIT, you can commit a version of the same file with a comment about what you did with it. And, of course, Git helps you work with others.  

  

## VisualDiffer&nbsp;

While GIT comes with comparison functionality to show the difference between versions, I don’t think it is particularly easy to use. [VisualDiffer](http://visualdiffer.com/)&nbsp;is a cheap and simple tool to show side-by-side comparisons of text files like CSV. More advanced (and expensive) tools like Beyond Compare, Araxis, and DeltaWalker can handle binary formats such as Excel and even merge differences. But I have not found a need for those yet. My most common use case is to see changes that a script or someone else made to a file.  

  

## AWS

I use a lot of AWS tools in my work. S3, DynamoDB, Lambda…. At the bare minimum EC2 is a quick and cheap way to set up a computer that I can execute a long running process on. For example, I have one automated process that goes through hundreds of thousands of records and uses various APIs to gather additional data. The process literally took weeks. Using EC2 and screen sessions is infinitely better than chaining my own workstation to an internet connection and having it run continuously for days.  

  

## Pandas and Jupyter Notebooks

Since I am already a Python programmer, Pandas and Jupyter Notebooks were an obvious choice for exploring and modeling data. I love how you can build a step by step annotated process to assemble and visualize the data.  

  

## PowerBI

At Aberdeen, we add another step onto the end of the OSEMN process: Publish. This is where we use the output of our research to deliver interactive data products to our customers. Those products include embeddable dashboards and alerts that customers can use to make better decisions and seize opportunities. PowerBI is a rapidly improving platform for delivering interactive reports. We have PowerBI experts on staff so I mainly send data for them to turn into customer facing tools.  

  
