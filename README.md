# Python GitLab Scripts

This repo contains a series of python scripts designed to interface to gitlab 
using the GitLab API. 

Testing was performed on Python version 3.7. PIP version was 19.3.1.

## What you will need
To use the python scripts or curl examples, here is what you need to have on hand:
- A Personal Access Token: You get that like so the below:


<img src=photos/PersonalAccessToken.gif width=40% height=50% />

**NOTE:** You must save the Personal Access Token somewhere else! Once it disappears from the screen it's gone!


- Your User ID: Note that you must have the correct level of priveledges to use these scripts
- The Project(s) ID(s) or Group(s) ID(s): Unique per project and group

You find these like below:

<img src=photos/GroupProjectUserIDLocations.gif width=40% height=50% />

# Code design
The code is broken into three primary components. 
EntryMenu.py is a primitive menu to use the tool. 
The featureLibrary.py contains all the scripts that interface to GitLab thru it's RESTful enterface. 
Finally, the remainder of the files are separate setup and entry files to call into the featureLibrary.py for each desired function. These files are located in the ./Frontend subdirectory.

# curl examples
This section provides some working examples using curl to interface to github.com in case a person may want a starting point to do  some shell scripting.
Once working in curl, [this helpful site](https://curl.trillworks.com) converts the curl commands to Python requests.

## List Group Members
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5255791/members
```

Sample output:
```
don@donh:~/PycharmProjects$ curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5255791/members
[{"id":3620564,"name":"Don Harbin","username":"dbharbin","state":"active","avatar_url":"https://secure.gravatar.com/avatar/97cd4f46eb78f3c28f7955500e5ee10a?s=80\u0026d=identicon","web_url":"https://gitlab.com/dbharbin","access_level":50,"expires_at":null},{"id":4421968,"name":"Scott Bambrough","username":"sbambrough","state":"active","avatar_url":"https://secure.gravatar.com/avatar/9181a5db4d34d3081a5ef3a79ef36ba4?s=80\u0026d=identicon","web_url":"https://gitlab.com/sbambrough","access_level":40,"expires_at":"2019-11-06"}]don@donh:~/PycharmProjects$
```

**Formatted output, adds subgroups, add pipe to make human readable
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5255791/projects?include_subgroups=true|python -m json.tool
```

Sample output:
```
don@donh:~/PycharmProjects$ curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5255791/projects?include_subgroups=true|python -m json.tool
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  7291  100  7291    0     0  14157      0 --:--:-- --:--:-- --:--:-- 14157
[
    {
        "id": 13839713,
        "description": "",
        "name": "ProjectSGA",
        "name_with_namespace": "c_linaro / AAA Private / SubGroupA / ProjectSGA",
        "path": "projectsga",
        "path_with_namespace": "codelinaro/qualcomm/subgroupa/projectsga",
        "created_at": "2019-08-16T04:58:51.539Z",
        "default_branch": null,
        "tag_list": [],
        "ssh_url_to_repo": "git@gitlab.com:codelinaro/qualcomm/subgroupa/projectsga.git",
        "http_url_to_repo": "https://gitlab.com/codelinaro/qualcomm/subgroupa/projectsga.git",
        "web_url": "https://gitlab.com/codelinaro/qualcomm/subgroupa/projectsga",
        "readme_url": null,
        "avatar_url": null,
        "star_count": 0,
        "forks_count": 0,
        "last_activity_at": "2019-08-16T04:58:51.539Z",
        "namespace": {
            "id": 5858888,
            "name": "SubGroupA",
            "path": "subgroupa",
            "kind": "group",
            "full_path": "codelinaro/qualcomm/subgroupa",
            "parent_id": 5858869,
            "avatar_url": null,
            "web_url": "https://gitlab.com/groups/codelinaro/qualcomm/subgroupa"
        },
        "_links": {
            "self": "https://gitlab.com/api/v4/projects/13839713",
            "issues": "https://gitlab.com/api/v4/projects/13839713/issues",
            "merge_requests": "https://gitlab.com/api/v4/projects/13839713/merge_requests",
            "repo_branches": "https://gitlab.com/api/v4/projects/13839713/repository/branches",
            "labels": "https://gitlab.com/api/v4/projects/13839713/labels",
            "events": "https://gitlab.com/api/v4/projects/13839713/events",
            "members": "https://gitlab.com/api/v4/projects/13839713/members"
        },
        "empty_repo": true,
        "archived": false,
        "visibility": "private",
        "resolve_outdated_diff_discussions": false,
        "container_registry_enabled": true,
        "issues_enabled": true,
        "merge_requests_enabled": true,
        "wiki_enabled": true,
        "jobs_enabled": true,
        "snippets_enabled": true,
        "issues_access_level": "enabled",
        "repository_access_level": "enabled",
        "merge_requests_access_level": "enabled",
        "wiki_access_level": "enabled",
        "builds_access_level": "enabled",
        "snippets_access_level": "enabled",
        "shared_runners_enabled": true,
        "lfs_enabled": true,
        "creator_id": 3620564,
        "import_status": "none",
        "open_issues_count": 0,
        "ci_default_git_depth": 50,
        "public_jobs": true,
        "build_timeout": 3600,
        "auto_cancel_pending_pipelines": "enabled",
        "build_coverage_regex": null,
        "ci_config_path": null,
        "shared_with_groups": [],
        "only_allow_merge_if_pipeline_succeeds": false,
        "request_access_enabled": false,
        "only_allow_merge_if_all_discussions_are_resolved": false,
        "printing_merge_request_link_enabled": true,
        "merge_method": "merge",
        "auto_devops_enabled": false,
        "auto_devops_deploy_strategy": "continuous",
        "approvals_before_merge": 0,
        "mirror": false,
        "external_authorization_classification_label": ""
    },
    {
        "id": 13839583,
        "description": "",
        "name": "ProjectA",
        "name_with_namespace": "c_linaro / AAA Public / ProjectA",
        "path": "projecta",
        "path_with_namespace": "codelinaro/qc-public/projecta",
        "created_at": "2019-08-16T04:38:24.181Z",
        "default_branch": "master",
        "tag_list": [],
        "ssh_url_to_repo": "git@gitlab.com:codelinaro/qc-public/projecta.git",
        "http_url_to_repo": "https://gitlab.com/codelinaro/qc-public/projecta.git",
        "web_url": "https://gitlab.com/codelinaro/qc-public/projecta",
        "readme_url": "https://gitlab.com/codelinaro/qc-public/projecta/blob/master/README.md",
        "avatar_url": null,
        "star_count": 0,
        "forks_count": 0,
        "last_activity_at": "2019-08-16T04:38:24.181Z",
        "namespace": {
            "id": 5858938,
            "name": "AAA Public",
            "path": "qc-public",
            "kind": "group",
            "full_path": "codelinaro/qc-public",
            "parent_id": 5255791,
            "avatar_url": null,
            "web_url": "https://gitlab.com/groups/codelinaro/qc-public"
        },
        "_links": {
            "self": "https://gitlab.com/api/v4/projects/13839583",
            "issues": "https://gitlab.com/api/v4/projects/13839583/issues",
            "merge_requests": "https://gitlab.com/api/v4/projects/13839583/merge_requests",
            "repo_branches": "https://gitlab.com/api/v4/projects/13839583/repository/branches",
            "labels": "https://gitlab.com/api/v4/projects/13839583/labels",
            "events": "https://gitlab.com/api/v4/projects/13839583/events",
            "members": "https://gitlab.com/api/v4/projects/13839583/members"
        },
        "empty_repo": false,
        "archived": false,
        "visibility": "public",
        "resolve_outdated_diff_discussions": false,
        "container_registry_enabled": true,
        "issues_enabled": true,
        "merge_requests_enabled": true,
        "wiki_enabled": true,
        "jobs_enabled": true,
        "snippets_enabled": true,
        "issues_access_level": "enabled",
        "repository_access_level": "enabled",
        "merge_requests_access_level": "enabled",
        "wiki_access_level": "enabled",
        "builds_access_level": "enabled",
        "snippets_access_level": "enabled",
        "shared_runners_enabled": true,
        "lfs_enabled": true,
        "creator_id": 3620564,
        "import_status": "none",
        "open_issues_count": 0,
        "ci_default_git_depth": 50,
        "public_jobs": true,
        "build_timeout": 3600,
        "auto_cancel_pending_pipelines": "enabled",
        "build_coverage_regex": null,
        "ci_config_path": null,
        "shared_with_groups": [],
        "only_allow_merge_if_pipeline_succeeds": false,
        "request_access_enabled": false,
        "only_allow_merge_if_all_discussions_are_resolved": false,
        "printing_merge_request_link_enabled": true,
        "merge_method": "merge",
        "auto_devops_enabled": false,
        "auto_devops_deploy_strategy": "continuous",
        "approvals_before_merge": 0,
        "mirror": false,
        "external_authorization_classification_label": "",
        "packages_enabled": true
    }
]
don@donh:~/PycharmProjects$ 
```

## List Group Members including inherited
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5858938/members/all|python -m json.tool
```

'''
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/6832150/members|python -m json.tool
'''

## List all projects under a group
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/groups/5255791/projects?include_subgroups=true|python -m json.tool
```

## List repo commits for a project
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/projects/dbharbin%2Fopencv-color-tracking-demo/repository/commits|python -m json.tool
```


## List Project notification settings
```
curl --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/ap9705/notification_settings|python -m json.tool
```

## Change Project visibility
```
curl -X PUT -d visibility="public" --header "PRIVATE-TOKEN: replacetextwithyourtoken" https://gitlab.com/api/v4/projects/13839583
```

## Search
The API provides a global search feature.  It can be used to search projects, groups, issues and other items.
The example below is an example of a global search of public projects on the gitlab.com instance and any private projects the curl request initiator has access to for the string "Chattertest".
'''
curl --request GET --header 'PRIVATE-TOKEN: replacetextwithyourtoken' 'https://gitlab.com/api/v4/search?scope=projects&search=Chattertest'|python -m json.tool
'''


# Opens

As these examples have been tested, the following gaps have been found that would be nice to resolve:

### Adding users / Changing roles in inherited projects and groups
It was noticed during testing that if a user in part of a project or groups through inheritance, that an error is returned when attempting to change a user role in the child projects/groups.
I have yet to find a way thru the API to find what the top level (parent) group the user was added to. It's shown in the UI, but still investigating for API.



<end>
