from modules import fisher, image_work, simple_debug
import time

fish = fisher.Fisher
image = image_work.Image_Processing
log = simple_debug.logger


time.sleep(2)
x=0
repair_count = 0
distance = 0.7
while x <= 1000:
    if repair_count == 3:
        fish.repair()
        repair_count = 0
        fish.anti_afk()
        log(str(repair_count))
    fish.start_fishing(distance)
    log('Finished Iteration : {}'.format(x))
    print('Iteration Done')
    x=+1
    
        
        