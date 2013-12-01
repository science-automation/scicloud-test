import cloud
import random

if __name__ == '__main__':

    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    result = cloud.environment.run_script(name, 'test.sh')
    print result
    cloud.environment.save_shutdown(name)
