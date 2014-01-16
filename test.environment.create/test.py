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
def test_environment_create():
    '''Create environment with random name'''
    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    assert hostname is not None 

@raises(TypeError)
def test_exception_one_argumment():
    '''Raise TypeError since cloud.environment.create called with 1 arguments'''
    cloud.environment.create('asdfd')

@raises(CloudException)
def test_exception_invalid_base_environment():
    '''Raise TypeError since cloud.environment.create called with invalid base environment'''
    cloud.environment.create('asdfd','precise2')

