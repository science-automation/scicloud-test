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
def test_cron_info():
    cron = cloud.cron.info("mycron")
    assert cron["label"] == "mycron"

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.info called without arguments'''
    cloud.cron.info()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.info called with 2 arguments'''
    cloud.cron.info("asdf","sadf")
