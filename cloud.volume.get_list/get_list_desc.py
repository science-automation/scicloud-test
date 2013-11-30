import cloud

def setup_function():
    # create some volumes that we can list
    if not cloud.volume.get_list():
        print "Setting up some volumes"
        cloud.volume.create("mydata", "/data", "This is a mount point")
        cloud.volume.create("mydata2", "/data2", "This is a mount point2")
        cloud.volume.create("mydata3", "/data3", "This is a mount point3")

def teardown_function():
    list = cloud.volume.get_list()
    for volume in list:
       print "deleting volume"
       cloud.volume.delete(volume['name'])


if __name__ == '__main__':

    setup_function()
    list =  cloud.volume.get_list()
    for volume in list:
       moreinfo =  cloud.volume.get_list(volume['name'],True)
       print moreinfo
    teardown_function()
