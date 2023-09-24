Title: Twitter Archive Unboxing
Date: 2023-09-14T17:42:28.183121
Modified: 2023-09-14T17:42:28.183121
Category: misc
Tags: Social Networking
Slug: 2023/09/twitter-archive-unboxing
Authors: Seth Gottlieb

Back in December, [I decided to leave <del>Twitter</del> X](https://www.contenthere.net/2022/11/digital-refactor.html) and direct my social energies elsewhere. Part of my emigration plan was to export my tweets in case I ever wanted to access them. After a few ignored requests, X finally generated an export that I was able to download. This is a summary of my experience.

I was never a prolific tweeter (less than 5,000 posts since 2008) so I was suprized by the size of the archive: 45MB compressed. The zip expands into a directory that contains a local website of all of your twitter activity.  

![archive home](/images/twitter-archive-home.png)

The tweets view allows you to browse, filter, and search your tweets, retweets, and replies. All of the images referenced in your posts are stored locally. That explains why the archive is so big. Clicking on the tweet takes you to the tweet on twitter.com. 

![archive tweets](/images/twitter-archive-tweets.png)

The likes view is my favorite mainly because I tended to ❤️ jokes. The personalization view shows how Twitter interpreted my interests from my activity to build my own personal echo chamber. 

![archive tweets](/images/twitter-archive-likes.png)

Under the hood, the archive stores all of the tweets in a single JSON file (data/tweets.js) that has high potential for harvesting programmatically because it is so nicely structured. For example, I could easily write a script that ranked my tweets by how many times they were retweeted.  

But I probably won't.

While I am impressed by the design and capabilities of the archive, I am disappointed by the utility of having it. Maybe if I was a great comedian, this could be my highlight reel. Most of my tweets, however, were parts of conversations, which are meaningless without the context of the thread. Quoted tweets and retweets also lack context because the original tweet is truncated. The worst problem is that nothing is particularly relevant right now. The moment has passed. The external links have rotted away. For me, the best part was the community and the interaction. And that can't be exported.  

For what it's worth, I have the exact opposite experience with this blog, which I started back in 2004. I regularly go back and read old posts to remind myself of something that I learned or how I thought about a topic. You need more than 140 (or even 280) characters to present an idea that can stand on its own. Because I was writing for a public audience, I made an effort to provide context, think and write clearly, and support my reasoning. Being a decade+ older than I was when I wrote many of these posts, I see that I could be the stranger that I was writing for. 

















 
