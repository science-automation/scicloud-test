import cloud

def setup_function():
    # check if volume already exists and delete it
    if cloud.volume.get_list("mydata"):
       cloud.volume.delete("mydata")

def teardown_function():
    if cloud.volume.get_list("mydata"):
       cloud.volume.delete("mydata")


if __name__ == '__main__':

    setup_function()
    cloud.volume.create("mydata", "/data", "This is a mount point")
    if cloud.volume.get_list("mydata"):
       print "mydata was created successfully"
    teardown_function()
