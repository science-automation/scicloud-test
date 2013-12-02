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

def test_delete():
    jid = cloud.call(lambda: 3*3)
    cloud.result(jid)
    result = cloud.delete(jid)
    assert result is None

@raises(CloudException)
def test_exception1():
    '''Raise CloudException since cloud.delete called and then cloud.result after job info has been deleted'''
    jid = cloud.call(lambda: 3*3)
    cloud.result(jid)
    result = cloud.delete(jid)
    fail = cloud.result(jid)

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.delete called without arguments'''
    cloud.delete()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.delete called with 1 invalid argument'''
    cloud.delete("asdf")
