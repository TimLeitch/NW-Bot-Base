import datetime

def logger(error):
    with open('log.txt', 'a') as log:
        dts = datetime.datetime.now().replace(microsecond=0)
        log.write('{}: {} \n'.format(dts, error))

        
        