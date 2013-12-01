import cloud
import random

if __name__ == '__main__':

    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    cloud.environment.save(name)
    result = cloud.environment.save_shutdown(name)

