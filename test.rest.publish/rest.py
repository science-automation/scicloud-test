import cloud

def add(x, y):
    """This function adds!"""
    return x+y

if __name__ == '__main__':

    url = cloud.rest.publish(add, 'addition')
    print url
