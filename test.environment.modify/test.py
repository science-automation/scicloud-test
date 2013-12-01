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
def test_environment_modify():
    '''Create environment with random name and then call modify'''
    name = "testenv" + str(random.randint(1,1000000))
    cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    hostname = cloud.environment.modify(name)
    cloud.environment.save_shutdown(name)
    assert hostname is not None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.environment.modify called with 0 arguments'''
    cloud.environment.modify()

@raises(CloudException)
def test_exception2():
    '''Raise TypeError since cloud.environment.modify called with env that does not exist'''
    cloud.environment.modify('asdf')

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.environment.clone called with 2 arguments'''
    cloud.environment.save_shutdown('asdfd','asdg')

