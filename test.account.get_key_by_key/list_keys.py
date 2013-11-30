import cloud
from optparse import OptionParser

if __name__ == '__main__':
 
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username",
                  help="user name", metavar="FILE")
    parser.add_option("-p", "--password", dest="password",
                  help="user password", metavar="FILE")
    (options, args) = parser.parse_args()
 

    cloud.account.list_keys(options.username, options.password)
