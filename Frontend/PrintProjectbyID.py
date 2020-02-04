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


import requests
import sys
import json

import featureLibrary

from httpStatusCodes import *


##################################################################
# CODE ENTRY POINT START
##################################################################
def printProjectJSON (myToken):
    print()
    print("Print Project JSON Object in human readable form:")
    print()

    project_ID = input("Type in your valid Proect ID: ")
    print("Project_ID: ", project_ID)

    # TEMP: aosp-4-group/sdk
    # project_ID = 11834410

    print("")
    print("=====================================")
    print("Project JSON information below...")
    print("=====================================")

    ##### Fetch all projects with in the Group Group_ID
    response = featureLibrary.get_project(project_ID, myToken)
    json_data = response.text
    json_object = json.loads(json_data)

    #print("**Print raw text**")
    #print(response.text)
    #print()

    if response.status_code == HTTP_STATUS_SUCCESS:
        print("printProjectJSON: Project Valid")

        print()
        print("GROUP OBJECT SUMMARY:")
        print("     Project id: " + str(json_object['id']), end="\t")
        print(" Full path: " + json_object['name_with_namespace'])

        print()
        print("PROJECT OBJECT DETAILS:")

        # PRINTS FORMATTED JSON
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
    else:
        print("printProjectJSON failed. Status = ",response.status_code)


