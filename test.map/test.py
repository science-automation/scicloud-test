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

def test_map():
    jid = cloud.map(lambda: x*y, 3, 3)
    answer = cloud.result(jid)
    assert answer == 9

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.map called without arguments'''
    jid = cloud.map()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.map called with 1 invalid argument'''
    jid = cloud.map("asdf")

@raises(TypeError)
def test_exception4():
    '''Raise TypeError since cloud.map called with 2 invalid arguments'''
    jid = cloud.map("asdf","sadf")

@raises(TypeError)
def test_exception4():
    '''Raise TypeError since second argument is not iterable'''
    jid = cloud.map(lambda: 3*3, 3)


