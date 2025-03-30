+++
date = 2020-11-12T17:28:09Z
description = ""
draft = false
image = "https://images.unsplash.com/photo-1586281380117-5a60ae2050cc?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ"
slug = "how-i-started-finishing-more-side-projects"
url = "/blog/how-i-started-finishing-more-side-projects"
summary = "This project was supposed to be easy, why do I keep running into brick walls?!? Ok, how do I work around this one without compromising my vision?"
title = "How to slay a Hydra: Finishing projects"

+++


_Am I fighting a hydra? Every time I work around a problem, two others appear! Just how twisted can time zones be?!?_

_And I thought this project would be easy._

_Take a deep breath...Phew. Alright, how do I work around this issue without compromising my vision too much?_

That was me a few weeks ago.

After seeing [my aunt struggling](__GHOST_URL__/newsletter/newsletter-14/) to convert time zones, I’d taken up the quest to build a site that would make the task easier. I’m always looking for fun side projects to build, and this one seemed like an easy candidate.

I was young and naïve. [Time zones are never easy](__GHOST_URL__/blog/falsehoods-programmers-believe-about-time-zones/)

Here’s the story of how I designed the web app, the hurdles I faced building it, and the principles I used to keep making progress.

# Set clear goals

First I had to know [what I was aiming at](https://twitter.com/ZainRzv/status/1322215554380308480).

I don’t write code for the sake of writing code, there is always some deeper goal. For me, it’s usually about what I expect to learn and capabilities I plan to enable. **Being clear on the goal is key to cutting scope ruthlessly later on**. It lets me see how the plan can be simplified while still offering everything I was after

My goals for this project:

* Enable others to easily share timezone links
* Practice rapid project development and reducing scope by building a feature complete service.
* Build in public
* Have fun

That was _why_ I was building. But _what_ was I going to build in particular?

I wrote it down:

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--3-.png" >}}

I've learned through experience that I tend to only stick with [my side projects for two weeks](__GHOST_URL__/blog/do-more-by-doing-less/). So I had to narrow down the vision to something that fits in that time frame. Anything unlikely to fit in that time frame got listed as a stretch goal. I’ll probably never do them, but writing those ideas down helps relax my brain, reassuring it that the cool features I just thought of aren’t being ignored (i.e., I’m using the [Zeigarnik effect](https://www.psychologistworld.com/memory/zeigarnik-effect-interruptions-memory) to my advantage).

I had my _what_ and my _why_. Now for the _how._

# Focus on the User

I can’t make a good product without looking at it from the user’s point of view. And for this project I had a very specific user in mind:

A person on WhatsApp sending an invitation to their friends to hang out online. They’re not too technically minded, but proficient enough to send a zoom link. And They don’t want to open up another app or website to create a link. That’s a pain to do.

This was the user persona I kept in mind as my target audience.

My solution: Let them be able to simply type out the link from memory.

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--4-.png" >}}

# Designing the Interface

Given that the url was meant to be typed directly into a chat box, how the url would look would be a big part of the design.

The idea was that the person writing the invitation would write the timestamp into the url, and when anyone clicks on it the site would show them that time converted into their own local time

This was going to be _the_ entry point to my app, so it had to be easy to use

You saw my first idea in the screenshot above. It looked perfect. It was short and easy to remember. I was ready to move on to the next step.

Except...

**That was my first idea. What are the chances that my first idea would be the best one?**

Alright, fine. I'd force myself to write down a few more alternatives.

For a couple minutes I stared at a blinking cursor until I thought of another format.  It took another minute to notice a third possibility.

And then something clicked in my brain and the idea floodgates opened. I jotted down each variation that occurred and some thoughts about them:

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--5-.png" >}}

We've come a long way from event.at#2009-05-20/4:22pm/PST seeming perfect!

At this point I realized I actually had three components to plan for: time, date, and time zone.

I could design each of them independently, and mix and match the best options. This gave me a bunch of possible alternatives, and more importantly, highlighted the many ways people might make mistakes while typing the url by hand.

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--6-.png" >}}

Analysis completed, the simplest interface I found was:

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--7-.png" >}}

People would definitely make mistakes with it though, so I planned to add support for all the other date/time formats I’d discovered. But those were filed away under “stretch goals”. For v1, I’d just focus on this one format.

It turns out, great minds think alike. A few days later I would discover [http://mytime.io/,](http://mytime.io/,) which uses the exact same url format.

# Designing: Keep it Simple

Given the two week time constraint, I wanted to **keep things as simple as possible**. Part of that would be to **minimize the amount of new tech I’d have to learn**.

To keep things simple, I decided to use the tools I already knew best and build a static site with a C# backend. Time zones are tricky, but I would look up some time zone conversion library (surely there must be one) and I’d generate static html web pages to show people their local time.

The site would be super simple. I’m no html/css expert, and this wasn’t the time to learn. My site would use whatever default look & feel the Visual Studio project template offered.

No databases involved. No state being saved.

I had a nagging thought in the back of my head though: I should add logging.

Thatwould let me discover all the different ways people might type the urls in practice. Folks might misremember how to write the url, and I could treat the common “mistakes” as if they were valid urls.

I jotted down the "stretch goal" and stopped worrying about it

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--8-.png" >}}

Tech stack chosen, time to start coding.

# Face first into the brick wall

And as I looked for a time zone conversion library I ran face first into [a brick wall of problems](__GHOST_URL__/blog/falsehoods-programmers-believe-about-time-zones/). Turns out different time zones [can have the same abbreviation](__GHOST_URL__/blog/falsehoods-programmers-believe-about-time-zones#misconception-14-every-time-zone-has-its-own-abbreviation) (e.g CST is used for Central Standard Time and for China Standard Time), the correct abbreviation [changes during daylight savings time](__GHOST_URL__/blog/falsehoods-programmers-believe-about-time-zones/#misconception-11-a-country-stays-in-the-same-time-zone-during-daylight-saving-time) (but most folks won’t know that and will enter the wrong time zone), and [there isn’t even always an unambiguous conversion](__GHOST_URL__/blog/falsehoods-programmers-believe-about-time-zones/#misconception-15-there-is-always-an-unambiguous-conversion-from-one-time-zone-to-another) from one time zone to another.

Given this ambiguity, what were my options?

I could hard code which time zones I would favor when the url is ambiguous. CST would always be interpreted as Central Standard Time

I could tweak the tool to auto-fix the time zone, by guessing whether or not DST was intended. This would also require again limiting the countries I support this for (doing it for all countries would likely exceed my 2 week budget)

I could change how the time zone is specified. Instead of specifying a time zone abbreviation, I could ask people to specify the city. Out of the 1000 most populated cities in the world, only 6 have the same name. I’d be limiting who gets to use the app, but still be catering to most of the population. But then I’d need a solution for cities with a space in their name.

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--9-.png" >}}

I chatted with a friend about this and he asked “why not just redirect everyone to Google?”

That...made sense.

Google has already solved this problem, they’ve already built in the right heuristics to guess which time zone you intended when you ask it to convert any time to your local time. By redirecting to them, I could leverage all that for my v1.

Sure, I’m not building a super cool time zone conversion logic, but that wasn’t one of my goals.

Suddenly the problem became very simple. When someone visits my site at [event.at/4pm/CST](https://localtime.azurewebsites.net/4pm/CST), I’d redirect them to Google with the search term “4pm CST”. Google would automatically convert this to their own local time

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--10-.png" >}}

Incidentally, while testing out the google urls I happened upon a site called [http://mytime.io/](http://mytime.io/), which was almost exactly like what I’d originally set out to do, except with slightly better graphics. It’s clearly also a v1 someone built and then didn’t take it further. They ran into the same set of issues that I did.

Now I needed my own domain. So far I had been developing this site at [https://localtime.azurewebsites.net/](https://localtime.azurewebsites.net/). But it needed a short, memorable url to actually be usable. To my disappointment, I soon learned that .at isn’t a TLD I could actually buy (so event.at wasn’t possible), and I quickly discovered that any easy to memorize domain was either already taken or would cost me hundreds of dollars to acquire.

This was a serious road block.

I spent a couple hours going down the rabbit hole of possible domains I could use, to no avail. I could have compromised and gotten a misspelt domain or something, but then I realized **I had already achieved my goals**:

* [http://mytime.io](http://mytime.io) got folks 90% of the functionality I’d envisioned. It was certainly good enough for my own use case, and building my own solution to solve that remaining 10% wasn’t very exciting
* I’d practiced evaluating design and trade offs, which game me most of my desired development practice
* I had plenty of content now to write about and share building-in-public style.
* Learning about time zones was a blast

So..

Mission Accomplished!

{{< figure src="/img/how-i-started-finishing-more-side-projects/pasted-image-0--11-.png" >}}

If you want to play around with what I built, here’s the horribly messy [source code](https://github.com/ZainRizvi/LocalTime) and the [live site](https://localtime.azurewebsites.net/).

# The Principles at Play

A quick recap of the key principles at play here:

* **Be clear about your goals**. They let you know how you can simplify your vision. Once you achieve them, you’re done! No shame in leaving the rest of the planned work.
* **Cut scope ruthlessly**. Be realistic about how long you’ll work on the project and don’t let the scope exceed that
* **Focus on the user**. Keep your target audience in mind, as well as their possible shortcomings. What will it take to give them a great experience?
* **Minimize how much you have to learn**. Lessons will come anyways, minimize the additional things you’ll have to learn as part of cutting scope.
* **You don’t have to cater to everyone**. If you can give one half of people a great experience and the other half nothing, that’s usually better than giving everyone a mediocre experience.

In the past, I would have considered this project a “failure”, thinking that I hadn’t “finished” it.

Heck, I probably wouldn’t have even gotten a working prototype.

But by being clear about what I actually wanted to get out of the work, I not only made faster progress but could also tell when the project was actually completed.

I didn't have to keep hacking away at the hydra's heads, the beast was already slain.

_Want to learn more about how to leverage your own mindset to build better products? Sign up for my weekly [newsletter](__GHOST_URL__/newsletter/) below where I share insights on how to be a better software engineer using principles from psychology._

_Want daily insights? Follow me on [twitter](https://twitter.com/zainrzv)_



