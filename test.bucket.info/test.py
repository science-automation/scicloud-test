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
def test_info_content_type():
    '''Get content_type on existing file'''
    info = cloud.bucket.info('test1.txt')
    assert info['content-type'] == "text/plain"

@with_setup(setup_function, teardown_function)
def test_info_cache_control():
    '''Get content_type on existing file'''
    info = cloud.bucket.info('test1.txt')
    assert info['cache-control'] == None

@with_setup(setup_function, teardown_function)
def test_info_content_disposition():
    '''Get content_disposition on existing file'''
    info = cloud.bucket.info('test1.txt')
    assert info['content-disposition'] == None

@with_setup(setup_function, teardown_function)
def test_info_md5():
    '''Get md5sum on existing file'''
    info = cloud.bucket.info('test1.txt')
    assert info['md5sum'] == '08c1f0b56a2f061a370ad61d01a839c9'

@raises(CloudException)
def test_get_no_exist():
    '''Raise CloudException since file should not exist'''
    assert cloud.bucket.info('doesnotexist.txt') == False

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since bucket.info called without arguments'''
    cloud.bucket.info()
