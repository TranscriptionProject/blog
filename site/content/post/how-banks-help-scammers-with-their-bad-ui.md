+++
date = 2020-09-30T16:41:48Z
description = ""
draft = false
image = "__GHOST_URL__/content/images/2020/09/Fake-it-image-1-.jpg"
slug = "how-banks-help-scammers-with-their-bad-ui"
url = "how-banks-help-scammers-with-their-bad-ui"
summary = "My sister wanted a summer job before starting college. Instead she was scammed out of thousands"
title = "How banks help scammers with their bad UI"

+++


My sister Sana just wanted to earn some money before returning to college. She was looking for a covid-friendly job on craigslist, something to cut down on the student loans she'd have to take out for the year. After searching and scrounging, Sana found someone who needed logistical help taking care of their pets. She applied and was excited to get hired.

First, they needed help buying pet food. They had ordered $1,800 worth of pet food (they bought high quality stuff in bulk apparently) but the seller would only accept payments via Zelle. Her employer was a bit old fashioned and didn't know how to use that service, so they offered a different arrangement: “I’ll mail you a check for $2,000” they said, “please deposit it in your own bank account, and then use $1,800 of it to Zelle the payment to the sellers. The remaining $200 is your fee.”

Sana was a bit suspicious, but she deposited the check into her Chase bank account and it cleared a few days later. Chase’s site showed that the money had been deposited successfully and was available to use, no strings attached.

Seemed like it was legit. So she did the honest thing and Zelle'd the money  to the seller.

Happy with the job well done, her "employer" sent her another $2,000 check to deposit and transfer. This person really liked their pets. The same process happened again, and her employer was happy with the job well done.

Two weeks later, Sana’s debit card stopped working. Confused, she checked her account to see what was wrong.

Her heart sank.

Chase showed it as overdrawn.

By more than three thousand dollars.

The checks had bounced, two weeks after Chase’s site had indicated they had “cleared”. Before this whole thing had started, Sana had $300 in her bank account. Now she had negative $3,300.

She had just been scammed out of $3,600.

## What happened?

Turns out checks can bounce weeks after they're deposited. It can take that long for the bank to verify they’re legitimate.

Why does it take so long? Here’s a peek behind the scenes:

1. You deposit your check, and it shows up as pending in your account.
2. Your bank sends the check to the check-writer’s bank to request the funds.
3. Their bank verifies if the check is legitimate and the account actually contains the funds. At small or international banks this step is often manual and could take _weeks_.
4. Their bank lets your bank know it's legit. That's when the check has "cleared".

{{< figure src="__GHOST_URL__/content/images/2020/10/Check-lifecycle-large.jpeg" caption="The life cycle of a check" >}}

I skipped one step though:

It take can than more than **six months** for a check to clear, but banks remove that “pending” status just a couple days after it's deposited and allow people to spend the money. This might sound a bit iffy, but it's actually a good thing. Most checks are legitimate and people might need the money quickly. But that assumption breaks down with fraudulent checks.

By removing the “pending” status before fully verifying the check’s legitimacy, Chase gave the illusion that the check had already cleared. _This is what the scammers count on._ 

Today there is _no way_ for a Chase customer to be sure that a check has fully cleared. But unless you have the inside scoop on how banks work, or a finely honed sense of when someone is trying to swindle you, you won’t catch it.

When Sana called up Chase, the bank heard her out. But instead of stopping the scammers, their only concern was making sure she pays up the remaining $3,000 that they claimed she owed them.

_Edit: Chase customer support had one clarification to make. I'd originally said it might take weeks for the check to clear, but they explained it could actually take more than six months. And you'll have no idea when that magic moment occurs._

<img src="__GHOST_URL__/content/images/2020/10/IMG_1399.jpg" class="kg-image" alt="" srcset="__GHOST_URL__/content/images/size/w600/2020/10/IMG_1399.jpg 600w, __GHOST_URL__/content/images/2020/10/IMG_1399.jpg 828w" sizes="(min-width: 525px) 525px" style="display:block;margin:auto">
<br/>

## And she's not the only one who's been hit by this scam.

