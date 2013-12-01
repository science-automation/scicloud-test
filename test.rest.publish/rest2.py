import cloud

if __name__ == '__main__':

    url = cloud.rest.publish(lambda: 3*3, "mult_sample")
    print url
