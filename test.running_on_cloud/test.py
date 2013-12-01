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

def test_oncloud():
    assert cloud.running_on_cloud() == False

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.call called with arguments'''
    cloud.running_on_cloud('asdfd')
