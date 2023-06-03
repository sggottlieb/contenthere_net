Title: Decisions
Date: 2023-04-28T11:53:43.911557
Modified: 2023-04-28T11:53:43.911557
Category: misc
Tags: Product Management
Slug: 2023/04/decisions
Authors: Seth Gottlieb

Decisions, regardless of whether they are right or wrong, are critical for moving an organization forward. Organizations that can't make decisions waste time rehashing the same discussions and eventually wind up going with whatever option was the default. A well managed decision, even if it leads to the wrong option, has value because it draws attention to an issue, allows the organization to act intentionally, and creates an opportunity to learn from the selected course of action to course correct. It's better to make a decision that you can pivot from than to cower in indecision. At Amazon, that's the ["Bias for Action" Leadership principle](https://www.amazon.jobs/content/en/our-workplace/leadership-principles). 

To get better at making decisions, organizations should use every decision as an opportunity to improve their process. Once you are aware of the necessity of a decision, I recommend you start your road to improvement by asking the following questions. 

## 1. What decisions do we need to make to move forward?

A decision is only necessary if not making it stops progress. As long as it doesn't slow you down, deferring a decision allows you to make a more informed decision in the future. But be aware of of decisions you are unconsciously making by over-linear thinking that ignores options -- especially those that are hard to reverse. 

## 2. Whose decision is it?

A decision should be made by someone who is accountable for the short and long term success of the impacted component, system, or experience. That person should own all of the relevant dimensions: cost, time to market, usability, viability, etc. The decision maker is also responsible for deciding who needs to be consulted or informed and manage that communication. If someone finds out about a decision and has the authority to question or reverse it after the fact, that's on the decision maker. So the first thing to do is understand the blast radius of the decision. A smaller internal technical design choice could be made by the person maintaining the code. If it has larger implications, the decision maker needs to have a broader scope of accountability.  

## 3. What information is needed to have reasonable confidence?

You will never have complete information about all the implications of all of the potential options. If you did, the choice would be too obvious to even consider it a decision. The threshold for the level of confidence depends on the reversibility of the decision. If reversing a decision has no cost, you might as well just start trying options. But that is never the case because just trying something has the cost of time. The decision maker should be able to articulate up front what data they would need to reduce risk to an acceptable level. Examples include a technical proof of concept demonstrating feasibility, user research using prototypes, a well designed survey with a large enough sample size to achieve statistical significance, revenue or cost projections. Be aware that sometimes the cost of gathering this information outweighs the risk of the decision itself.

## 4. How will you validate whether you made the right decision?

Decisions shouldn't be fire and forget. Your plan to implement the decision should include instrumentation, monitoring, and attention to the results. Ideally, you should think of thresholds when you should reconsider your choice. For example, if we see a retention rate of less than Y, we will pivot to a different choice. Or time could be part of your threshold. For example, we will run this experiment for 4 weeks and then look at the data. Good decisions should preserve the opportunity to change course. But you need to know when to consider those other options. 
