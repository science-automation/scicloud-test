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
    cloud.bucket.put('test1.txt')

def teardown_function():
    cloud.bucket.remove('test1.txt')

@with_setup(setup_function, teardown_function)
def test_iterlist():
    '''Retrieve obj_paths of all user's objects stored on PiCloud'''
    iterlist = cloud.bucket.iterlist()
    first = iterlist.next
    assert first is not None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since bucket.iterlist called with 5 arguments'''
    cloud.bucket.iterlist('asdf','asdg','asdg','asgd','asdg')
