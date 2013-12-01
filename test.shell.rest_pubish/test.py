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

@with_setup(setup_function, teardown_function)
def test_rest_publish():
    url = cloud.shell.rest_publish("ls -al", "lsfunc", return_file='return.txt')
    assert url is not None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.shell.rest_publish called without arguments'''
    cloud.shell.rest_publish()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.shell.rest_publish called with one argument'''
    cloud.shell.rest_publish('asdfasdf')
