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
    cloud.result(jid)
    result = cloud.status(jid)
    assert result == "done"

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.status called without arguments'''
    cloud.status()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.status called with 1 invalid argument'''
    jid = cloud.status("asdf")

@raises(CloudException)
def test_exception4():
    '''Raise CloudException since cloud.status called for job that does not exist'''
    cloud.status(100000)

