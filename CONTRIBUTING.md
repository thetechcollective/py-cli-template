# Contributing


## My extension my rules!
### 1: `workon` issues in the GitHub repo for all changes that you workon

You can then start working on existing issues using (using isseu 12 as an example):

```
gh workon --issue 12
```

Or you can create the issue in the process by only providing an issue title:

```
gh workon --title "Need to fix the some issue"
```

You will get a new branch (or reuse existing) commit as mut as you want - Use commit messages that _would make sense, if they should end up in a release message_ 

The `workon` command will also make your issue show up in the downstram GitHub project you have defined in `.gitconfig` in status column "In Progress" (defined in `.gitconfig`)

### 2: `wrapup` the branch 

When you are ready to attempt an entry into `main` you can run

```
gh wrapup
```

It will collapse your branch into just a single commit, and make sure that your commit message includes a keyword that will close the isse when it reaches main.


### 3: `deliver` to the remote

The deliver process is initiated from your IDE by running

```
gh deliver
```

It will create a pull-request — or reuse one if applicable — and move the issue in the downstream GitHub project to a Status named "Delivery Initiated" (defined in `.gitconfig`)

### 4: Accept the pull request
...and you're done

NOTE:
You should do **ONE THING manually**😱[^manual]: In the Command Palette in VC Code search for and select `Python: Select interpreter...`. It's likely that you are presented with several options. You should pick the venv that specifically mentions your workspace in the title.

[^manual]: This is not ideal, but I havn't figured out how to add this specific setting to the configuration - please chip in with suggestions if you know how!

<img src="https://github.com/user-attachments/assets/92391bee-ffe4-473e-b83a-900dcac4cf52" align="right"/>
Now you are good to go - start by going to the testing console and let see that the test discovery runs without any issues.

You should in general pay attention to the the unittests. Run them. And run them again _with coverage_. If you wish to contribute to this product you should at least gurantee that coverage is the same or higher when you push to main (defined in `.coveragerc`).
