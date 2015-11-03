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
out = git['commit', '-m', '"Initial commit"']()
print(out)

#########################
gapi_epoint = 'https://api.github.com/user/repos'
params = {"name": args.repo, "description": description,
          "homepage": "https://github.com", "private": False,
          "has_issues": True, "has_wiki": True, "has_downloads": True}

print("Trying to access as '" + args.user + "' github account\n")
password = getpass.getpass()

try:
    r = requests.get(gapi_epoint, auth=(args.user, password), params=params)
except requests.exceptions.ConnectionError as e:
    print("Internet connection not available")
    exit(1)

out = r.json()
if 'message' in out and out['message'] == 'Bad credentials':
    print(out['message'])
    exit(1)

##############################
print(out)
repourl = out.url
git['remote', 'add', 'origin', repourl]()
git['remote', '-v']

#########################
print("Done")
