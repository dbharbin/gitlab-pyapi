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
import csv
import string
import requests

import featureLibrary

from httpStatusCodes import *


##################################################################
# CODE ENTRY POINT START
##################################################################
def adminCreateUsers(myToken):

    createUsersIntro="""
    ==========================================================================================
    ==========================================================================================
    Create new accounts from a CSV file...
    ADDITIONAL NOTES:  
    * Prior to going any further make sure to have the following available:
    * The input file must be formatted as follows:
    * - CSV format with one user entry per line,
    * - The fields per line are:
    *        first_name, last_name, username, public email address, organization, can_create_group(true/false)
    * - email addresses must be unique
    * 
    ==========================================================================================
    ==========================================================================================
    """
    print(createUsersIntro)
    
# curl --request POST --header "PRIVATE-TOKEN: Z6ckcsSXeYU4xsDSexbE" "https://git.poc.itmethods.com/api/v4/users?email=arizidon@yahoo.com&password=abc123dorayme&username=testusername&name="Git Crackin"&reset_password=true"

    #source_file = input("Enter the input file name with full path: ")
    source_file = "../../create_users.txt"

    with open(source_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\tadminCreateUsers: Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tAdding {row[0]} {row[1]} with username={row[2]}, email={row[3]}, org={row[4]}, and group creation={row[5]}')
                response = featureLibrary.admin_create_users(myToken, {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]})
                if response.status_code == HTTP_STATUS_SUCCESS_CREATED:
                    print("\t User successfully created")
                elif response.status_code == HTTP_STATUS_ERROR_CONFLICT:
                    print("\tUser creation error. Likely cause - user already exists")
                else:
                    print("\tError creating user. HTTP response = ", response)
                line_count += 1
        print(f'Processed {line_count} lines.')

token="Z6ckcsSXeYU4xsDSexbE"
results=adminCreateUsers(token)


