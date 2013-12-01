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
    answer = cloud.result(jid)
    assert answer == 9

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.result called without arguments'''
    cloud.result()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.result called with string argument'''
    cloud.result("asdf")

@raises(CloudException)
def test_exception3():
    '''Raise TypeError since cloud.result called with invalid job number'''
    cloud.result(1000000)

