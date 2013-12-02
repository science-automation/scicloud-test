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

def test_multiply():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    answer = cloud.result(jid)
    assert answer == 9

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.join called without arguments'''
    cloud.join()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.join called with 1 invalid argument'''
    cloud.join("asdf")

@raises(TypeError)
def test_exception4():
    '''Raise TypeError since cloud.join called with not existing job'''
    jid = cloud.call(100000)

