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
def test_is_public():
    '''File should exist and not be public'''
    assert cloud.bucket.is_public('test1.txt') == False

@with_setup(setup_function, teardown_function)
def test_is_public2():
    '''File should exist and be public'''
    cloud.bucket.make_public('test1.txt')
    info = cloud.bucket.info('test1.txt')
    print info
    assert cloud.bucket.is_public('test1.txt') == info['url']

@raises(CloudException)
def test_get_no_exist():
    '''Raise CloudException since file should not exist'''
    assert cloud.bucket.is_public('doesnotexist.txt') == False

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since bucket.is_public called without arguments'''
    cloud.bucket.is_public()
