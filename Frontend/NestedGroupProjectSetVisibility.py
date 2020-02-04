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

##################################################################
# CODE ENTRY POINT START
##################################################################
def nestedGroupSetVisibility(myToken):
    print("=============================================================")
    print("Set visibility of ALL Projects and Subgroups under a Group...")
    print("=============================================================")
    print("")

    group_ID = input("Type in your valid Group_ID: ")
    visibilityState = input("Enter desired visibility state (public, private, internal): ")

    print("Group_ID: ", group_ID)
    print("Visibility state: ", visibilityState)

    # Test aosp-4-group group_ID=500973
    # TEMP: aosp-4-group
    #group_ID = 5007973

    #dbh_TestGroup1
    #group_ID = 4850332

    # Check for valid group_ID
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


    if visibilityState == "private":
        # =========== Set Projects Visibility ==============
        print()
        print("     ===================================")
        print("     ==== SET PROJECT(s) VISIBILITY ====")
        print("     ===================================")
        page = 0

        while True:
            page = page + 1
            print("     GET NEXT PAGE OF PROJECTS: ", page)
            responseProjects = featureLibrary.group_get_all_projects(group_ID, page, myToken)

            json_data = responseProjects.text
            json_object = json.loads(json_data)

            if len(json_object) is 0:
                print("==== NO MORE PAGES")
                break
            else:
                for i in json_object:
                    featureLibrary.set_project_visibility(i['id'], visibilityState, myToken)

    print()
    print("     ===================================")
    print("     ==== SET GROUP(s) VISIBILITY ====")
    print("     ===================================")
    responseGroups = featureLibrary.group_set_nested_visibility(group_ID, visibilityState, myToken)

    # =========== Set Projects Visibility after set groups if going to public ==============
    if visibilityState == "public":
        print()
        print("     ===================================")
        print("     ==== SET PROJECT(s) VISIBILITY ====")
        print("     ===================================")
        page = 0

        while True:
            page = page + 1
            print("     GET NEXT PAGE OF PROJECTS: ", page)
            responseProjects = featureLibrary.group_get_all_projects(group_ID, page, myToken)

            json_data = responseProjects.text
            json_object = json.loads(json_data)

            if len(json_object) is 0:
                print("==== NO MORE PAGES")
                break
            else:
                for i in json_object:
                    featureLibrary.set_project_visibility(i['id'], visibilityState, myToken)

