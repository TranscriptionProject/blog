+++
date = 2020-12-18T16:44:14Z
description = ""
draft = false
image = "https://images.unsplash.com/photo-1497400338895-940f2d01a6f4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MXwxMTc3M3wwfDF8c2VhcmNofDJ8fGRpZ3xlbnwwfHx8&ixlib=rb-1.2.1&q=80&w=2000"
slug = "your-confusion-is-the-litmus-test"
url = "your-confusion-is-the-litmus-test"
title = "Your confusion is the litmus test"

+++


I was fumbling in the dark. Groping blindly.

It seemed so much simpler a month ago.

"Hey, could you integrate this tool into our service?" my manager had asked. "Sure," I'd replied. "How hard could it be?"

Famous last words.

Now it was my job to take this [convoluted](__GHOST_URL__/blog/the-truth-about-vpc-security-controls/) piece of security infrastructure, which I knew nothing about, which itself was still under active development, and wrangle it into submission.

It's just code, right?

Every step felt like wading through mud. I failed ten different ways trying to get a single piece to work, only to be told about a magic setting I was supposed to have turned on. It wasn't an isolated incident.

I should add that setting to the docs. Did I mention I was effectively beta testing their instructions? All 73 pages of them?

And I was supposed to finish this integration in five weeks. That wasn't long enough!

Because of the time crunch, I'd been trying to minimize the time spent learning, hoping to use that time to actually solve problems.

Except it wasn't working.

I was firefighting, trying to sprint to the end of the marathon.

Burning out.

It was time to switch gears.

To throw away the firefighter's helmet, and don a detective hat.

What principles would serve better?

# 1) **Go deep often, but keep each dig short**

I needed a more wholistic view of how the security tool saw the world.

As we learn, we build a [mental model](https://jamesclear.com/mental-models) of the world, a collection of ideas and impressions about how parts of the world would react in various circumstances. That understanding lets us predict what our tools will do.

Our mental models are never perfect[1], but as we learn we're continually refining them, making accurate, and gradually we're able to apply that knowledge to more domains. It's like trying to drive a van once you've already practiced on a sedan.

Transfer learning, if you will.

It lets us work faster, more accurately, and get more done.

**Every time you go deep into a problem you're making a bet, guessing this expedition will result in a more useful mental model**. **** Each foray down the rabbit hole is like planting a seed which might eventually bear fruit. As always, it's a balancing act:

> "[People] tend to think they can only work on important problems-hence they fail to plant the little acorns which grow into the mighty oak trees.Not that you should merely **work on** random things, but on **small things which seem to you to have the possibility of future growth**." --from [The Art of Doing Science and Engineering](https://amzn.to/2IYkjOS)

The key is to have many digs, which is only possible if you keep each individual foray short.

Go deep, but time box yourself. Don't go too far in.

What's too far? It's hard to know which depths will yield treasure, but [one layer of abstraction deep](https://twitter.com/ZainRzv/status/594036797836951552) tends to work well (if you reach assembly code, you've gone too far).

Each tripe down a rabbit hole is a roll of the dice, and you won't always roll high. But keeping each trip short you leave yourself with time roll that dice over and over again, increasing your chance of rolling that six.

Additional heuristics can help hone your search even further...

# 2) Your confusion is a litmus test

Go deep on the tasks you're actively working on, specifically when you encounter something that feels confusing.

**Confusion means you've reached the limits of your current mental models**. It's no longer helping you predict what something will do. The gaps in your mental model are showing and it's time to dig deeper to plug them up.

Your confusion is a litmus test.

And boy was I confused.

Now, why only go deep into stuff you're actively working on? Because that's a giant sign that this hunt will result in a mental model which is actually useful.

> "[These] studies are surprisingly broadly applicable because, even if you’re learning about the details of some specific system, **that system’s design will contain a juicy core of extractible general principles**. Unlike many “general principles” people try to teach you, the ones you learn [this way] are guaranteed to be important to at least one real-world system (the one you’re learning about). And you’ll see them realized in all their messy detail" --from [In Defense of Blub Studies](https://www.benkuhn.net/blub/)

# 3) There's always a bigger picture

Sometimes you go deep by going broad.

**Everything you do is a local optimization within a larger goal**, one that you might not be aware of.

I was trying to integrate the security tool into our service, but the end goal was to let our customers have a more secure cloud footprint than anyone else offered. My service was just one of many the customer would be enabling this security offering with. I had to see things from the customer's perspective and understand how they would use this feature.

Not knowing that would risk pushing the boulder up the wrong hill.

Expanding your understanding of that broader picture can be especially helpful when you're designing a solution, preventing you from getting stuck at a local maximum.

**The quality of your solution is limited by your understanding of the problem.** Without a broad enough context on the problem your solution might even make the actual problem worse! (*cough* Google logo redesign[2] *cough*)

But when you understand the larger problem, you might realize the guy asking for a faster horse cart would be better served by a car.

[Richard Hamming describes](https://amzn.to/2IYkjOS) how he gradually discovered the larger and larger goals his work contributed to, and how he adjusted what he did accordingly:

> "**There is no single larger picture.** For example, when I first had a computer under my complete control, I thought the goal was to get the maximum number of arithmetic operations done by the machine each day. It took only a little while before I grasped the idea that it was the amount of important computing, not the raw volume, that mattered. Later I realized it was not the computing for the mathematics department, where I was located, but the computing for the research division which was important.Indeed, I soon realized that to get the most value out of the new machines it would be necessary to get the scientists themselves to use the machine directly so they would come to understand the possibilities computers offered for their work and thus produce less actual number crunching, but presumably more of the computing done would be valuable to Bell Telephone Laboratories. Still later I saw I should pay attention to all the needs of the Laboratories, and not just the research department.Then there was AT&T, and outside AT&T the country, the scientific and engineering communities, and indeed the whole world to be considered. Thus I had obligations to myself, to the department, to the division, to the company, to the parent company, to the country, to the world of scientists and engineers, and to everyone. **There was no sharp boundary I could draw and simply ignore everything outside**."

# To Recap

These are three guidelines for when it's worth going deep:

1. **Go deep often, but keep each dig short**. Each exploration is a seed you're planting. Plant many, and some will eventually bear fruit.
2. **Use your confusion as a litmus test**. You've found a gap in your mental model of the world, time to fill it.
3. **There's always a bigger picture**. Go broad, traveling across tangential nodes to understand the problem space better.

I ignored these principles to my own peril. But turning around and digging deeper helped me not only solidify my own understanding of the problem, I later [shared my newfound understanding](__GHOST_URL__/blog/the-truth-about-vpc-security-controls/) with others, helping over hundreds of people both inside and outside Google to understand this highly niche problem.

And yes, the feature shipped on time.

[1] [https://fs.blog/2015/11/map-and-territory](https://fs.blog/2015/11/map-and-territory/)[2] [https://techcrunch.com/2020/10/06/googles-new-logos-are-bad](https://techcrunch.com/2020/10/06/googles-new-logos-are-bad/)

