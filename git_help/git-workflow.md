#### Usual workflow:

* Fork a repo using github

* Clone the repo locally

        git clone https://github.com/vijayvikrant/netplugin.git

* Set the upstream 

        git remote add upstream https://github.com/contiv/netplugin.git

* Creating a new branch specific to the changes planned

        git checkout -b my_new_branch

* Make the changes to this branch

        git add .
        git commit -m "changed branch code"

* Push the changes to origin (not upstream yet - that needs to be using a pull request)

        git push origin my_new_branch


* Now go to github and raise a pull request for this branch


#### Deleting a git branch
* Local delete

    `git branch -D branchname`
* Remote delete

    `git push origin :branchname`

#### Diff commands
* Basic diff

    `git diff`
* Diff current working directory and the most recent commit

    `git diff HEAD`
* Using a external diff tool

    `git difftool`
* Diff between the index and most recent commit

    `git diff --cached`
* Diff between the last commit and the most recent commit

    `git diff HEAD HEAD^`
* Diff between the last commit and 3 commits prior to it.

    `git diff HEAD HEAD^^^`

#### Retrigger ci using a dummy push

    git commit -s --amend -m "commit msg"
    git push remote branch -f


#### Git stash
* Stashes the changes so that we can work on something else and restore the
    changes back at a later time.

        git stash save "saving changes for later"

        // list the stash
        git stash list

        // applying the changes that were stashed

        // this will apply the changes but will not remove changes in stash
        git stash apply stash@{0}

        // takes the first change from the stashes, applies it and removes it from the stash 
        git stash pop

        // drop the stash 
        git statsh drop stash@{0}

#### Git rebase
* Make all the changes that are done on a feature branch on another branch.

        // checkout the branch and make your changes
        git checkout feature_branch

        // this will port all your changes over the master branch
        git rebase master

        // post this you will have all your changes over the master branch
        // all your sha would change

#### Misc commands:

        git remote -v

