#
#Copyright 2019 Don Harbin
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#and associated documentation files (the "Software"), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge, publish, distribute,
#sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or
#substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
#FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#DEALINGS IN THE SOFTWARE.


import requests
import sys
import json

# Set the following BASE_URL to point to the GitLab instance url root.
BASE_URL = "https://gitlab.com/api/v4"

def admin_create_users(token, first_name,last_name,username,email,org,group_creation):
    print("\t\tEntry: admin_create_users()")

    headers = {
        'PRIVATE-TOKEN': token,
    }

    separator = ""
    full_name_string = (separator.join(first_name) + " " + separator.join(last_name))
    print("\t\tFull name: ", full_name_string)

    params = {
        'email': email,
        'username': username,
        'name': full_name_string,
        'org': org,
        'group_creation': group_creation,
        'reset_password': 'true'
    }

    response = requests.post('https://git.poc.itmethods.com/api/v4/users', headers=headers, params=params)

    return response

def set_project_visibility(projectID, visibility, privateToken):
    '''
    Summary: This function will set the GitLab visibility for a project.  Three options - "public" "private" "internal".
    Don't expect "internal" to be used much as it is defined as visibility to anyone logged into gitlab, and we are
    using the gitlab.com (hosted) so that makes "internal" nearly equivalent to "public"

    Prerequisites:
        NewAccountRequest already completed
    
    Parameters:
        projectID:  The ID of the GitLab Project whose visibility is to be updated.
        visibility: String with three options.  "private" "public" "internal".
        privateToken: The privateToken set up in GitLab that allows access to the security level of the requester.

    
    returns: 
        Pass / Fail
    
    '''
    vis = visibility
    pid = projectID
    token = privateToken

    response = get_project(pid, token)
    json_data = response.text
    json_object = json.loads(json_data)
    print("Set ProjectVisibility Entry")
    print("     Group id: " + str(json_object['id']), end="\t")
    print("Full path: " + json_object['name_with_namespace'])

    headers = {
        'PRIVATE-TOKEN': token
    }

    data = {
        'visibility': vis
    }

#   response = requests.put('https://gitlab.com/api/v4/projects/{}'.format(pid), headers=headers, data=data)
    response = requests.put('{}/projects/{}'.format(BASE_URL, pid), headers=headers, data=data)

    return response


def set_group_visibility(group_ID, visibility, privateToken):
    '''
    Summary: This function will set the GitLab visibility for a group or subgroup.  Three options - "public" "private" "internal".
    Don't expect "internal" to be used much as it is defined as visibility to anyone logged into gitlab, and we are
    using the gitlab.com (hosted) so that makes "internal" nearly equivalent to "public"

    Prerequisites:
        NewAccountRequest already completed

    Parameters:
        group_ID :  The ID of the GitLab Group whose visibility is to be updated.
        visibility: String with three options.  "private" "public" "internal".
        privateToken: The privateToken set up in GitLab that allows access to the security level of the requester.


    returns:
        Pass / Fail

    '''
    vis = visibility
    gid = group_ID
    token = privateToken

    response = get_group(gid, token)
    json_data = response.text
    json_object = json.loads(json_data)
    print("Set GroupVisibility Entry")
    print("     Group id: " + str(json_object['id']), end="\t")
    print("Full path: " + json_object['full_path'])

    headers = {
        'PRIVATE-TOKEN': token
    }

    data = {
        'visibility': vis
    }

    response = requests.put('{}/groups/{}'.format(BASE_URL, gid), headers=headers, data=data)
    return response

def group_get_all_projects(Group_ID, page_number, MyToken):
    '''
    Summary: This function fetches the RESTful JSON data structure of all Projects within the Group structure for
    the Group_ID being requested.

    Prerequisites:
        Valid GroupID.

    '''

    gid = Group_ID
    page = page_number
    token = MyToken
    true = "true"

    headers = {
        'PRIVATE-TOKEN': token
    }

    params = (
        ('include_subgroups', true)
    )

