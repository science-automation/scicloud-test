import cloud
import time

def square(x):
        time.sleep(x)
        return x*x

jids = cloud.map(square, range(8))
for y in cloud.iresult(jids):
        print y
# will print 0, 1, 4, 9, 16, 25, 36, 49. Printing will start before every job has completed.
