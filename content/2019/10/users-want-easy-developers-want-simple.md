Title: Users want easy. Developers want simple.
Date: 2019-10-23T16:03:00.001Z
Modified: 2019-10-28T20:24:28.263Z
Category: misc
Tags: development, usability
Slug: 2019/10/users-want-easy-developers-want-simple
Authors: Seth Gottlieb

One of my favorite tech presentations is [Rich Hickey’s Simple Made Easy](https://www.infoq.com/presentations/Simple-Made-Easy/). The premise of the talk is that simple and easy are not the same thing. In fact, you often sacrifice simplicity in pursuit of easiness. As Rich says, we consider something easy if it is “at hand.” Like the [Staples Easy Button](https://www.staples.com/Staples-Easy-Button/product_606396). Simplicity is something totally different. It is the absence of complexity - lots of moving parts entwined together in intricate ways. If an “easy button” really existed, it would be supported by a complex network of solutions that could take care of any problem.   

  

Rich was talking about programming and how to keep code maintainable. Simple code is easier to understand and extend. But I apply this perspective to lots of things. For example, a bicycle is a simple machine. A quick glance reveals how it works and what every part does. But pedaling up a hill is not easy. A modern car is complex. There is a lot of stuff going on under the hood and nearly all drivers accept that they have no hope of understanding it all.  

  

In building software, I have come to realize that users only value ease. A user wants the features he/she likes “at hand.” In a mature, multi-featured application, UI design is mainly focused on hiding some features to make the frequently used ones stand out. Users don’t want simple. Take away any feature and there will be complaints.   

  

Developers want simple. They want to work with code that is understandable and behaves predictably. They realize that every new feature is supported by hundreds of lines of code that need to be tested with every modification. Much of Rich's talk deals with programming styles that unnecessarily create complexity. But some requirements will force even well designed code to become complex. Ironically, these requirements are often driven by a desire for a "simple and easy" user experience (personalization, natural language inputs, voice control...).  

  

Why does this matter?   

  

If we don't acknowledge that "simple and easy" are in conflict, there will be unmet expectations that lead to friction between stakeholders. Users can become impatient discussing complex details about their "simple feature." Development teams can feel under-appreciated for the effort required to do a "simple thing." The time taken to wrestle with ignored complexity can look like incompetence.  

  

Take, for example, the Google search box. It is easy to use... just type in some text and click the button. But it is anything but simple. There is an [art to constructing effective queries](https://www.lifehack.org/articles/technology/20-tips-use-google-search-efficiently.html) and a whole industry (SEO) dedicated to manipulating what comes back. There is also a set of [features that makes the search box like the command line for the web](https://zapier.com/blog/advanced-google-search-tricks/). I can't tell you how many times I have heard "I just want something simple like Google." Google isn't simple. But it _is_ easy. What makes Google search feel easy is that the core functionality is obvious and it gives useful feedback to help you get what you want. You may not get what you want on the first try, but it is easy to refine your search to hone in on your target. Voice assistants aim for the same level of ease but I find the trial/error loop to be more frustrating. That is probably because the system can return only one response and the feedback loop takes longer.   

  

I know how annoying it can be for someone to pick at language and I am not advocating to constantly correct people on their word choices. But I do think it is important for everyone to understand what they are asking for and what they are giving up when they get it. We can do that by probing into what the user means by "simple." That question is reasonable because both "simple" and "easy" are subjective terms that require elaboration. When we document requirements, we should avoid all subjective language. After all, most of the work to achieve the perception of ease and simplicity is through iteration and refinement. These qualities are not intrinsic to the feature but rather to the sentiment of the user.
