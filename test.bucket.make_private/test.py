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
    cloud.bucket.make_public('test1.txt')

def teardown_function():
    cloud.bucket.remove('test1.txt')

@with_setup(setup_function, teardown_function)
def test_make_private():
    '''File should exist and be made public'''
    cloud.bucket.make_private('test1.txt')
    assert cloud.bucket.is_public('test1.txt') == False

@raises(CloudException)
def test_make_private_no_exist():
    '''Raise CloudException since file should not exist'''
    assert cloud.bucket.make_private('doesnotexist.txt') == False

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since bucket.make_private called without arguments'''
    cloud.bucket.make_private()
