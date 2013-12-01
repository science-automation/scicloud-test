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
    '''Create environment with random name and clone it'''
    name = "testenv" + str(random.randint(1,1000000))
    clonename = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    cloud.environment.clone(name, clonename, new_desc="This is a clone") 
    list = cloud.environment.list_envs(name=clonename)
    cloneenv = list[0]
    assert cloneenv['name'] == clonename

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.environment.clone called with 0 arguments'''
    cloud.environment.clone()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.environment.clone called with 4 arguments'''
    cloud.environment.save_shutdown('asdfd','asdg','asdf','asdf')

