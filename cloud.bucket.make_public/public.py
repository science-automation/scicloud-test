import cloud

if __name__ == '__main__':

    cloud.bucket.put('test1.txt')
    cloud.bucket.make_public('test1.txt')
