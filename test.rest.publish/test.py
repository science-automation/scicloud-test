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

@with_setup(setup_function, teardown_function)
def test_rest_publish():
    url = cloud.rest.publish(lambda: 3*3, "mult_sample")
    print url
    assert url is not None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.rest.publish called without arguments'''
    cloud.rest.publish()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.rest.publish called with one argument'''
    cloud.rest.publish('asdfasdf')
