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
def test_list():
    '''Should be able to get file.  Returns None if no issues'''
    list = cloud.bucket.list()
    assert len(list) > 0 

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since bucket.get called with 5 arguments'''
    cloud.bucket.list('asdf','asdg','asdg','asgd','asdg')
