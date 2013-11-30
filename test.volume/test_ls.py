import cloud
from nose import with_setup

def setup_function():
    pass
 
def teardown_function():
    cloud.volume.delete("nosedata2")
 
@with_setup(setup_function, teardown_function)
def test_volume_create():
    assert cloud.volume.create("nosedata2", "/nose2", "This is a mount point") == True


#    cloud.volume.create("mydata", "/data", "This is a mount point")
#    cloud.volume.sync("data","mydata")
