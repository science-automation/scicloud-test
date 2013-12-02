#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
import sys

def setup_function():
    pass
 
def teardown_function():
    pass

def test_info_all():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['status','stdout','stderr','logging','pilog','exception','runtime','created','finished','env','vol','function','label','args','kwargs','func_body','attributes','profile','memory','cputime','cpu_percentage','ports'] )
    obj = result[jid]
    assert obj['status'] == 'done'

def test_info_status():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['status'] )
    obj = result[jid]
    assert obj['status'] == 'done'

def test_info_stdout():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['stdout'] )
    obj = result[jid]
    assert obj['stdout'] == None

def test_info_stderr():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['stderr'] )
    obj = result[jid]
    assert obj['stderr'] == None

def test_info_logging():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['logging'] )
    obj = result[jid]
    assert obj['logging'] == ''

def test_info_pilog():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['pilog'] )
    obj = result[jid]
    assert obj['pilog'] == ''

def test_info_exception():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['exception'] )
    obj = result[jid]
    assert obj['exception'] == None

def test_infoi_runtime():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['runtime'] )
    obj = result[jid]
    assert obj['runtime'] > 0

def test_info_created():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['created'] )
    obj = result[jid]
    assert obj['created'] is not None

def test_info_finished():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['finished'] )
    obj = result[jid]
    assert obj['finished'] is not None

def test_info_env():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['env'] )
    obj = result[jid]
    assert obj['env'] == ''

#def test_info_volume():
#    jid = cloud.call(lambda: 3*3)
#    cloud.join(jid)
#    result = cloud.info(jid, ['volume'] )
#    obj = result[jid]
#    assert obj['volume'] == None

def test_info_function():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['function'] )
    obj = result[jid]
    assert obj['function'] is not None

def test_info_label():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['label'] )
    obj = result[jid]
    assert obj['label'] == ''

def test_info_args():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['args'] )
    obj = result[jid]
    assert obj['args'] is not None

#def test_info_kargs():
#    jid = cloud.call(lambda: 3*3)
#    cloud.join(jid)
#    result = cloud.info(jid, ['kargs'] )
#    obj = result[jid]
#    assert obj['kargs'] == None

#def test_info_func_body():
#    jid = cloud.call(lambda: 3*3)
#    cloud.join(jid)
#    result = cloud.info(jid, ['func_body'] )
#    obj = result[jid]
#    assert obj['func_body'] == None

#def test_info_attributes():
#    jid = cloud.call(lambda: 3*3)
#    cloud.join(jid)
#    result = cloud.info(jid, ['attributes'] )
#    obj = result[jid]
#    assert obj['attributes'] == None

def test_info_profile():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['profile'] )
    obj = result[jid]
    assert obj['profile'] == ''

def test_info_memory():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['memory.max_usage'] )
    obj = result[jid]
    assert obj['memory.max_usage'] > 0

def test_info_cputime():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['cputime.user'] )
    obj = result[jid]
    assert obj['cputime.user'] > 0

def test_info_cpu_percentage():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['cpu_percentage'] )
    obj = result[jid]
    assert obj['cpu_percentage.system'] == None

def test_info_ports():
    jid = cloud.call(lambda: 3*3)
    cloud.join(jid)
    result = cloud.info(jid, ['ports'] )
    obj = result[jid]
    assert obj['ports'] == ''

@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.info called without arguments'''
    cloud.info()

@raises(TypeError)
def test_exception2():
    '''Raise TypeError since cloud.info called with 1 invalid argument'''
    cloud.info("asdf")

@raises(TypeError)
def test_exception3():
    '''Raise TypeError since cloud.info called with 2 invalid arguments'''
    cloud.info("asdf","sadf")

