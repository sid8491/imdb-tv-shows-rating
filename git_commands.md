# Basic GIT commands

### Initialize a git directory :
* Go to desired directory
* command -> git init (alternativey git init dir_name)

### Sync with github project (most important)
* Go to existing local repo
* command -> git remote add origin git@github.com:username/repo.git
* info of remote repo -> git remote (or git remote -v)
* you can add more remote repo by -> git remote add repo_name repo_address

### Add, commit and push (mostly used)
* Add -> git add -A (will add all the files to local git)
* Commit -> git commit -m "commit message"
* Push -> git push origin master
* Note : git commit -a -m "message" (will add and commit)

### Fetch from remote to local
* git fetch origin (will only fetch, you need to merge manually)
* git pull origin (will fetch & merge)


********** end **********