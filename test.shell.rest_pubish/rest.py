import cloud

if __name__ == '__main__':

    cloud.shell.rest_publish("ls -al", "lsfunc", return_file='return.txt')
