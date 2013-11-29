import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    info = cloud.bucket.get_md5('test1.txt')
    print info
