import cloud
from optparse import OptionParser

if __name__ == '__main__':
 
    username = "wrong" 
    password = "wrong"

    cloud.account.list_keys(username, password)

#[Sat Nov 30 07:55:58 2013] - [ERROR] - Cloud.HTTPConnection: rawquery: received error from server: Error 999: Username/Password were incorrect, not found, or deactivated.
#Traceback (most recent call last):
#  File "list_keys.py", line 14, in <module>
#    cloud.account.list_keys(options.username, options.password)
#  File "/home/ve/local/lib/python2.7/site-packages/cloud/account.py", line 44, in list_keys
#    auth=(username, password))
#  File "/home/ve/local/lib/python2.7/site-packages/cloud/transport/network.py", line 519, in send_request
#    log_cloud_excp = log_cloud_excp)
#  File "/home/ve/local/lib/python2.7/site-packages/cloud/transport/network.py", line 387, in send_request_helper
#    retry=error['retry'], logger=cloudLog)
#cloud.cloud.CloudException: Error 999: Username/Password were incorrect, not found, or deactivated.