#    response = requests.get('https://gitlab.com/api/v4/groups/{}/projects'.format(gid), headers=headers, params=params)
    response = requests.get('{}/groups/{}/projects?include_subgroups=true&page={}'.format(BASE_URL,gid,page), headers=headers)

    return response


def get_project(Project_ID, MyToken):
    '''
    Summary: This function returns the Project Object

    Prerequisites:
        Valid Project_ID

    '''

    pid = Project_ID
    token = MyToken
    true = "true"

    headers = {
        'PRIVATE-TOKEN': token
    }

    params = (
        ('include_subgroups', true)
    )

    #    response = requests.get('https://gitlab.com/api/v4/groups/{}/projects'.format(gid), headers=headers, params=params)
    response = requests.get('{}/projects/{}/'.format(BASE_URL,pid), headers=headers)

    return response


def get_group(Group_ID, MyToken):
    '''
    Summary: This function returns the Group Object

    Prerequisites:
        Valid Group_ID

    '''

    gid = Group_ID
    token = MyToken
    true = "true"

    headers = {
        'PRIVATE-TOKEN': token
    }

    params = (
        ('include_subgroups', true)
    )

    response = requests.get('{}/groups/{}/'.format(BASE_URL,gid), headers=headers)

    return response


def group_get_subgroups(Group_ID, MyToken):
    '''
    Summary: This function fetches the RESTful JSON data structure of all Project within the Group structure for
    the Group_ID being requested.

    Prerequisites:
        Valid GroupID.

    '''

    gid = Group_ID
    token = MyToken
    true = "true"

    headers = {
        'PRIVATE-TOKEN': token
    }

    params = (
        ('include_subgroups', true)
    )

    response = requests.get('{}/groups/{}/subgroups?include_subgroups=true'.format(BASE_URL,gid), headers=headers)

    return response


def group_get_nested_subgroups(Group_ID, MyToken):
    '''
    Summary: This function fetches and prints all subgroups under a group. It only prints the Subgroup ID's and the
    Full Path of the Subgroup.

    Prerequisites:
        Valid GroupID.

    '''

    gid = Group_ID
    token = MyToken
    true = "true"

    print("==== ENTRY: group_get_nested_subgroups ====")

    headers = {
        'PRIVATE-TOKEN': token
    }

    params = (
        ('include_subgroups', true)
    )

    responseGroups = requests.get('{}/groups/{}/subgroups?include_subgroups=true'.format(BASE_URL,gid), headers=headers)

    json_data = responseGroups.text
    json_object = json.loads(json_data)

#    json_formatted_str = json.dumps(json_object, indent=2)
#    print(json_formatted_str)
    if len(json_object) is 0:
        print("==== NO MORE SUBGROUPS")
    else:
        print("==== CURRENT LAYER SUBGROUPS")
        for i in json_object:
            print("     Subgroup id: " + str(i['id']), end="\t")
            print("Full path: " + i['full_path'])


    for i in json_object:
        print("     ++++ CHECK NEXT LAYER")
        print("     Subgroup id: " + str(i['id']), end="\t")
        print("Full path: " + i['full_path'])

        # Recursive call to next sub-layer.
        group_get_nested_subgroups(i['id'], token)

    print("==== EXIT GroupGetNestedSubgroups ====")

    return responseGroups



