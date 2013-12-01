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
    cloud.start_simulator()
 
def teardown_function():
    pass

def test_not_simulated():
    assert cloud.is_simulated() == False

@with_setup(setup_function, teardown_function)
def test_simulated():
     assert cloud.is_simulated() == True

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.is_simulated called with arguments'''
    cloud.is_simulated('asdf')
