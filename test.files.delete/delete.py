import cloud

def setup_function():
    cloud.files.put('test.txt')

def teardown_function():
    print "Tear down"


if __name__ == '__main__':

    setup_function()
    cloud.files.delete('test.txt')
    teardown_function()
