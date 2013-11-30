import cloud

def setup_function():
    cloud.files.put('test.txt')

def teardown_function():
    cloud.files.delete('test.txt')


if __name__ == '__main__':

    setup_function()
    cloud.files.sync_from_cloud('test.txt')
    teardown_function()
