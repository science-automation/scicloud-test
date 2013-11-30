import cloud

def setup_function():
    # check if volume already exists and delete it
    if not cloud.volume.get_list("mydata"):
       cloud.volume.create("mydata", "/data", "This is a mount point")

def teardown_function():
    print "teardown completed"


if __name__ == '__main__':

    setup_function()
    cloud.volume.delete("mydata")
    if not cloud.volume.get_list("mydata"):
       print "mydata was deleted successfully"
    teardown_function()
