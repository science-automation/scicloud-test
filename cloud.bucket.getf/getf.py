import cloud

if __name__ == '__main__':

    # put face.jpg into your bucket
    cloud.bucket.put('test1.txt')
    cloud.bucket.getf('test1.txt')
