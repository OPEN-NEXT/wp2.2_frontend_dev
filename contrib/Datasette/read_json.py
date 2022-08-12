#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022 Pen-Yuan Hsing
# SPDX-License-Identifier: AGPL-3.0-or-later

# Try to read in JSON from wp2.2_dev backend into an SQLite database to be 
# served by Datasette. Per: 
# https://gist.github.com/simonw/eb5ad8e55d75bbc3003dd9e5d6eb438b

# Python Standard Library
import json
import sqlite3

# External libraries
# import flatten_json
import pandas as pd

# Read saved data
with open("./contrib/GitHub_repos_data.json") as json_file: 
    json_data = json.load(json_file)

# Initialise Pandas DataFrames to hold loaded data

repositories_df: pd.DataFrame = pd.DataFrame() # Repository URL and platform
files_editability_df: pd.DataFrame = pd.DataFrame() # 
files_info_df: pd.DataFrame = pd.DataFrame()
tags_df: pd.DataFrame = pd.DataFrame()
license_df: pd.DataFrame = pd.DataFrame()
commits_level_df: pd.DataFrame = pd.DataFrame()
issues_level_df: pd.DataFrame = pd.DataFrame()

# Go through each item in the loaded `json_data` list, which would represent
# a repository. Then load the data about each repository into the respective 
# DataFrames.

for repo in json_data: 
    
    print(f"Processing repository: {repo['repository']}")
    
    #
    # Repository URL and platform
    #
    
    repositories_df = repositories_df.append(
        {
            "repository": repo["repository"], 
            "platform": "GitHub"
            }, 
        ignore_index=True
    )
    
    #
    # Files count, openness, and encoding
    #
    
    files_editability: dict = {
        "repository": repo["repository"], 
        "files_count": repo["requested_data"]["files_editability"]["files_count"], 
        "open": repo["requested_data"]["files_editability"]["files_openness"]["open"], 
        "closed": repo["requested_data"]["files_editability"]["files_openness"]["closed"], 
        "openness_other": repo["requested_data"]["files_editability"]["files_openness"]["other"], 
        "binary": repo["requested_data"]["files_editability"]["files_encoding"]["binary"], 
        "text": repo["requested_data"]["files_editability"]["files_encoding"]["text"], 
        "encoding_other": repo["requested_data"]["files_editability"]["files_encoding"]["other"]
    }
    
    files_editability_df = files_editability_df.append(
        files_editability, 
        ignore_index=True
    )
    
    #
    # File types breakdown
    #
    
    files_info: dict = {
        "repository": repo["repository"], 
        "total_files": repo["requested_data"]["files_info"]["total_files"], 
        "ecad_files": repo["requested_data"]["files_info"]["ecad_files"], 
        "mcad_files": repo["requested_data"]["files_info"]["mcad_files"], 
        "image_files": repo["requested_data"]["files_info"]["image_files"], 
        "data_files": repo["requested_data"]["files_info"]["data_files"], 
        "document_files": repo["requested_data"]["files_info"]["document_files"], 
        "other_files": repo["requested_data"]["files_info"]["other_files"], 
        "ecad_proportion": repo["requested_data"]["files_info"]["ecad_proportion"], 
        "mcad_proportion": repo["requested_data"]["files_info"]["mcad_proportion"], 
        "image_proportion": repo["requested_data"]["files_info"]["image_proportion"], 
        "data_proportion": repo["requested_data"]["files_info"]["data_proportion"], 
        "document_proportion": repo["requested_data"]["files_info"]["document_proportion"], 
        "other_proportion": repo["requested_data"]["files_info"]["other_proportion"]
    }
    
    files_info_df = files_info_df.append(
        files_info, 
        ignore_index=True
    )
    
    #
    # Repository tags
    #
    
    # Create list of tags
    repo_tags_list: list = [tag["topic"]["name"] for tag in repo["requested_data"]["tags"]]
    # Add "(no tags)" tag if there are not tags
    if len(repo_tags_list) == 0: 
        repo_tags_list = ["(no tags)"]
    
    for tag in repo_tags_list: 
        tags_df = tags_df.append(
            {
                "repository": repo["repository"], 
                "tag": tag
            }, 
            ignore_index=True
        )
    
    #
    # Repository license
    #
    
    # Handle situation with no license
    if repo["requested_data"]["license"] == None: 
        license_info: dict = {
            "repository": repo["repository"], 
            "name": "none detected", 
            "spdxId": "NA", 
            "url": "NA", 
            "permissions": ["NA"], 
            "conditions": ["NA"], 
            "limitations": ["NA"]
        }
    # Otherwise, add information about license
    else: 
        permissions: list = [
            i["label"] for i in repo["requested_data"]["license"]["permissions"]
        ]
        conditions: list = [
            i["label"] for i in repo["requested_data"]["license"]["conditions"]
        ]
        limitations: list = [
            i["label"] for i in repo["requested_data"]["license"]["limitations"]
        ]
        license_info: dict = {
            "repository": repo["repository"], 
            "name": repo["requested_data"]["license"]["name"], 
            "spdxId": repo["requested_data"]["license"]["spdxId"], 
            "url": repo["requested_data"]["license"]["url"], 
            "permissions": str(permissions), 
            "conditions": str(conditions), 
            "limitations": str(limitations)
        }
    
    license_df = license_df.append(
        license_info, 
        ignore_index=True
    )
    
    #
    # Commits
    #
    
    commits_list: list = [
        {
            "repository": repo["repository"], 
            "oid": commit["oid"], 
            "committedDate": commit["committedDate"], 
            "messageHeadline": commit["messageHeadline"], 
            "commitUrl": commit["commitUrl"]
        } for commit in repo["requested_data"]["commits_level"]
    ]
    
    commits_level_df = commits_level_df.append(
        commits_list, 
        ignore_index=True
    )
    
    #
    # Issues
    #
    
    issues_list: list = [
        {
            "repository": repo["repository"], 
            "number": issue["number"], 
            "title": issue["title"], 
            "createdAt": issue["createdAt"], 
            "updatedAt": issue["updatedAt"], 
            "url": issue["url"], 
            "state": issue["state"], 
            "closedAt": issue["closedAt"]
        } for issue in repo["requested_data"]["issues_level"]
    ]
    
    issues_level_df = issues_level_df.append(
        issues_list, 
        ignore_index=True
    )

