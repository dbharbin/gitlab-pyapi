# Python Admin Scripts

This repo contains a number of python scripts designed to interface to gitlab.com back end directly. 

## What you will need
To use the python scripts or curl examples, here is what you need to have on hand:
- A Personal Access Token: You get that like so the below:


<img src=photos/PersonalAccessToken.gif width=40% height=50% />

**NOTE:** You must save the Personal Access Token somewhere else! Once it disappears from the screen it's gone!


- Your User ID: Note that you must have the correct level of priveledges to use these scripts
- The Project(s) ID(s) or Group(s) ID(s): Unique per project and group

You find these like below:

<img src=photos/GroupProjectUserIDLocations.gif width=40% height=50% />



# curl examples
This section provides some working examples using curl to interface to github.com in case a person may want a starting point fto do  some shell scripting.


## List Group Members
```
curl --header "PRIVATE-TOKEN: NL1DJfCAJRs7oEAeduJL" https://gitlab.com/api/v4/groups/5255791/members
```

Sample output:
```
**don@donh:~/PycharmProjects$** curl --header "PRIVATE-TOKEN: NL1DJfCAJRs7oEAeduJL" https://gitlab.com/api/v4/groups/5255791/members
[{"id":3620564,"name":"Don Harbin","username":"dbharbin","state":"active","avatar_url":"https://secure.gravatar.com/avatar/97cd4f46eb78f3c28f7955500e5ee10a?s=80\u0026d=identicon","web_url":"https://gitlab.com/dbharbin","access_level":50,"expires_at":null},{"id":4421968,"name":"Scott Bambrough","username":"sbambrough","state":"active","avatar_url":"https://secure.gravatar.com/avatar/9181a5db4d34d3081a5ef3a79ef36ba4?s=80\u0026d=identicon","web_url":"https://gitlab.com/sbambrough","access_level":40,"expires_at":"2019-11-06"}]don@donh:~/PycharmProjects$
```


