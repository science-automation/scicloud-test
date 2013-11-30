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
    cloud.cron.deregister("mycron")

@with_setup(setup_function, teardown_function)
def test_manual():
    cloud.cron.manual_run("mycron")

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.manual_run called without arguments'''
    cloud.cron.manual_run()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.manual_run called with 2 arguments'''
    cloud.cron.manual_run("asdf","sadf")
