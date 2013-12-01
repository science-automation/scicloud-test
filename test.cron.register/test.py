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
    cloud.cron.deregister("mycron")

@with_setup(setup_function, teardown_function)
def test_register():
    cloud.cron.register(lambda: 3*3, 'mycron', '5 0 * * *')

@raises(ValueError)
def test_register_invalid_cron():
    cloud.cron.register(lambda: 3*3, 'mycron', '5 0 * * * *')

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.register called without arguments'''
    cloud.cron.register()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.register called with 1 arguments'''
    cloud.cron.register('asdfasdf')

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.register called with 2 arguments'''
    cloud.cron.register('asdfasdf','asdfdsf')

@raises(TypeError)
def test_exception4():
    '''Raise TypeError since cloud.register called with 4 arguments'''
    cloud.cron.register('asdfasdf','asdfdsf','asdfads','asdfds')


