import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    cloud.bucket.make_private('test1.txt')
