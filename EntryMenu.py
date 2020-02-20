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

# Imports
import time
import sys

from Frontend.PrintGroupbyID import printGroupJSON
from Frontend.PrintProjectbyID import printProjectJSON
from Frontend.SetGroupVisibility import setGroupVisibility
from Frontend.SetProjectVisibility import setProjectVisibility
from Frontend.NestedPrintAllGroups import nestedGroupsPrint
from Frontend.NestedGroupProjectSetVisibility import nestedGroupSetVisibility
from Frontend.GetUsersInGroup import getUsersInGroup
from Frontend.GetUsersInProject import getUsersInProject
from Frontend.AddRemoveUser import addOrRemoveMember
from Frontend.ChangeUserRole import changeUserRole
from Frontend.GitLabSearch import globalSearch
from Frontend.AdminCreateUsers import adminCreateUsers

# from AddRemoveUser import print_hello

print()
print()

intro_text = """
==========================================================================================
==========================================================================================
Welcome to pyAPI-GitLab Entry Menu.
WHAT YOU WILL NEED:  Prior to going any further make sure to have the following available:
* Your GitLab UserID:
* Any GitLab Project or Group ID's you may need:
* Your Personal Access Token:
* Additional information may be required depending on the selected menu options
==========================================================================================
==========================================================================================
"""
print(intro_text)

print("             ==== Your installed Python version is %s.%s.%s ====" % sys.version_info[:3])
print()


# Get user credentials

privateToken = input("Enter your PRIVATE-TOKEN: ")

#privateToken = "PutMyTokenHere!"

print("PRIVATE-TOKEN = ", privateToken)

#For Test so don't have to type in Token each time.  Comment out when entering token from menu.
#privateToken = "enter-valid-token-here"

entry_Menu = """
================================================================================= 
===== PyAPI-GitLab Selection Menu - Press letter to invoke associated function =====
================================================================================= 
A Print Group JSON          B Print Project JSON    C Set Group Visibility
D Set Project Visibility    E Print Nested Groups   F Set Nested Group Visibility
G Add/Remove User           H Change User Role      I Get Users in a Group
J Get Users in a Project    K Create User Accounts

S Search Projects/Users     U Update Access Token   X Exit    
================================================================================= 
"""

while True:
    print(entry_Menu)
    key = input("Press desired key.... ").lower()

    if key == "a":
        printGroupJSON(privateToken)
    elif key == "b":
        printProjectJSON(privateToken)
    elif key == "c":
        setGroupVisibility(privateToken)
    elif key == "d":
        setProjectVisibility(privateToken)
    elif key == "e":
        nestedGroupsPrint(privateToken)
    elif key == "f":
        nestedGroupSetVisibility(privateToken)
    elif key == "g":
        addOrRemoveMember(privateToken)
    elif key == "h":
        changeUserRole(privateToken)
    elif key == "i":
        getUsersInGroup(privateToken)
    elif key == "j":
        getUsersInProject(privateToken)
    elif key == "k":
        adminCreateUsers(privateToken)
    elif key == "s":
        globalSearch(privateToken)
    elif key == "u":
        print("Current Token Value: ", privateToken)
        print()
        privateToken = input("Enter new PRIVATE-TOKEN: ")
        print("Updated PRIVATE-TOKEN = ", privateToken)
    elif key == "x":
        print("See ya later...", end="\t")
        time.sleep(1)
        break
    else:
        print ("Invalid Key Press, try again")
        time.sleep(1)

print("hasta luego!")


# AddRemoveUser.print_hello()



