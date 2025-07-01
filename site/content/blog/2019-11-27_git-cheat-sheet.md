+++
date = 2019-11-27T08:00:00Z
description = ""
draft = false
image = "https://images.unsplash.com/photo-1477949331575-2763034b5fb5?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=2000&fit=max&ixid=eyJhcHBfaWQiOjExNzczfQ"
slug = "git-cheat-sheet"
url = "/blog/git-cheat-sheet"
title = "The Essential Git Cheat Sheet"

+++


Quick cheat sheet of commonly used git commands that I’d otherwise have to keep Googling to remember

# Rebase your branch to the latest master

If your current branch was branched off of master and you want to pull the latest updates pushed to master since then:

```
git pull --rebase origin master

```

# Pull a branch other than the one you're on

For example, if you're not on the master branch but want to pull and merge master

```
git fetch origin master:master

```

# Committing Changes

## Merge changes with last commit

```
git commit --amend --no-edit

```

## Squash commits

To squash the last four commits into one, do the following:

```
git rebase -i HEAD~4

```

or

```
git rebase -i [hash of commit before the one last one you want to squash]

```

In the list that shows up, replace the word “pick” with “squash” or “s” next to all but the oldest commit you’re squashing.

Then, to change the timestamp of the resulting commit:

```
git commit --amend --reset-author --no-edit
```

## Set the date of the last commit to right now

You may want to do this after you’ve squashed some commits

```
git commit --amend --no-edit --date "$(date)"

```

# Editing commits

## Edit a commit in your history

Say you have commits: `A -> B -> HEAD` and you want to edit `B`:

Do:

1. `git rebase -i B~`. note the tilda is important, you want to point to the commit before B
2. In the opened file, go to the commit in the list that you want to edit and change `pick` to `edit`. Save and close the file
3. Make the edits you want, save them, stage them
4. Do `git commit --all --amend --no-edit`. This amends the last commit (`B`)
5. Type `git rebase --continue`

More details at: [https://stackoverflow.com/a/1186549/21539](https://stackoverflow.com/a/1186549/21539)

## Insert a commit in your history

Same as Editing a commit in your history, except for in step 4 do a normal commit, not an `--amend`. This'll add your change as a new commit. Then continue the rebase.

More details at: [https://stackoverflow.com/a/32315197/21539](https://stackoverflow.com/a/32315197/21539)

# Undoing/Reverting Changes

## Discard all local changes to tracked files

```
git reset --hard

```

## Discard all local changes to a single unstaged file

```
git checkout --[file]

```

## Discard changes to all untracked/unstaged files. _This cannot be undone_

```
# first run 'git clean -n' to get a preview of what will be deleted
git clean -f

```

## Discard all local changes

Combine the above to get:

```
git reset --hard
git clean -f 

```

## Revert/Undo an Entire Commit

Note: this leaves the commit in the branch history

```
git revert [commit-id]

```

## Revert/Undo changes to a single file in a commit

This will undo the changes to a single file from the given commit id.

The edited file will be unstaged.

```
git show [commit-id] -- [file] | git apply -R

```

# Set your branch head to the remote branch’s head

Use when you want to discard any local changes and start over from the remote branch state

```
# Replace 'origin/master' with your desired remote branch or 
#   the specific CL you want to set the HEAD to
git reset --hard origin/master 

```

# Pull a new remote branch to your existing repo

For when you want to pull a new branch from your repo origin. You can replace ‘origin’ with your desired remote branch if you’re using something different

```
git checkout --track origin/[branch_name]

```

For more details see [this article](https://stackabuse.com/git-fetch-a-remote-branch/)

# Rebase your branch to a different parent branch

If your current branch was forked from one branch, but you instead want to have you changes applied on top of a different branch

From the branch that you want to rebase run:

`git rebase --onto [desired_parent_branch] [current_parent_branch]`

[More details here](https://medium.com/@gabriellamedas/git-rebase-and-git-rebase-onto-a6a3f83f9cce)

# Changing the Branch HEAD

To change the current branch’s head to a different commit

This can be used as a form of undo to remove commits from the dependency tree

```
git reset --hard [commit-id]
git push -f # This line changes the head on the remote branch as well

```

# Finding SHA ids for old branch heads

`git reflog` lets you see what individual local branches used to point to on your box

# Create a New Branch from Current Branch

```
git checkout -b [newBranchName]

```

And then to push that branch to a remote repository:

```
git push -u origin [newBranchName]

```

# Diffing Changes

Key thing to note is that appending ~ to the end of a commit makes it refer to its parent. Appending ~N instead makes it refer to it’s Nth parent

## Diffing the last commit

```
git diff HEAD~ HEAD

```

## Diffing a specific commit

```
git diff [commitId]~ [commitId] #e.g. git diff f23a4s~ f23a4s

```

## Diffing the last N commits

```
git diff HEAD~N HEAD # e.g diff last 4 commits: git diff HEAD~4 HEAD

```

# Pretty Git Log printout

Add the following to your [git config](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Where-system-global-and-local-Windows-Git-config-files-are-saved) file to enable pretty logs (based on work by [Filipe Kiss](https://coderwall.com/p/euwpig/a-better-git-log))

```
alias.lg=!git lg1
alias.lg1=!git lg1-specific
alias.lg2=!git lg2-specific
alias.lg3=!git lg3-specific
alias.lgs=!git lg1 — simplify-by-decoration
alias.lg1s=!git lg1-specific — all — simplify-by-decoration
alias.lg2s=!git lg2-specific — all — simplify-by-decoration
alias.lg3s=!git lg3-specific — all — simplify-by-decoration
alias.lg1-specific=log — graph — abbrev-commit — decorate — format=format:’%C(bold blue)%h%C(reset) — %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)’
alias.lg2-specific=log — graph — abbrev-commit — decorate — format=format:’%C(bold blue)%h%C(reset) — %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n’’ %C(white)%s%C(reset) %C(dim white)- %an%C(reset)’
alias.lg3-specific=log — graph — abbrev-commit — decorate — format=format:’%C(bold blue)%h%C(reset) — %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(bold cyan)(committed: %cD)%C(reset) %C(auto)%d%C(reset)%n’’ %C(white)%s%C(reset)%n’’ %C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)’

```

With the above in your git config file you can just enter the below to see your history:

```
git lg

```

Or to limit history to just the past N commits:

```
git lg -[# of commits]  # Example: git lg -5

```



