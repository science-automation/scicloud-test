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
def test_getf():
    '''Create CloudBucketObject for the file.  Tell will confirm file is at position 0'''
    bucketobj = cloud.bucket.getf('test1.txt') 
    assert bucketobj.tell() == 0

@raises(TypeError)
def test_exception1():
    '''Raise CloudException since bucket.getf called without arguments'''
    cloud.bucket.getf()

@raises(CloudException)
def test_exception2():
    '''Raise CloudException since bucket.getf called without arguments'''
    cloud.bucket.getf('doesnotexist.txt')
