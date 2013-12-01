#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
import random

def setup_function():
    pass

def teardown_function():
    pass

@with_setup(setup_function, teardown_function)
def test_environment_rsync():
    '''Create environment with random name and then call rsync'''
    name = "testenv" + str(random.randint(1,1000000))
    clonename = "testenv" + str(random.randint(1,1000000))
    cloud.environment.create(name,'precise')
    sync_path = name + ":/tmp"
    result = cloud.environment.rsync('sync',sync_path)
    cloud.environment.save_shutdown(name)
    assert result is None

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.environment.rsync called with 0 arguments'''
    cloud.environment.rsync()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.environment.rsync called with one argument'''
    cloud.environment.rsync('asdf')

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.environment.clone called with env that does not exist'''
    cloud.environment.save_shutdown('asdfd','asdg')

