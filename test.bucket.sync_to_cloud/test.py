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
def test_exists():
    '''Sync File To Cloud'''
    assert cloud.bucket.sync_to_cloud('test1.txt') == None

@with_setup(setup_function, teardown_function)
@raises(IOError)
def test_no_exist():
    '''File Does Not Exist'''
    assert cloud.bucket.sync_to_cloud('doesnotexist.txt') == False

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.sync_to_cloud called without arguments'''
    cloud.bucket.sync_to_cloud()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.sync_to_cloud called with 4 arguments'''
    cloud.bucket.sync_to_cloud('file1.txt','file2.txt','file3.txt','file4.txt')
