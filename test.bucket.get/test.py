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
def test_get():
    '''Should be able to get file.  Returns None if no issues'''
    assert cloud.bucket.get('test1.txt') == None 

#def test_get_no_exist():
#    '''File should not exist'''
#    assert cloud.bucket.get('doesnotexist.txt') == False

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since bucket.get called without arguments'''
    cloud.bucket.get()

@with_setup(setup_function, teardown_function)
@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.call called with incorrect start byte'''
    cloud.bucket.exists('test1.txt','test/test1.txt',10000)
