import cloud
from optparse import OptionParser

if __name__ == '__main__':
 
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username",
                  help="user name", metavar="FILE")
    parser.add_option("-p", "--password", dest="password",
                  help="user password", metavar="FILE")
    parser.add_option("-k", "--key", dest="key",
                  help="user password", metavar="FILE")
    (options, args) = parser.parse_args()
 

    cloud.account.get_key(options.username, options.password, options.key)
