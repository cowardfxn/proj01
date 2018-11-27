# Git commands

## git tag

Annotated tag
`git tag -a "tag name" -m "tagging message"`

The annotated tag is stored as full objects in Git database, checksumed, contain the tagger name, email and date, having a tagging message

Lightweighted tag
`git tag "tag name"`

Just a pointer to certain commit

#### Showing tag infos
 * `git tag`  show all tags of current project
 * `git tag -l "pattern"` show specific tags
 * `git show "tag name"`  show tag infos, works to annotated tags and lightweighted tags

#### Uploading local tags
 * `git tag -a "commit checksum"`  add tag to specific commit

The `git push` command doesn't transfer local tags to remote server by default.

##### git push tag
 * `git push origin "tag name"`  push specific local tag to remote server
 * `git push origin --tags`  push all local tags to remote server
 * `git tag -d "tag name"` delete local tag
 * `git push <remote> :refs/tags/<tagname>`  delete tag from remote server after deleting locally
 * `git checkout "tagname"`  view the code the tag is pointing to, it's slightly different from branching
