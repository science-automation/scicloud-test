import cloud

if __name__ == '__main__':

    cloud.shell.cron_register(lambda: 3*3, 'mycron', '5 0 * * *')

