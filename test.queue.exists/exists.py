import cloud

def setup_function():
    print "Setup"

def teardown_function():
    print "Tear Down"


if __name__ == '__main__':

    setup_function()
    q = cloud.queue.exists('numbers')
    print q
    teardown_function()
