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

def infinite_loop():
    while True:
       pass

def test_kill():
    '''Kill specified job'''
    jid = cloud.call(infinite_loop)        #start a job which will never end
    assert cloud.kill(jid) == None         #at least until you kill it

def test_kill_all():
    '''Kill all running jobs when calling without argument'''
    assert cloud.kill() == None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.call called with string argument'''
    cloud.kill("asdf")
