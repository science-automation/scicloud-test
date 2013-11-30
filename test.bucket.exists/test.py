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
    '''File Should Exist'''
    assert cloud.bucket.exists('test1.txt') == True

@with_setup(setup_function, teardown_function)
def test_no_exist():
    '''File Does Not Exist'''
    assert cloud.bucket.exists('doesnotexist.txt') == False

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.call called without arguments'''
    cloud.bucket.exists()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.call called with 3 arguments'''
    cloud.bucket.exists('file1.txt','file2.txt','file3.txt')
