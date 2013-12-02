#
# Test cases for Science VM scicloud API
#
# Copyright 2014 Science Automation
#
import cloud
from cloud import CloudException, CloudTimeoutError
from nose import with_setup
from nose.tools import *
from cloud.util.configmanager import ConfigSettings
import cloud.cloudconfig as cc

def setup_function():
    pass
 
def teardown_function():
    pass

def test_config():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert cc._needsWrite == False

def test_config_api_key():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.api_key == '8432'

def test_config_automatic_dependency_transfer():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.automatic_dependency_transfer == True

def test_config_cloud_result_cache_size():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.cloud_result_cache_size == 4096

def test_config_cloud_status_cache_size():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.cloud_status_cache_size == 65536

def test_config_force_serialize_logging():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.force_serialize_logging == True

def test_config_http_close():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.http_close == False

def test_config_log_filename():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.log_filename == 'cloud.log'

def test_config_log_level():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.log_level == 'DEBUG'

def test_config_max_transmit_data():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.max_transmit_data == 1000000

def test_config_mp_cache_size_limit():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.mp_cache_size_limit == 0

def test_config_num_procs():
    config = ConfigSettings(cc.config)  #sets cc.config values
    assert config.num_procs == 8

def test_config_print_log_level():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.print_log_level == 'ERROR'

def test_config_proxy_server():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.proxy_server == None

def test_config_purge_days():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.purge_days == 7

def test_config_redirect_job_output():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.redirect_job_output == True

def test_config_save_log():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.save_log == True

def test_config_serialize_logging():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.serialize_logging == False

def test_config_serialize_logging_path():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.serialize_logging_path == 'datalogs/'

def test_config_server_list_url():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.server_list_url == 'http://api.picloud.com/servers/list/'

def test_config_use_gzip():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.use_gzip == True

def test_config_use_simulator():
    config = ConfigSettings(cc.config)  #sets cc.config values
    config.use_simulator == False




@raises(TypeError)
def test_exception1():
    '''Raise TypeError since cloud.config.commit called with an argument'''
    config = ConfigSettings()
