import pydirectinput
import time
from modules.image_work import Image_Processing as ip
from modules.simple_debug import logger as log


class Fisher():
    
    def start_fishing(distance): 
       
        log('Inside start fishing')
        if ip.template_match('Images\\1080p\\hook_test.png',0.70) != None: #if pole out return true
            Fisher.cast_line(distance)
        
        else:               # if pole not out, bring pole out, wait for movement complete then return true
            pydirectinput.press('F3')
            time.sleep(2)
            Fisher.cast_line(distance)
        
    def cast_line(distance):
        log('Inside cast line')
        pydirectinput.mouseDown()
        time.sleep(distance)
        pydirectinput.mouseUp()
        time.sleep(2.5)
        Fisher.bobber(distance)
        #add a check to see if bobber appears.. if not.. restart.. if so move on*****************
        
    def bobber(distance):
        log('Inside bobber before hook fish')
         
        while ip.template_match('Images\\1080p\\bobber_test.png',0.70) != None:
            Fisher.hook_fish(distance)   
            
    def hook_fish(distance):
        # hook_fish = ip.template_match('Images\\1080p\\hook_test.png',0.70)
        # caught = ip.template_match('Images\\1080p\\caught_test.png', 0.70)
        
        while ip.template_match('Images\\1080p\\caught_test.png', 0.70) == None:
            continue
        pydirectinput.click()
        log('Inside hook fish, after click should be calling reel')
        Fisher.reel()   
        
        # if ip.template_match('Images\\1080p\\hook_test.png',0.70) == None:
        #     Fisher.cast_line(distance)
        #     log('Inside hookfish, should only be called if hook fails ')
        #     return
            
    
    
    def reel():
        start_timer = time.time()
        
         #check if fishing pole is out
        while ip.template_match('Images\\1080p\\hook_test.png',0.70) == None and (time.time() - start_timer < 2000): #timer function to handle graphic bugs and long casts. will end the reeling after 2 min
            green_tension = ip.template_match('Images\\1080p\\greenReel_test.png',0.70)
            orange_tension = ip.template_match('Images\\1080p\\orangeReel_test.png',0.70)
            red_tension = ip.template_match('Images\\1080p\\redReel_test.png',0.70)
            fish_hook =  ip.template_match('Images\\1080p\\hook_test.png',0.70) #check if fishing pole is out
            if green_tension != None and orange_tension == None and red_tension == None: #sees green but not orange or red
                
                pydirectinput.keyDown('alt')        #hold down alt to enter free camera mode, fixes the camera move on fish caught    
                pydirectinput.mouseDown()
                log('Inside reel, after mouse down')
            
            if orange_tension != None or red_tension != None: #sees orange OR Red
                
                pydirectinput.mouseUp()
                log('Inside reel, after mouse up')
            
            if fish_hook != None:
                pydirectinput.keyUp('alt')
                log('Inside reel, after alt up and hook seen')
                break
            
        
        
    

    def repair():
        log('Begin Repair')
        pydirectinput.press('TAB')
        time.sleep(2)
        x,y = ip.full_template_match('Images\\1080p\\repairF3.png',0.7)        
        pydirectinput.moveTo(int(x-50),int(y))
        pydirectinput.keyDown('r')
        time.sleep(.25)
        pydirectinput.keyDown('ctrl')
        time.sleep(0.25)
        pydirectinput.click()
        pydirectinput.keyUp('ctrl')
        pydirectinput.keyUp('r')
        pydirectinput.press('esc')
        
        
    
    def anti_afk():
        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')
        pydirectinput.keyDown('w')
        time.sleep(0.6)
        pydirectinput.keyUp('w')