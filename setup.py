"""
This file is needed only when you want to generate an executable using py2exe or py2app
"""
from distutils.core import setup
import py2exe, os

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows=[{'script': "finder.py"}],
    zipfile=None
)

""" FOR MacOs Building change with
from distutils.core import setup
import py2app

setup(
    app=["finder.py"],
)
"""