#
# Set DataFrame column data types
#

# Types as defined in: 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes

repositories_df = repositories_df.astype(
    {
        "repository": str, 
        "platform": "category"
    }
)

files_editability_df = files_editability_df.astype(
    {
        "repository": str, 
        "files_count": "int", 
        "open": "int", 
        "closed": "int", 
        "openness_other": "int", 
        "binary": "int", 
        "text": "int", 
        "encoding_other": "int"
    }
)

files_info_df = files_info_df.astype(
    {
        "repository": str, 
        "total_files": "int", 
        "ecad_files": "int", 
        "mcad_files": "int", 
        "image_files": "int", 
        "data_files": "int", 
        "document_files": "int", 
        "other_files": "int", 
        "ecad_proportion": "float", 
        "mcad_proportion": "float", 
        "image_proportion": "float", 
        "data_proportion": "float", 
        "document_proportion": "float", 
        "other_proportion": "float"
    }
)

tags_df = tags_df.astype(
    {
        "repository": str, 
        "tag": str
    }
)

license_df = license_df.astype(
    {
        "repository": str, 
        "name": str, 
        "spdxId": str, 
        "url": str, 
        "permissions": str, 
        "conditions": str, 
        "limitations": str
    }
)

commits_level_df = commits_level_df.astype(
    {
        "repository": str, 
        "oid": str, 
        "committedDate": "datetime64[ns]", 
        "messageHeadline": str, 
        "commitUrl": str
    }
)

issues_level_df = issues_level_df.astype(
    {
        "repository": str, 
        "number": "int", 
        "title": str, 
        "createdAt": "datetime64[ns]", 
        "updatedAt": "datetime64[ns]", 
        "url": str, 
        "state": "category", 
        "closedAt": "datetime64[ns]"
    }
)

#
# Save DataFrames to SQLite database
#

# Open connection to database
conn = sqlite3.connect('delitos.db')
# Save DataFrames to database tables
# SQLite `dtype`s as defined in: 
# https://docs.sqlalchemy.org/en/14/core/type_basics.html
repositories_df.to_sql(
    'repositories', 
    conn, 
    if_exists="replace", 
    dtype={
        "platform": "Enum"
    }
)
files_editability_df.to_sql(
    'files_editability', 
    conn, 
    if_exists="replace"
)
files_info_df.to_sql(
    'files_info', 
    conn, 
    if_exists="replace", 
    dtype={
        "ecad_proportion": "Float", 
        "mcad_proportion": "Float", 
        "image_proportion": "Float", 
        "data_proportion": "Float", 
        "document_proportion": "Float", 
        "other_proportion": "Float"
    }
)
tags_df.to_sql(
    'tags', 
    conn, 
    if_exists="replace"
)
license_df.to_sql(
    'license', 
    conn, 
    if_exists="replace"
)
commits_level_df.to_sql(
    'commits_level', 
    conn, 
    if_exists="replace", 
    dtype={
        "committedDate": "DateTime"
    }
)
issues_level_df.to_sql(
    'issues_level', 
    conn, 
    if_exists="replace", 
    dtype={
        "createdAt": "DateTime", 
        "updatedAt": "DateTime", 
        "state": "Enum", 
        "closedAt": "DateTime"
    }
)

pass