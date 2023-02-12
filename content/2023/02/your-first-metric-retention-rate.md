Title: Your First Metric: Retention Rate
Date: 2023-02-12T11:01:17.427466
Modified: 2023-02-12T11:01:17.427466
Category: misc
Tags: Product Management
Slug: 2023/02/your-first-metric-retention-rate
Authors: Seth Gottlieb

If you invested time and effort to build a ≠new feature on your product, you had at least an informal hypothesis that the new capability would bring value to your customers. But did you actually test that hypothesis by validating the value? Chances are you obsessed over the design, implementation, and delivery of the feature but your attention shifted to the next project once the feature was launched. If you make a habit out of this, your product becomes a bloated jumble of features that your customers can't discover, don't understand, or don't like. You have fallen into the [Feature Debt Trap](https://medium.com/@dlondon4/introducing-feature-debt-the-unconventional-sibling-of-tech-debt-4e046609f53a). The cost of maintaining a product like this is high because of the large surface area for defects and you are vulnerable to disruption by a simpler product that delivers high value by scratching the right itches.

To avoid this fate, or at least slow the onset, you must concentrate your investment on the features that matter the most to your customers and ensure that they are delivering high value. If you look at one metric, start with retention - not for your entire product but for users of the feature. The strongest evidence of a feature delivering value is continued use. Retention means that customers have a recurring need and have found your solution the most convenient way to satisfy it. 

The level of usage regularity one can expect from a feature depends on the feature. For example, your payroll product's W-2 generation function probably just gets used once per year. There are some important features that solve sporadic problems such as password reset. But, for most features, regular usage means high perceived value. 

You measure retention by duration. 2-Week Retention is the percent of customers who continued to use the feature a week after they started to use it. 3-Week Retention is the percent of that group that continued to use it in the 3rd weeks and so on. Retention usually declines over weeks and then stabilizes. The shape of the decline is called a [Survival Curve](https://towardsdatascience.com/survival-analysis-to-understand-customer-retention-e3724f3f7ea2). The longest survivors are getting the most value from the feature. For some features, the time range when the survival curve starts to flatten can be considered the habit formation period - meaning that if someone sticks with something for this long, they continue to use it. For example, a meditation app.  Or the survivor curve could be an asymptote approaching the ideal segment of users. 

If the retention rate is low, your feature or product suffers from one or both of the following issues:

1. Low usability. There are easier ways to solve the problem. 
2. Low utility. The problem that the feature solves isn't a regular priority for the customer. 

You should fix those problems before you invest in promoting the feature or invest in support and maintenance.  

The low utility problem is the harder one to address. It could mean you were undisciplined in managing the product ("wouldn't it be cool if") or didn't understand your customer very well. Or it could be that the customer doesn't understand the value. For example, they may not anticipate the value of having a backup or auto-save. Whatever the root cause, you need to determine whether you can establish value or figure out an exit. Otherwise, the cost of maintaining the feature will be all waste. 

The low usability problem is easier to solve and there are great techniques and skilled people who can help. The only hitch is that you need to plan for the investment. If you are locked into a road map that promises a hit parade of new feature launches, you will need to reset expectations. Nobody wins if your feature launches don't deliver value to your customers. 

If a feature is not fixable, you should eliminate it. But that is hard to do if it has a small group of loyal customers that have relied on this feature to address an important need. To stay out of this situation, give yourself a two way door by leveraging [pilot](https://www.contenthere.net/2007/03/poc-prototype-or-pilot-when-and-why_92.html) or soft launch strategies. Often these approaches are just used to test scaling but they offer a great opportunity to monitor retention. 

Once you have achieved a suitable retention rate, your attention can shift to building adoption (measured by penetration rate) by raising awareness for the feature. But you still need to monitor retention in the form of lapse and churn. But that is for another blog post.  
