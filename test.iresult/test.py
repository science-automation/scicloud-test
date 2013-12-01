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

def square(x):
        time.sleep(x)
        return x*x

#def test_iresult():
#    jids = cloud.map(square, range(8))
#    for y in cloud.iresult(jids):
#        print y

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.iresult called without arguments'''
    cloud.iresult()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.iresult called with 1 invalid argument'''
    cloud.iresult("asdf")