def group_set_nested_visibility(Group_ID, Visibility, MyToken):
    '''
    Summary: This function sets the visibility of all subgroups under a group.  Note that since GitLab groups do not
    allow "private" groups or projects under private groups this requires a separate algorithm for "private" vs
    "public" groups.  So when setting a tiered group to all private, the algorithm is "bottoms-up" (i.e. must start
    from the lowest projects and subgroups, make them private, and work back up to the top.  When need to set to all
    public, it's then top down.
    Also note that this routine is recursive to work thru all Subgroup branches.

    Prerequisites:
        Valid GroupID.

    '''

    gid = Group_ID
    token = MyToken
    visibility = Visibility
    true = "true"

    print("==== ENTRY: group_set_nested_visibility ====")

    if visibility == "public":
        # Top - Down
        #Set top level Group first
        set_group_visibility(gid, visibility, token)

        #Now complete the rest starting
        headers = {
            'PRIVATE-TOKEN': token
        }

        params = (
            ('include_subgroups', true)
        )

        responseGroups = requests.get('{}/groups/{}/subgroups?include_subgroups=true&per_page=50'.format(BASE_URL,gid), headers=headers)

        json_data = responseGroups.text
        json_object = json.loads(json_data)

    #    json_formatted_str = json.dumps(json_object, indent=2)
    #    print(json_formatted_str)
        '''
        GitLab requires that no subgroups or projects may have a higher security level than the parent group.
        Therefor, for the "public" use case, when converting a large multi-level project with tiered subgroups, 
        the parent groups / subgroups must be made private before the childresn. The following code uses recursion 
        to set the permissions to public from the parent to the children. 
        '''
        if len(json_object) is 0:
            print("==== NO MORE SUBGROUPS")

        else:
            print("==== SET CURRENT LAYER GROUPS VISIBILITY")
            for i in json_object:
                print("     Subgroup id: " + str(i['id']), end="\t")
                print("Full path: " + i['full_path'])
                set_group_visibility(i['id'], visibility, token)
            print("     ++++ CHECK NEXT LAYER")
            for i in json_object:
                print("     Subgroup id: " + str(i['id']), end="\t")
                print("Full path: " + i['full_path'])

                # Recursive call to next sub-layer.
                group_set_nested_visibility(i['id'], visibility, token)

        print("==== EXIT GroupSetNestedSubgroups ====")
    elif visibility == "private":
        # Bottom - up
        # Now complete the rest starting
        headers = {
            'PRIVATE-TOKEN': token
        }

        params = (
            ('include_subgroups', true)
        )

        responseGroups = requests.get('{}/groups/{}/subgroups?include_subgroups=true&per_page=50'.format(BASE_URL,gid), headers=headers)
        json_data = responseGroups.text
        json_object = json.loads(json_data)

        '''
        GitLab requires that no subgroups or projects may have a higher security level than the parent group.
        Therefor, for the "private" use case, when converting a large multi-level project with tiered subgroups, 
        the child subgroups must be made private before the parent. The following code uses recursion to drill 
        down to the lowest level children and then changes permissions starting from the bottom and working it's way 
        back up to the top level parent group. 
        '''
        for i in json_object:
            if len(json_object) is not 0:
                print("==== MORE SUBGROUPS")
                group_set_nested_visibility(i['id'], visibility, token)
            else:
                print("     Subgroup id: " + str(i['id']), end="\t")
                print("Full path: " + i['full_path'])
                set_group_visibility(i['id'], visibility, token)

            # Set top level Group last
        print("==== EXIT GroupSetNestedSubgroups ====")
        set_group_visibility(gid, visibility, token)

    return

def get_users_in_group(group_ID, myToken):
    '''
    Summary: This function displays all users in the Group and child groups

    Prerequisites:
        Valid Group_ID

    '''

    headers = {
        'PRIVATE-TOKEN': myToken
    }

    response = requests.get('{}/groups/{}/members/all'.format(BASE_URL,group_ID), headers=headers)

    json_data = response.text
    json_object = json.loads(json_data)

    # PRINTS FORMATTED JSON
#    json_formatted_str = json.dumps(json_object, indent=2)
#    print(json_formatted_str)

    if len(json_object) is 0:
        print("==== NO SUBGROUPS")
    else:
        print("==== CURRENT MEMBERS")
        for i in json_object:
            print("     username: " + str(i['username']), end="\t")
            print(" | User ID: " + str(i['id']), end="\t")
            print(" | Name: " + str(i['name']))

    return response

def get_users_in_project(project_ID, myToken):
    '''
    Summary: This function displays all users in the Group and child groups

    '''

    headers = {
        'PRIVATE-TOKEN': myToken
    }

    response = requests.get('{}/projects/{}/members/all'.format(BASE_URL,project_ID), headers=headers)

    json_data = response.text
    json_object = json.loads(json_data)

    # PRINTS FORMATTED JSON
