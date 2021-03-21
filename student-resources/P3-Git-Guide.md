# P3 Git Guide

-------------------------------------

<blockquote><i>"I'm working on a group project to build a MERN stack app. How do I contribute via git?"</i> - You, c. 202X</blockquote>

That's a great question. Before contributing to the project, read through these quick and easy steps.  

Key: 

* **remote** = your Github
* **local** = your terminal
* **upstream** = your gitmaster's Github repo

1. On your local: `git checkout -b mybranchname`. The name of the branch should be related to the feature you're working on, e.g. `nav-component` or `route-updates`. 
2. Development time! (Make edits to the code.)
3. Once your feature is finished and ready to commit, commit the changes with `git add -A`, `git commit -m "your message"`
4. Now, push the changes to your remote branch: `git push origin mybranchname`. 
5. On your local (aka terminal), merge the development branch onto main via `git checkout main`, `git merge mybranchname`. 
6. Push this new change to your remote repo via `git push origin main`. 
7. Go on Github and make a pull request. At the top of your `main` branch, Github should say something along the lines of "this branch is 7 commits ahead of gitmastername/project3/main". Click where it says "Pull Request" and make a pull request to your gitmaster. Be sure to include a description of what you accomplished. 
8. Slack your gitmaster and ask them to review/accept your pull request.
9. Once they have accepted the PR, pull the changes to your local via `git pull upstream main`, and then push them to your remote via `git push origin main`. 

This is just one of many ways to organize a group project via git. I have shared this one, since this is the one I used for my project, and students have told me it worked for them. 


