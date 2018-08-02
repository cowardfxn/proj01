# Jenkins-Github automation

## Jenkins configurations

#### General
 - GitHub project git repo address, https or ssh, e.g. `https://github.com/elvis/tranquility.git`

#### Source Code Management
 - Git
  * **Repository URL** URL of git repo, both https and ssh work, e.g. `https://github.com/elvis/tranquility.git`
  * **Credentials**  choose kind *SSH Username with private key*, "github username: private access token" 
  * **Branches to build**  specify which branch to track, default to master. Jenkins will check changes in all branches if left blank
 - Build Triggers
  * **GitHub hook trigger for GITScm polling**  checked
  * **Poll SCM**  checked, leave schedule blank
 - Build
  * Execute shell


## Git configurations
#### User setttings (overall)
#####Generate personal access token  
`Settings > Developer settings > Personal access tokens`  
click "Generate new token"

#### Settings in repository
`Repository page > Settings > Webhooks`  
click "Add webhook"

 - **Payload URL** set "notifyCommit" with personal access token
  * `https://bl-dev-jenkins.pwc.com/jenkins/git/notifyCommit?url=git@github.com:Xeonan/docker-compose-test.git&token=781141a326f5ea1091e9a80e62ccd9a7bafa30e8`
 - **SSL** verification disable
 - **Which events would you like to trigger this webhook?**  choose necessary ones
 - **Active** checked

Webhooks page also shows "Recent Deliveries", allow users to check delivery response and try to redeliver.

