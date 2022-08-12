#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022 Pen-Yuan Hsing
# SPDX-License-Identifier: AGPL-3.0-or-later

#
# Script to read a list of GitHub or Wikifactory URLs from a file, then access
# an instance of `wp2.2_dev` backend to retrieve information about them
#

# Python Standard Library imports
import csv
import os
import string
import sys
import urllib

# External imports
import aiohttp
import asyncio

import requests

#
# Parameterise this run
#

# CSV file containing repository URLs
REPO_LIST_FILE: str = "repo_list.csv"
# Get wp2.2_dev backend API endpoint from environment variable
if (BACKEND_URL := os.environ.get("BACKEND_URL")) is None: 
    raise Exception("Need to set environment variable BACKEND_URL")

# 

request: dict = {
	"repo_urls": [
		"https://github.com/nasa-jpl/open-source-rover"
	], 
	"requested_data": [
		"files_editability", 
		"files_info", 
		"tags",
		"license", 
		"commits_level", 
		"issues_level"
	]
}

query_repo_tree_response: requests.models.Response = requests.post(
        url = BACKEND_URL, 
        headers = {
            "Content-Type": "application/json"
            }, 
        json=request
    )


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.post(
            BACKEND_URL, 
            json=request, 
            headers={"Content-Type": "application/json"}
            ) as response:
            
            print(await response.json())

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            # html = await response.text()
            # print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())