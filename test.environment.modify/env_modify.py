import cloud
import random

if __name__ == '__main__':

    name = "testenv" + str(random.randint(1,1000000))
    clonename = "testenv" + str(random.randint(1,1000000))
    cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    hostname = cloud.environment.modify(name)
    cloud.environment.save_shutdown(name)
    print hostname
