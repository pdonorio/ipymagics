#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
To start your next python3 project

Note: it requires libraries
$ pip3 install --upgrade plumbum mkdocs pyscaffold
"""

#########################
import os
import argparse
# import sys
# from plumbum.cmd import git, putup, mkdocs

#########################
arg = argparse.ArgumentParser(description='Template for Github python3 repo')
arg.add_argument('repo', type=str, metavar='REPOSITORY_NAME',
                 help='Github repository name to create')
arg.add_argument('user', type=str, metavar='GITHUB_USERNAME',
                 help='Github existing account')
arg.add_argument('--force', dest='forced',
                 action='store_const', const=True, default=False)

#########################
args = arg.parse_args()
print("Arguments", args)

#########################
if not args.forced and os.path.exists(args.repo):
    print("Project '%s' already exists..." % args.repo)
    print("Add --force to remove it")
    exit(1)

print("READY")
