#
# Copyright 2019 Don Harbin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import json

import featureLibrary

from httpStatusCodes import *

##################################################################
# CODE ENTRY POINT START
##################################################################
def changeUserRole(myToken):
    print("")
    print("===========================================")
    print("Change a User Role in a Group or Project...")
    print("===========================================")
    print("")

    User_ID = input("Enter valid User_ID: ")

    pg_valid = False
    while pg_valid == False:
        projectORgroup = input("Enter whether want to add to project or group (p/g): ").lower()
        if (projectORgroup == "p") or (projectORgroup == "g"):
            pg_valid = True
        else:
            print(" Entry error: Invalid entry, try again")

    if (projectORgroup == "p"):
        project_ID = input("Enter valid Project_ID: ")
    else:
        group_ID = input("Enter valid Group_ID: ")

    # Get user info
    # Display current role Access Level
    # Set new Role Access Level
    access_level_text = """
    =================================================================
    Valid access levels when adding a Member:
        10 => Guest access
        20 => Reporter access 
        30 => Developer access
        40 => Maintainer access
        50 => Owner access # Only valid for groups
    =================================================================
    """
    print(access_level_text)
    al_valid = False
    while al_valid == False:
        accessLevel = input("Enter desired numerical access level (10/20/30/40/50): ")

        if (accessLevel == "10") or  (accessLevel == "20") or (accessLevel == "30") or (accessLevel == "40") or (accessLevel == "50"):
            al_valid = True
        else:
            print(" Entry error: Invalid access level entered, try again")

    if (projectORgroup == "p"):
        response = featureLibrary.change_user_project_role(User_ID, project_ID, accessLevel, myToken)
    else:
        response = featureLibrary.change_user_group_role(User_ID, group_ID, accessLevel, myToken)

    # 201 == Created succsessfully
    if response.status_code == HTTP_STATUS_ERROR_CREATED:
        print("ERROR: User already exists, must remove or edit vs add...")
    elif (response.status_code == HTTP_STATUS_SUCCESS_CREATED) or (response.status_code == HTTP_STATUS_SUCCESS):
        print("==== PASS - DETAILS: ")
        json_data = response.text
        json_object = json.loads(json_data)

        # PRINTS FORMATTED JSON
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
    elif (response.status_code == HTTP_STATUS_SUCCESS_NOCONTENT):
        print("==== PASS")
    else:
        print(" ERROR: Request Failed - Status_code: ", response.status_code)


