+++
date = 2022-08-22T19:10:53Z
description = ""
draft = false
image = "https://images.unsplash.com/photo-1545987796-b199d6abb1b4?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDU3fHxuZXR3b3JrfGVufDB8fHx8MTY2MTE5NTQwMg&ixlib=rb-1.2.1&q=80&w=2000"
slug = "want-to-make-a-feature-change-to-pytorch"
url = "/blog/want-to-make-a-feature-change-to-pytorch"
summary = "With such a large number of commits coming in, PyTorch needs a process for managing it all to keep the codebase maintainable. For smaller changes, like a five line bug fix, this takes the form of a regular PR review.  For larger changes, we prefer a Request for Comments"
title = "Want to make a feature change to PyTorch?"

+++


This page contains instructions on how to propose and implement feature changes to PyTorch.

Over half the commits made to pytorch every week come from the wider open source community. Sometimes researchers have a certain feature that they want to see implemented, companies have hardware they want to support, or a developer found a bug they really need fixed.

With such a large number of commits coming in, PyTorch needs a process for managing it all to keep the codebase maintainable. For smaller changes, like a five line bug fix, this takes the form of a regular PR review. Make a change, submit a PR, and a core pytorch contributor will review it soon.

But sometimes you’ll want to contribute a larger change, like an enhancement to an existing function or even a brand new feature. Submitting a 1,000 line PR for a feature no one has heard about rarely results in a good experience (for neither the reviewer nor the coder).

For larger changes like this, we have a more indepth process that’s similar in spirit to a design review. It ensures that the feature you’re working on becomes something the core owners are happy to accept and maintain going forward.


The Request for Comments

To propose a new feature, you’ll submit a Request For Comments (RFC). This RFC is basically a design proposal where you can share a detailed description of what change you want to make, why it’s needed, and how you propose to implement it.

It’s easier to make changes while your feature is in the ideation phase vs the PR phase, and this doc gives core maintainers an opportunity to suggest refinements before you start code. For example, they may know of other planned efforts that your work would otherwise collide with, or they may suggest implementation changes that make your feature more broadly usable.


Step 1: Create an RFC

RFCs are located in their own repository.

To create one:

 1. For the https://github.com/pytorch/rfcs repository
 2. Copy the template file RFC-0000-template.md to RFC-00xx-your-feature.md and fill it out with your proposal. The template is a guideline, feel free to add sections as appropriate
 3. You may also have the template simply link to another editor, like a Google Docs file, but please ensure that the document is publicly visible. This can make the template easier to add edit, but commenting doesn’t scale very well, so please use this option with caution.


Step 2: Get Feedback on The RFC

 1. Submit a pull request titled RFC-00xx-your-feature.md
 2. Before your PR is ready for review, give it the draft label.
 3. Once it’s ready for review, remove the draft label and give it the commenting label
 4. File an issue against the https://github.com/pytorch/pytorch repository to review your proposal.
 5. In the description, include a short summary of your feature and a link to your RFC PR
 6. Pytorch Triage review will route your issue to core contributors with the appropriate expertise.
 7. Build consensus. Those core contributors will review your PR and offer feedback. Revise your proposal as needed until everyone agrees on a path forward. (Note: A proposal may get rejected if it comes with unresolvable drawbacks or if it’s against the long term plans of the pytorch maintiners)


Step 3: Implement your Feature

 1. If your RFC PR is accepted, you can merge it into the pytorch/rfcs repository and begin working on the implementation.
 2. When you submit PRs to implement your proposal, remember to link to your RFC to help reviewers catch up on the context.