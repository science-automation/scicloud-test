import cloud

if __name__ == '__main__':

    # put face.jpg into your bucket
    cloud.bucket.put('test1.txt')
    cloud.bucket.get('test1.txt','data/test1.txt')
