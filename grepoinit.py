#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
grepoinit: GitHub Repository INIT;
to start your next python3 project.

Note: it requires libraries
$ pip3 install --upgrade plumbum mkdocs pyscaffold requests
"""

#########################
import os
import argparse
import getpass
import shutil
import requests
# import sys
from plumbum import local
from plumbum.cmd import \
    git, putup, mkdocs, \
    mv, rm  # , ls

description = "Automatic python3 git project creation"

#########################
# Command line options
arg = argparse.ArgumentParser(description='Template for Github python3 repo')

arg.add_argument('repo', type=str, metavar='REPOSITORY_NAME',
                 help='Github repository name to create')
arg.add_argument('user', type=str, metavar='GITHUB_USERNAME',
                 help='Github existing account')
arg.add_argument("--force", action="store_true",
                 help='force removal of existing dir with the same name')

#########################
args = arg.parse_args()
print("Arguments", args)

#########################
# Existing directory
if os.path.exists(args.repo):
    if args.force:
        shutil.rmtree(args.repo)
    else:
        print("Project '%s' already exists..." % args.repo)
        print("Add --force to remove it")
        exit(1)

#########################
# Inital scaffold
putup[args.repo]()

# Change dir
path = os.path.join(os.getcwd(), args.repo)
local.cwd.chdir(path)

# Remove useless
rm['-r', 'README.rst', 'docs']()

#########################
# Init new git repo
git["init"]()
var = 'tmp'

# Make the docs
mkdocs['new', var]()
mv[var+'/docs', var+'/mkdocs.yml', '.']()
rm['-r', var]()
# print(ls['-a']())

#########################
# Requirements?
with open('requirements.txt', 'w') as f:
    f.write('Flask')

#########################
with open('README.md', 'w') as f:
    f.write('#' + args.repo + '\n' + description)
git['add', '*', '.*']()
out = git['commit', '-m', '"First commit"']()
print(out)

# #########################
# gapi = "https://api.github.com"
# params = '{ "name": "'+args.repo+'", "description": "'+description+'", ' + \
# '"homepage": "https://github.com", "private": false,
# "has_issues": true, ' + \
# '"has_wiki": true, "has_downloads": true }'
# params = '{ "name": "'+args.repo+'"}'
# access = args.user + ':'
# curl['-u', "\"$guser:$gpass\" $gapi/user/repos -d $params

print("Trying to access as '" + args.user + "' github account\n")
password = getpass.getpass()
r = requests.get('https://api.github.com/user', auth=(args.user, password))
out = r.json()
if 'message' in out and out['message'] == 'Bad credentials':
    print(out['message'])
    exit(1)

print(out)

#########################
print("Done")
