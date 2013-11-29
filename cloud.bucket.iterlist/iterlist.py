import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    list = cloud.bucket.iterlist()
    print list
