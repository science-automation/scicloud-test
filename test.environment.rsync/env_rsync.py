import cloud
import random

if __name__ == '__main__':

    name = "testenv" + str(random.randint(1,1000000))
    clonename = "testenv" + str(random.randint(1,1000000))
    cloud.environment.create(name,'precise')
    sync_path = name + ":/tmp"
    cloud.environment.rsync('sync',sync_path)
    cloud.environment.save_shutdown(name)
