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

#### Misc commands:

        git remote -v

