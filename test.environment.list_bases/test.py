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
#    cloud.environment.create('testenv','precise')
    pass

def teardown_function():
    # unable to delete environments through api
    pass

@with_setup(setup_function, teardown_function)
def test_environment_list():
    '''List the environment bases'''
    list = cloud.environment.list_bases()
    assert len(list) > 0

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.environment.list_envs called with 1 argument'''
    cloud.environment.list_bases('asdfd')
