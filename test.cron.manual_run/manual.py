import cloud

def setup_function():
    label = "mycron"
    schedule = "5 0 * * *" 
    cloud.cron.register(lambda: 3*3, label, schedule)

def teardown_function():
    label = "mycron"
    cloud.cron.deregister(label)

if __name__ == '__main__':

    setup_function()
    cloud.cron.manual_run("mycron")
    teardown_function()
