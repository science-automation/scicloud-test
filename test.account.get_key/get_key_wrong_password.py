import cloud
from optparse import OptionParser

if __name__ == '__main__':
 
    username="wrong" 
    password="wrong"
    key="wrong"

    cloud.account.get_key(username, password, key)

# Sat Nov 30 08:12:21 2013] - [ERROR] - Cloud.HTTPConnection: rawquery: http connection failed
