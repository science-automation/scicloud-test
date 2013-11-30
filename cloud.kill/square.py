import cloud
import time

def square(x):
        time.sleep(x)
        return x*x

jids = cloud.map(square, range(4))
# jobs have completed, kill should not have any bad effect
cloud.kill(jids)
