+++
date = 2021-03-19T00:23:10Z
description = ""
draft = true
slug = "untitled"
url = "untitled"
title = "(Untitled)"

+++


stes

sdfs



"Zain, they want us to build them a  unofficial API"

> "What?!? But the service isn't ready yet. We'd have to hack something up that'll
become pure technical debt."
 * "I know, but unfortunately we have no choice."
 * Back in my Google days, we were building a brand new cloud service: AI
   Platform Notebooks. My manager at the time had the insight to find a couple
   large enterprise customers to be our early beta users. They would give us
   rapid feedback on our product, and we'd make sure to address all their
   critical use cases. This rapid feedback loop let us discover product
   shortcomings that only end users could find.
 * It was a great partnership, until they asked us to build technical debt.
 * "Look, if we build it, we're going to have to support this hacky API for
   months (or even longer)! That'll be a huge drain on our small team. Can't
   they wait until we release our official API in six months?"
 * "They can't start integrating until they have this API. So, no."
 * Why didn't our notebooks already have an API? To get the product out the door
   fast, we had built them on top of GCP Compute Engine (bare VMs) and designed
   it to be usable via those VM's api. It was just required some more arcane
   commands.
 * Apparently our enterprise customers wanted something more, but it wasn't
   clear why.
 * The next time we had our sync with those customers, I was on the call as
   well.
 * "Hey folks, I understand you want us to build you an API. Would you mind
   explaining why you need it?"
 * They started sharing their integration challenges, the limitations of our
   VM-based api, and the specific functionality they wanted unlocked. As they
   listed all of their use cases a thought entered my mind.
 * "So, if we send you a google doc containing instructions explaining how to
   achieve each of your use cases with the existing GCP api, would that be good
   enough for you folks?"
 * "Yeah, that would be great!"