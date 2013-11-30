import cloud

if __name__ == '__main__':

    cloud.volume.create("mydata", "/data", "This is a mount point")
    cloud.volume.sync("data","mydata")
