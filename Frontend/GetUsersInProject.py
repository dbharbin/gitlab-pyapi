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
def getUsersInProject(myToken):
    print("")
    print("=====================================")
    print("Show all Users in a Project...")
    print("NOTE: Group / Project Membership is inherited from parents. ")
    print("Therefore ALWAYS start search from the child group/projects!")
    print("=====================================")
    print("")


    project_ID = input("Enter valid Proct ID: ")
    print("project_ID: ", project_ID)

    ##### Check for valid project_ID
    response = featureLibrary.get_project(project_ID, myToken)
    if response.status_code != 200:
        print(" ERROR: Invalid project_ID, return to main menu")
        return
    json_data = response.text
    json_object = json.loads(json_data)

    print()
    print("PROJECT OBJECT SUMMARY:")
    print("     Project id: " + str(json_object['id']), end="\t")
    print(" Full path: " + json_object['path_with_namespace'])


    response = featureLibrary.get_users_in_project(project_ID, myToken)
    if response.status_code != 200:
        print(" ERROR: Request Failed - Status_code: ", response.status_code)
    else:
        print("==== DETAILS: ")
        json_data = response.text
        json_object = json.loads(json_data)

        # PRINTS FORMATTED JSON
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)


