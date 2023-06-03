Title: Penetration Rate
Date: 2023-05-25T09:03:22.462995
Modified: 2023-05-25T09:03:22.462995
Category: misc
Tags: Product Management
Slug: 2023/05/penetration-rate
Authors: Seth Gottlieb

A couple of months ago I wrote a post about [Retention Rate](/2023/02/your-first-metric-retention-rate.html) as the first metric to watch when rolling out a new product or feature. High retention rate is strong evidence of your product's utility and usability. Once you have established this value, it's time to drive adoption.

You measure adoption with penetration rate, which is calculated as the number of active users divided by the total number of potential users. Sometimes there is debate around the scope of the potential user base. I advocate for a broader definition. For example, even if you have only launched in one locale, I think that you should calculate penetration rate against worldwide potential customers. This way, when you launch a new locale, your penentration rate goes up and not down. In general, I like metrics that go up when good things happen rather than ones whose dips can be explained by progress in other areas. 

To increase penetration rate, you need to attract new users and keep the ones that you have. You should track both customer acquisition and retention because aggressive customer acquisition can mask churn, which is harmful to your business long term. You don't want to waste resources chasing customers that you can't keep. 

Consider the channels you have to build awareness: release notes, tool tips and [interactive product tours](https://userguiding.com/blog/best-product-tour-software/#), searchable documentation, email, youtube channels... But be aware of the annoyance factor, the more accessible (in your face) the channel, the more disruptive it can be when unwanted. My team at Alexa Audio owns the hints that occur during audio playback. Alexa "by the way" hints can be very annoying so we have strict rules for which ones we allow during the audio experience. The hint must introduce a feature or content that is useful in current context. For example, we might suggest how to make a play queue continuous after the music naturally ends. 

You need to be scientific in how you measure the impact of an experiment. This means randomized tests with control and treatment groups and the ability to compare immediate and long term behavior of both groups. A high conversion rate is not good if those who got the impression wind up using your product less over the following months. 

In addition to building awareness, you need to make sure that the customer's first attempt to use the feature is successful and they experience immediate value. If the feature is not designed for immediate value (like auto-save), show progress toward that value (like showing a last saved time).

Most organizations don't have the analytical capacity to measure and manage penetration rate for every feature in their product. It is best to focus on "high value actions:" features that, when adopted, increase overall engagement with the product and value exchange between you and your customers. There are sophisticated statistical models that can calculate the monetary value of each action but a simpler approach is to segment your user population by overall engagement (such the days in a month that they use the product). Compare the behavior of the top quartile with the bottom quartile and see which features your most active customers love. Then you can build programs to help your less active users discover these features. 
