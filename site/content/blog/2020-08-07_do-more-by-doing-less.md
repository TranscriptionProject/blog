+++
date = 2020-08-07T17:03:06Z
description = ""
draft = false
image = "https://images.unsplash.com/photo-1586473219010-2ffc57b0d282?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ"
slug = "do-more-by-doing-less"
url = "/blog/do-more-by-doing-less"
summary = "I didn't want this to become another abandoned project. By trying to do less stuff, I got more done"
title = "I couldn’t abandon another side project"

+++


“That deer is huge!”

I’d been driving home late that night. As I came up to my house, my headlights landed on the biggest deer I had ever seen, right in the middle of the road. I live by some woodlands and neighbors had mentioned deer having free reign in there, but this was the first time I got to see one. This guy didn’t grow that big with proverbial instincts: when my headlights landed on it, Bambi dashed away...straight up my driveway!

Come back!

I chased after it, hoping to prolong my impromptu safari by another second or two, only to see a white tail disappear into the bushes.

That was too short, I wanted to see Bambi again!

I rarely see animals around the house, but they’re definity there. We hear coyotes howling at night and were warned of a bobcat prowling the area. They know how to stay out of sight though, I almost never get to see them in person.

Hmm...could I fix that?

What if I set up a camera to look for the animals and tell me when walked by? I’d get to see them every day! (I'm not going to deny it, I was kinda inspired by the [ninja squirrel obstacle course](https://www.youtube.com/watch?v=hFZFjoX2cGg)).

Time to brainstorm what I’d build:

* A live video feed pointed at the woods.
* Then record video whenever animals walk by. I’ll save it in the cloud!
* I’d need an iPhone app to notify me when an animal is outside.
* Oh, and I can stream the video feed to the app.
* Gotta have AI! I’ll use image recognition to detect which animal is walking by so that I’m only notified when the more unique animals walk by (sorry racoons).
* Finally, some logging to record the time of day each animal showed up. Let’s get scientific

It was totally doable. I was already imagining the day when I’d get an alert on my phone saying “Quick, there’s a deer outside!”

But there was a nagging voice in the back of my head. It whispered: **“You’ll never finish this”**

See, I have a long line of side projects left abandoned by the wayside. “You’ll abandon this one too” the voice kept insisting, “Don’t bother starting.”

I didn’t want to listen to that voice. But it wasn’t lying either.

Now what?

Alright, it’s calling out a real risk. Risk noticed. What can I do to mitigate it and improve my odds? I thought back to my past projects, hoping to find a hint that would let this one have a happy ending.

I found one.

It sounds crazy, but as I thought through all my old projects, I realized the dead projects had something surprising in common: I abandoned them about two weeks after starting. Almost every side project I completed was something I finished in under two weeks. **Two weeks seemed to be when my motivation ran out.**

Huh, that was unexpected.

It kinda made sense though. All of those passion projects were something I did for fun, without a large cause propelling them. I had certainly completed large, multi-month side projects before, but all of them solved some pressing need. But the ones which were just for fun? They were forgotten once the enthusiasm wore off. Which apparently takes two weeks.

Watching deer was definitely a “for fun” project. That meant **I had a deadline**, and not an artificial one. There was an invisible hourglass, and with each passing second my motivation was trickling away.

I had a clock to beat.

{{< figure src="/img/do-more-by-doing-less/pasted_image_0-1-.png" >}}

How do I do that? There’s no way I could build that many features in two weeks.

It was time to do the same thing I do at work: Cut scope mercilessly.

**If I couldn’t complete the project in two weeks, it wasn’t worth attempting**. As much as I was in love with the vision, I had to look at the entire project with this lens. So what gets the axe?

First I had to **be clear about the *real* problem I was trying to solve.**

I wanted to see the animals as they walked by. That required software to notice when they showed up. And something to notify me about it immediately. That’s it. **Everything else was fluff.**

I had to kill the fluff

Saving footage of the deer would be really cool, but nope. Goodbye cloud recording.

Live streaming video to my phone? Never mind.

Logging? Only at the end, if I have time.

Even for the remaining features I tried to keep cutting scope. For every bit of work I’d ask myself: Do I really need to have this? **Is there a simpler way I can achieve the same goal?**

Did I really need to build my own app to tell me about the animal outside? A telegram bot could do that. Great, no need to learn how to build iphone apps.

It was critical to **limit how many new tools I’d have to learn**. Learning one new tool would take a while and eat into the two week window. Learning two new tools would guarantee failure.

Maybe this wasn’t the time to figure out a new machine learning library, I’ll use a motion sensing algorithm instead. When the app detected motion it would take a picture and send it to me. I’d take over the AI’s job and decide if it was interesting.

Sometimes the scope cuts were much more subtle. Some steps which might be best practices at work are unnecessary bloat at home. To know which is which, **think about why** it’s a best practice in the first place.

Should I write tests for the motion sensing code? I had no idea how to test that. Heck, I won’t be maintaining this code after two weeks anyways. Cut. What about a clean, general way to send notifications to people? I’m the only recipient here, so I’ll just hardcode myself into the telegram bot instead.

But the urge to add “useful” features doesn’t go away. There’s even a name for it: scope creep.

It’s the insistent urge that you should add one more thing. “I should make it easier to code this” “What if I do that with a different tool instead?”

{{< figure src="/img/do-more-by-doing-less/one-more-thing.png" >}}

Scope creep happens naturally, and **if I didn’t fight it the timer would run out**.

Time for the coding spree. I found the [right camera](https://www.amazon.com/Raspberry-Pi-Camera-Module-1080P30/dp/B071WP53K7/) on Amazon. Buy. Wrote the motion sensing code, hooked it up to a camera. Done. Wrote a telegram bot. Woohoo! Hooked them up to each other. Boo yeah!

I hit the two week mark, but I was still going strong. I was going to finish this! Calibrating the motion sensor to work outdoors turned out to be trickier than I’d expected but I was making progress...when the last grain of sand trickled out ⏳

Despite my best efforts, a couple days went by when I couldn’t work on the project and suddenly the motivation timer ticked down to zero.  Suddenly pushing it to completion felt like a slog. I didn’t want to continue.

No! I had almost finished it! The project was 95% finished, it just needed a bit more of a push to be complete.

But it just didn’t feel interesting anymore.

There had never been a grand vision driving this thing, I’d started it on a whim. And the motivation was as fleeting as the motive.

A part of me wanted to deny it. “I’ll finish it tomorrow,” I kept thinking. Five tomorrows later I had to accept the truth. It was time to move on and let go of that mental burden. This was a passion project, once the passion wore off it just wasn’t worth slogging through.

But all wasn’t lost. When I started the project I had carefully designed it to really be three distinct projects disguised as one: a motion sensing algorithm, a telegram bot, and an integration project which put it all together. I had completed the first two projects! That would not have happened without me relentlessly cutting scope.

And every project was useful. I’d designed the motion sensor and telegram bot to be independent of the exact application I was developing. Now in any of my future projects I’ll be able to [reuse those components](https://fortelabs.co/blog/create-reusable-components/) if needed, saving me days of work and letting me complete more ambitious projects in that same two week period. I have new tools in my tool belt. That’s still a win!

**By trying to do less stuff, I got more stuff done.**

So I moved on. But now if that niggling voice ever comes back, I’ll be ready.

And if I see Bambi again, I’ll just take a picture.



