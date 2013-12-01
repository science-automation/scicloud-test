import cloud
import random

if __name__ == '__main__':

    name = "testenv" + str(random.randint(1,1000000))
    hostname = cloud.environment.create(name,'precise')
    cloud.environment.save_shutdown(name)
    newname = "testenv" + str(random.randint(1,1000000))
    cloud.environment.edit_info(name, new_name=newname, new_desc="Updated the information")
    newenv = cloud.environment.list_envs(name=newname)
    print newenv
