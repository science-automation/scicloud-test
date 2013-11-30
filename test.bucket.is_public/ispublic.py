import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    if (cloud.bucket.is_public('test1.txt')):
       print "File is public"
    else
       print "File is not public"
