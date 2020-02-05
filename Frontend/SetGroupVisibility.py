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
def setGroupVisibility(myToken):
    print("")
    print("=====================================")
    print("Set visibility for a Group...")
    print("=====================================")
    print("")

    # TEMP: aosp-4-group
    # group_ID = 5007973
    # aosp-4-group/tools
    # group_ID = 5008464

    group_ID = input("Type in your valid Group_ID: ")

    visibilityState = input("Enter desired visibility state (public, private, internal): ")

    #print("Group_ID: ", group_ID)
    print("Visibility state: ", visibilityState)

    ##### Fetch all projects with in the Group Group_ID
    response = featureLibrary.get_group(group_ID, myToken)
    if response.status_code != 200:
        print(" ERROR: Invalid group_ID, return to main menu")
        return
    json_data = response.text
    json_object = json.loads(json_data)

    print()
    print("GROUP OBJECT SUMMARY:")
    print("     Group/Subgroup id: " + str(json_object['id']), end="\t")
    print(" Full path: " + json_object['full_path'])

    temp = input("Change Visibility to " + visibilityState + " now? (y/n): ").lower()

    if temp == "y":
        response = featureLibrary.set_group_visibility(group_ID, visibilityState, myToken)
        if response.status_code == HTTP_STATUS_SUCCESS:
            print("Update passed")
        else:
            print(" ERROR: Request Failed - Status_code: ", response.status_code)
    else:
        print("Exit without updating")
