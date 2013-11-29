import cloud

if __name__ == '__main__':

    # put face.jpg into your bucket
    cloud.bucket.put('test3.txt')

    # sync it
    cloud.bucket.sync_to_cloud('test3.txt')
