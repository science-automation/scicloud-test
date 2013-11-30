import cloud

def setup_function():
    print "Setup"

def teardown_function():
    print "Tear Down"


if __name__ == '__main__':

    setup_function()
    q = cloud.queue.get('numbers')
    q.push([1,2,3,4,5])
    print q.count()
    print q.pop()
    teardown_function()
