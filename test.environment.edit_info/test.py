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
def test_environment_edit_info():
    '''Create environment and edit it's info'''
    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    newname = "testenv" + str(random.randint(1,1000000))
    cloud.environment.edit_info(name, new_name=newname, new_desc="Updated the information")
    newenv = cloud.environment.list_envs(name=newname)
    newenvdict = newenv[0]
    print newenvdict
    assert newenvdict['name'] == newname
