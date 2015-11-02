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
parser = argparse.ArgumentParser(
    description='Template for Github python3 repo')
parser.add_argument('repo', type=str, metavar='REPOSITORY_NAME',
                    help='Github repository name to create')
parser.add_argument('user', type=str, metavar='GITHUB_USERNAME',
                    help='Github existing account')
parser.add_argument('--sum', dest='accumulate', action='store_const')

#########################
args = parser.parse_args()
print("Arguments", args)

#########################
if os.path.exists(args.repo):
    print("Project '%s' already exists..." % args.repo)
    print("Add --force to remove it")
    exit(1)
