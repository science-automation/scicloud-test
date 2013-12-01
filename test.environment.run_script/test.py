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

#@with_setup(setup_function, teardown_function)
#def test_environment_run_script():
#    '''Create environment with random name, run script on it and shut it down'''
#    name = "testenv" + str(random.randint(1,1000000))
#    hostname = cloud.environment.create(name,'precise')
#    result = cloud.environment.ssh(name, cmd='cd /; ls -al')
#    cloud.environment.run_script(name)
#    assert result is not None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.environment.run_script called with 0 arguments'''
    cloud.environment.run_script()

@raises(CloudException)
def test_exception2():
    '''Raise TypeError since cloud.environment.run_script called with invalid script name'''
    cloud.environment.run_script('asdfd','asdg')