My friend David Vargas was caught by [pretty much the exact same scam](https://davidvargas.me/blog/i-got-scammed-out-of-5k/). He was sent checks which included his fee and payment that was supposed to be made to someone else. And they only accepted Zelle.

In fact, similar [scams](https://techcrunch.com/2018/02/16/zelle-users-are-finding-out-the-hard-way-theres-no-fraud-protection/?guccounter=1&guce_referrer=aHR0cHM6Ly9uZXdzLnljb21iaW5hdG9yLmNvbS8&guce_referrer_sig=AQAAAEVQ_LYXhqL8UBL2vmnP9kphsW_QtokZbglthvs6MgR-ZvqTSF7pcgQMl05VmPjal00O9pBtatU8paO6pmmAYyt91oRIxVEX7L32zEu7v3WKlKOYDV-RVDEHjYe3Co_ugzyWZPRq3oFD-D2giDL1H-Dvj7jmdSbg6NLoAjBnnyWt)  [have](https://news.cardnotpresent.com/news/zelle-scam-emerging)  [been](https://chicago.cbslocal.com/2019/11/19/how-to-avoid-zelle-scams-and-fraud/)  [going on](https://medium.com/@eirurueta/i-was-scammed-by-using-zelle-for-ethereum-crypto-online-2fa3a38d1817)  [for years](https://www.wsj.com/articles/you-accidentally-venmoed-149-to-a-stranger-good-luck-getting-it-back-1531411133), yet most banks don’t seem to care as long as they're not the ones losing money.

## What should Chase have done here?

### #1 Take responsibility: their system is broken

Is Chase bank directly responsible for scamming people? Of course not. Did they create an environment where scammers could thrive? Absolutely.

The harm was unintentional, but they played a hand in it.

Involuntary manslaughter.

What have other companies done when someone abused their products to deliberately cause harm? They took responsibility for it and fixed the problem at a systematic level.

**The Tylenol murders:** In 1982, someone started [spiking bottles of Tylenol](https://www.pbs.org/newshour/health/tylenol-murders-1982) with poison, killing seven people. This was clearly not Tylenol’s fault, but they still immediately paid to recalled all bottles in the stores, offered anyone who had already purchased the pills free replacements. They took it a step further and **developed tamper-proof packaging** to prevent anyone from contaminating the medicine again in the future.

**Credit Card fraud services**: Online payments are inherently risky. Credit card companies know this, and they’ve committed to helping their customers when the inevitable fraud occurs. If you pay someone with your Discover card and the product turns out to be a scam, _Discover will accept responsibility and refund you the money_, taking a loss if necessary. This dynamic keeps Discover on their toes working to prevent scams before they even happen.

### #2 How should they fix it?

Make the status of the deposited check abundantly clear. This is how Chase can tamper-proof their bottles.

If a check has been deposited but not fully cleared, if it hasn't had the actual funds transferred over to the bank, then Chase needs to make that fact clear to customers! This missing piece of UX is what scammers depend on. That’s the systemic flaw here.

If the bank actually made the status of the funds clear to its customers, then it would have a much stronger leg to stand on when claiming innocence.

But as things stand right now, the only way a person could know the check was still at risk is if they already knew about the long clearing time and how banks hide it. Before the results come back from the external bank, Chase itself doesn’t know if the check is valid. Yet they offer customers no hint of that uncertainty.

And instead of taking responsibility, what did Chase actually do?

### Chase took option #3: Shakedown their customers

{{< figure src="__GHOST_URL__/content/images/2020/09/Ya340FffaeszEwIQ0ZPdxC9WQbRbN4kGKmcgTWiXLUiifzyqYvwzQSr4nwR3-jR--TS_Z-WrSDyVCcx4G37knBt171ds1zqYgfJ9hB4m-rUHKsDrCMG_N_2u6uTVCOreTRlc32iw.png" >}}

Chase acted like the mafia, shaking down whoever they could to get their money back.

My sister had created this bank account back when she was in high school. For minors, Chase requires a guarantor, someone who would make sure her debts are paid. My dad had listed himself, he was also a Chase customer.

And now Chase came after him for the remaining three grand.

He spent hours on the phone with Chase’s customer support trying to get the scam resolved. The reps may have been empathetic, they weren’t empowered to help.

From the bank's perspective, the money they had already pulled from Sana's account was theirs. Sorry, no negotiation possible. The computer won't let us. And Chase did their darned best to not have to take a hair cut on the rest of the amount they enabled scammers to steal.

The most those reps could share was to suggest my dad could try not paying the remaining three thousand and wait until the debt goes to collections. And then pray that the collections department has more leniency. It might hurt his credit rating though, they warned. How much? They didn’t know.  The account was scheduled to go to collections at the end of September.

But a month before that date, my dad noticed his own account was now three thousand dollars lighter. Chase had just helped itself to those funds without warning.

And now that Chase is no longer losing money on this scam, customer support tells him “Sorry, there’s nothing we can do.”

With every step Chase made sure it got paid, one way or another. Vito Corleone would be proud.

{{< figure src="__GHOST_URL__/content/images/2020/09/image-3-1.png" >}}

And if the bank has no skin in the game, why worry about fixing some misleading UI? They seem to think people don’t bother switching banks, and that it can treat its customers as captive users.

## How widespread must this be?

When a person gets scammed they’re usually hesitant to speak up about it.

They're ashamed of having been duped, afraid of being scorned for their foolishness, and so their story rarely gets told.

Yet I know two people who’ve admitted to being hurt by this scam. What does that imply about the scale of this problem?

And Chase allows it to continue happening, punishing their customers for not having intimate knowledge of how banking works.

## Is your blood boiling yet?

I get furious every time I think about it. David Vargas tried to pass his situation off as his own fault, but I was outraged on his behalf.

I want everyone at Chase to see this story. I want every other bank that’s enabling scammers to see this. And I want them to fix their system to let people know when shady checks have not yet been deposited.

When I showed this article to a friend, he got restless, he wanted to take action. “How can I help?” he asked, “Tell me what to do!” At the time I wasn’t sure what could be done, but there is one thing:

**My ask to you:** Can you help spread the word and make Chase notice this problem? Maybe the internet outrage machine can turn this into a priority and protect the thousands of other people who are being scammed by this.

You could share this article ([retweet the Tweet](https://twitter.com/ZainRzv/status/1311701855148236800), or post on FB, Reddit, HN, whatever your usual channels are). Get this shared widely. And maybe, just maybe, some executive at Chase will notice and take the lead in transforming the banking industry. My sincerest thank you to everyone who helps.

So far, Chase hasn’t been interested in accepting an ounce of responsibility for their part in this scheme. Why bother fixing the system when you can just pull money from your customer’s bank accounts? But maybe they can change. Who wants to be known as an unwitting accomplice to scammers?

And even if they don't change, remember Chase's missteps and apply those lessons to your own products. Look for how your problems could be fixed at a systemic level.

As for Sana, she won’t be using Chase anymore.

They don’t tamper proof their bottles.

_Chase doesn't seem to get get how people work. It's like they haven't heard of psychology! The most successful products managed to leverage psychology with their engineering efforts, and others can do the same. You can subscribe below to get it in your inbox, and I'll also be sharing any updates on what happens with Chase_

_Don't like newsletters? I share the same stuff on [twitter](https://twitter.com/zainrzv)_

