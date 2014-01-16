#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
# Assumes environment exists with name test2
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
import random

def setup_function():
    pass

def teardown_function():
    cloud.environment.edit_info("test3", new_name="test2", new_desc="Updated the information")

@with_setup(setup_function, teardown_function)
def test_environment_edit_info():
    newname = "test3"
    cloud.environment.edit_info("test2", new_name=newname, new_desc="Updated the information")
    newenv = cloud.environment.list_envs(name=newname)
    newenvdict = newenv[0]
    print newenvdict
    assert newenvdict['name'] == newname

#@raises(CloudException)
#def test_exception_one_argumment():
#    '''Raise CloudException since cloud.environment.edit_info called with 1 arguments'''
#    cloud.environment.edit_info('asdfd')

@raises(CloudException)
def test_exception_invalid_base_environment():
    '''Raise CloudException since cloud.environment.edit_info called with invalid environment name'''
    cloud.environment.edit_info('asdfd','precise2', new_desc="Updated the information")
