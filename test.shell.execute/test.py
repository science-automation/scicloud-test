#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *


def setup_function():
    pass
 
def teardown_function():
    pass

#@with_setup(setup_function, teardown_function)
#def test_register():
#    cloud.shell.execute(lambda: 3*3,return_file='return.txt')

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.shell.execute called without arguments'''
    cloud.shell.execute()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.shell.execute called with invalid function'''
    cloud.shell.execute('asdfasdf')
