import cloud
import time

def square(x):
        time.sleep(x)
        return x*x

jids = cloud.map(square, range(4))
# delete information about these jobs from server
cloud.delete(jids)
