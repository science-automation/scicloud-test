import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    info = cloud.bucket.info('test1.txt')
    print info
