#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
import cloud.mp

def setup_function():
    pass
 
def teardown_function():
    pass

def test_multiply():
    jid = cloud.mp.call(lambda: 3*3)
    answer = cloud.mp.result(jid)
    assert answer == 9

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.call called without arguments'''
    jid = cloud.mp.call()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.call called with 1 invalid argument'''
    jid = cloud.mp.call("asdf")

@raises(TypeError)
def test_exception4():
    '''Raise TypeError since cloud.call called with 2 invalid arguments'''
    jid = cloud.mp.call("asdf","sadf")

