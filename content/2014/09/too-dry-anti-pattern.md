Title: Too Dry Anti-Pattern
Date: 2014-09-22T16:18:00Z
Modified: 2015-01-06T12:30:25.520Z
Category: misc
Tags: development
Slug: 2014/09/too-dry-anti-pattern
Authors: Seth Gottlieb

I do a lot of code reviews. On average, I probably spend an hour a day looking at diffs. I find this an efficient use of time because I frequently spot bugs that wouldn't be revealed by regular testing. I can also prevent implementations that will create obstacles as we progress through the road map.

  

One of the [anti-patterns](http://en.wikipedia.org/wiki/Anti-pattern) that I have started to notice is what I call the "Too DRY Anti-Pattern." For the uninitiated, DRY stands for "Don't Repeat Yourself". It is a primary tenet in one of my favorite books: [The Pragmatic Programmer: From Journeyman to Master](http://www.amazon.com/gp/product/020161622X/ref=as_li_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=020161622X&amp;linkCode=as2&amp;tag=contenthere-20&amp;linkId=EEQKRFOE4EFAJXKX)

<img alt="" border="0" height="1" src="http://ir-na.amazon-adsystem.com/e/ir?t=contenthere-20&amp;l=as2&amp;o=1&amp;a=020161622X" style="border:none !important; margin:0px !important;" width="1"/>

. Keeping your code DRY means using methods and functions rather than copying and pasting code and not storing the same information in multiple places. I have written about [DRY in terms of content management](http://contenthere.net/2010/07/keeping-your-content-dry.html) in this blog before.

  

The Too DRY anti-pattern starts with the good intention of keeping the code DRY. The developer creates a function or method to avoid having the same code exist in lots of places. However, over time the developer starts to use that function in places that do not quite fit. The function gets more parameters and has increasingly complex internal logic to control its behavior in different cases. Too DRY functions are easy to spot. They have lots of intricate if-then logic that try to address a wide diversity of usage.

  

A counter-weight to the Too DRY anti-pattern is the [Unix philosophy of doing "one thing and doing it well."](http://en.wikipedia.org/wiki/Unix_philosophy) When you run into a Too DRY function, use the Unix "one thing" philosophy to break it down. Perhaps create smaller functions that do specific elements of the larger Too Dry function and then have different functions that use those building blocks in different ways. Also, repeating code isn't always a bad thing if the code is small and performs a discrete function. For example, if you have some code that creates an object and sets its properties, it is OK to have similar instances of this logic if the properties need to be set to different values.

  

Like all things, best practices need to be applied thoughtfully rather than as rigid rules. So keep your code DRY, but not at the expense of simplicity.
