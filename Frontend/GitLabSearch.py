"""
Copyright 2018 Don Harbin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.


"""

# Imports
import featureLibrary
import json
from httpStatusCodes import *

def globalSearch(myToken):
    print()
    print("=============================================")
    print("     Global Text Search of Projects or Users ")
    print("=============================================")
    print()

    action_valid = False
    while action_valid == False:

        type = input("Search Projects or Users? (p/u): ").lower()
        if (type == "p"):
              action_valid = True
              search_type="projects"
        elif (type == "u"):
              action_valid = True
              search_type="users"
        else:
              print(" Entry error: Invalid entry, try again")

    search_string = input("Enter string to search for: ")


    response = featureLibrary.global_search(search_type,search_string,myToken)


    json_data = response.text
    json_object = json.loads(json_data)

    #print("**Print raw text**")
    #print(response.text)
    #print()

    if response.status_code == HTTP_STATUS_SUCCESS:
        print("globalSearch: Search Valid")

        #print()
        #print("GROUP OBJECT SUMMARY:")
        #print("     Project id: " + str(json_object['id']), end="\t")
        #print(" Full path: " + json_object['name_with_namespace'])

        #print()
        #print("PROJECT OBJECT DETAILS:")

        # PRINTS FORMATTED JSON
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
    else:
        print("globalSearch: failed. Status = ",response.status_code)


