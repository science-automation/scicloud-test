#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
import random

def setup_function():
    pass

def teardown_function():
    pass

@with_setup(setup_function, teardown_function)
def test_environment_save_shutdown():
    '''Create environment with random name and shut it down'''
    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    result = cloud.environment.save_shutdown(name)
    assert result is None 

@raises(CloudException)
def test_exception1():
    '''Raise TypeError since cloud.environment.save_shutdown called with 1 arguments'''
    cloud.environment.save_shutdown('asdfd')

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.environment.save_shutdown called with 2 arguments'''
    cloud.environment.save_shutdown('asdfd','asdg')

