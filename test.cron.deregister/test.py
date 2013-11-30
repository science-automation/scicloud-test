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
    cloud.cron.register(lambda: 3*3, 'mycron', '5 0 * * *')
 
def teardown_function():
    pass

@with_setup(setup_function, teardown_function)
def test_deregister():
    cloud.cron.deregister("mycron")

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.deregister called without arguments'''
    cloud.cron.deregister()

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.deregister called with 2 invalid arguments'''
    jid = cloud.call("asdf","sadf")

