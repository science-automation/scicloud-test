import cloud

def setup_function():
    label = "mycron"
    label2 = "mycron2"
    schedule = "5 0 * * *" 
    cloud.cron.register(lambda: 3*3, label, schedule)
    cloud.cron.register(lambda: 3*4, label2, schedule)

def teardown_function():
    label = "mycron"
    cloud.cron.deregister(label)
    label2 = "mycron2"
    cloud.cron.deregister(label2)


if __name__ == '__main__':

    setup_function()
    crons = cloud.cron.list()
    print crons
    teardown_function()
