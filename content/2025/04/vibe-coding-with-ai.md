Title: Vibe coding with AI
Date: 2025-04-23T14:14:23.102439
Modified: 2025-04-23T14:14:23.102439
Category: misc
Tags: AI
Slug: 2025/04/vibe-coding-with-ai
Authors: Seth Gottlieb



After hearing so much about how LLMs are revolutionizing software development, I decided to give it a try. Specifically, I wanted to be able to formulate my own opinions on whether: 

- AI will make software engineers obsolete 
- AI will transform the way software is developed and teams are organized
- AI will unlock new opportunities for non-programmers to experiment
- AI will allow me to overcome my own rust to be a productive programmer

Over the years I have learned that the best way to learn a technology is to "use it in anger." That is,  use it to solve a real world problem. Unlike doing simple "hello world" experiments or running through tutorials, this technique gives you the best chance of running across a technology's rough edges. Plus, you get a useful solution out of it. 

Some of the inspiration for my project came from a [New York Times article about "Vibe Coding](evernote:///view/96464/s2/8b83a401-7c3e-4bb5-a7fe-431f5cd1bfb3/edc0dfb3-76b6-42c2-9234-ce55090e2a7a)" where the reporter described how he used AI to write little personal applications to make his life easier. The problem that I wanted to solve was a natural tendency to fall out of touch with my friends. So I built a little relationship tracker that remembers the last time that I connected with each of my friends. My application synchronizes with a "Relationships" group in my address book and allows me to record when and how I connected with them. Friends that I haven't talked to in a while go from green to yellow to red. It's a simple little application but I use it regularly. 

I went into the exercise with requirements but no AI coding experience. I knew that I wanted to write the back end in Python and host it as AWS Lambda functions. I am a decent (although rusty) Python developer so I felt like I could judge the quality of the backend code. But I wanted the front end to be in ReactJS and React got popular after I stopped doing web front end work. I wanted to try Claude Sonnet 3.7 because people were raving about it. 

My first attempt was to go to the Claude website and request the whole application in one massively detailed prompt. That just gave me some code blocks that I could paste into files. Realizing the absurdity of my plan, I decided to use the [Cursor IDE](https://www.cursor.com/en) and program the old fashioned way: incrementally and iteratively. I started by asking the agent to build out a directory structure for the front end and back end components of my project and started describing backend requirements for synchronization and an API to retrieve them from the application's database. It took a while to figure out how my email/contacts/calendar service represented groups of contacts in their CardDAV API and Claude was very helpful in writing experimental code to interrogate the API. Once *we* figured it out, I was able to coach Claude to optimize the code to minimize API calls. 

Creating the front end was almost effortless. Claude wrote functionally correct code and also made sensible choices on the user interface. The iteration cycle was super fast. If I wanted to experiment with a usability improvement, I just described my idea. Somehow it understood my directives for moving page elements around making them more visible. 

The experience of working with Claude is magical. It reminds me of pair programming with a really good developer. It has all of the collaborative benefits of pair programming (different perspectives, two sets of "eyes," etc.), but without the cost. Sometimes the coding agent does foolish things or forgets a decision. The agent also writes a lot of code so you need to constantly clean out what you don't want to use. But I found myself welcoming opportunities to add value by guiding it. Most of all, I was exhilarated by the satisfaction of being so productive. The time from idea to execution is nearly nothing. Issues melt away as the agent tries different problem solving approaches. It's easy to get into the zone and forget the rest of the world. 

I think that all developers should use a coding agent and, based on what my peers say, many of them already are. AI agents allow developers to iterate and experiment faster and I don't think they will replace them. However, I do think that AI diminishes the value of large offshore teams that offset additional management overhead and collaborative friction (language, time zones, etc.) with wage arbitrage. With an AI agent, a small development team can keep up with a product manager's ideas. AI does the typing so lots of hands on keyboards isn't as useful. 

In addition to coding faster, AI coding agents help developers work across unfamiliar code bases. Somewhere I heard the analogy that maintaining someone else's code is like looking at art through a cardboard paper towel roll. The AI agent slurps up the whole program and understands how it works and where the changes need to be made. It is great for refactoring because it can quickly write unit tests to ensure changes don't break. 

I am also wondering if lowering the cost of writing and maintaining custom code will shift the build vs. buy calculus. Buyers may be more tempted to build exactly what they need rather than compromise on software built for a larger market segment. Incumbent software category leaders may also lose their maturity advantage because a competitor can build critical feature parity so much faster. 

My overall advice to anyone who is not thinking about AI coding is to start thinking about how to use it. Consider guidelines for use and processes for ensuring quality. Think about new opportunities that it unlocks and prior reasoning it invalidates. Whatever you do, don't ignore it. 
