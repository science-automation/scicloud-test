import cloud

if __name__ == '__main__':

    # put face.jpg into your bucket
    cloud.bucket.put('thumb_face.jpg')

    # sync it
    cloud.bucket.sync_to_cloud(thumb_face.jpg)