#    json_formatted_str = json.dumps(json_object, indent=2)
#    print(json_formatted_str)

    if len(json_object) is 0:
        print("==== NO SUBGROUPS")
    else:
        print("==== CURRENT MEMBERS")
        for i in json_object:
            print("     username: " + str(i['username']), end="\t")
            print(" | User ID: " + str(i['id']), end="\t")
            print(" | Name: " + str(i['name']))

    return response


def add_user_to_project(user_ID, project_ID, accessLevel, myToken):
    print("Entry: add_user_to_project...")
    print(" User_ID: ", user_ID)
    print(" project_ID: ", project_ID)
    print(" accessLevel: ", accessLevel)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
        'access_level': accessLevel
    }

    response = requests.post('{}/projects/{}/members?user_id={}&access_level={}'.format(BASE_URL,project_ID,user_ID,accessLevel), headers=headers)

    return response


def add_user_to_group(user_ID, group_ID, accessLevel, myToken):
    print("Entry: add_user_to_group...")
    print(" User_ID: ", user_ID)
    print(" project_ID: ", group_ID)
    print(" accessLevel: ", accessLevel)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
        'access_level': accessLevel
    }

    response = requests.post('{}/groups/{}/members?user_id={}&access_level={}'.format(BASE_URL,group_ID,user_ID,accessLevel), headers=headers)

    return response

def remove_user_from_project(user_ID, project_ID, myToken):
    print("Entry: remove_user_from_project...")
    print(" User_ID: ", user_ID)
    print(" project_ID: ", project_ID)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
    }

    response = requests.delete('{}/projects/{}/members/{}'.format(BASE_URL,project_ID,user_ID), headers=headers)

    return response

def remove_user_from_group(user_ID, group_ID, myToken):
    print("Entry: remove_user_from_group...")
    print(" User_ID: ", user_ID)
    print(" Group_ID: ", group_ID)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
    }

    response = requests.delete('BASE_URL/groups/{}/members/{}'.format(BASE_URL,group_ID,user_ID), headers=headers)

    return response

def change_user_group_role(user_ID, group_ID, accessLevel, myToken):
    print("Entry: change_user_group_role...")
    print(" User_ID: ", user_ID)
    print(" Group_ID: ", group_ID)
    print(" accessLevel: ", accessLevel)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
        'access_level': accessLevel
    }

    response = requests.put('{}/groups/{}/members/{}?access_level={}'.format(BASE_URL,group_ID,user_ID,accessLevel), headers=headers)

    return response

def change_user_project_role(user_ID, project_ID, accessLevel, myToken):
    print("Entry: change_user_project_role...")
    print(" User_ID: ", user_ID)
    print(" Project_ID: ", project_ID)
    print(" accessLevel: ", accessLevel)

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    data = {
        'user_id': user_ID,
        'access_level': accessLevel
    }

    response = requests.put('{}/projects/{}/members/{}?access_level={}'.format(BASE_URL,project_ID,user_ID,accessLevel), headers=headers)

    return response

def global_search(search_scope,search_string,myToken):
    print("Entry: global_search...")

    headers = {
        'PRIVATE-TOKEN': myToken,
    }

    response = requests.get('{}/search?scope={}&search={}'.format(BASE_URL,search_scope,search_string), headers=headers)

    return response


#User_ID = 3536981
#Group_ID = 4850345
#myToken = "token here"
#headers = {
#    'PRIVATE-TOKEN': myToken,
#}
#response = RemoveUserFromGroup(User_ID, Group_ID, myToken)
##response = requests.delete('https://gitlab.com/api/v4/groups/{}/members/{}'.format(Group_ID, User_ID), headers=headers)

#print("==== PASS - DETAILS: ")
#json_data = response.text
#json_object = json.loads(json_data)

# PRINTS FORMATTED JSON
#json_formatted_str = json.dumps(json_object, indent=2)
#print(json_formatted_str)
