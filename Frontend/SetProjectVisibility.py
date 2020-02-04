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
def setProjectVisibility(myToken):
    print("")
    print("=====================================")
    print("Set visibility for a Project...")
    print("=====================================")
    print("")

    # TEMP: aosp-4-group
    # project_ID = 5007973
    # aosp-4-group/tools
    # project_ID = 5008464

    project_ID = input("Type in your valid project_ID: ")

    visibilityState = input("Enter desired visibility state (public, private, internal): ")

    #print("project_ID: ", project_ID)
    print("Visibility state: ", visibilityState)

    ##### Fetch all projects with in the Group project_ID
    response = featureLibrary.get_project(project_ID, myToken)
    if response.status_code != 200:
        print(" ERROR: Invalid project_ID, return to main menu")
        return
    json_data = response.text
    json_object = json.loads(json_data)

    print()
    print("GROUP OBJECT SUMMARY:")
    print("     Project id: " + str(json_object['id']), end="\t")
    print(" Full path: " + json_object['path_with_namespace'])

    temp = input("Change Visibility to " + visibilityState + " now? (y/n): ")

    if temp == "y" or temp == "Y":
        response = featureLibrary.set_project_visibility(project_ID, visibilityState, myToken)
        if response.status_code == HTTP_STATUS_SUCCESS:
            print("Update passed")
        else:
            print(" ERROR: Request Failed - Status_code: ", response.status_code)
    else:
        print("Exit without updating")