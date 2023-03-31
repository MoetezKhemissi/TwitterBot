from nordvpn_switcher import initialize_VPN,rotate_VPN
import time
import time

start = time.time()
print("Started timer ...")

##############
## WINDOWS ###
##############


instructions = initialize_VPN(area_input=['France']) # <-- Be aware: the area_input parameter expects a list, not a string

for i in range(3):
    rotate_VPN(instructions) #refer to the instructions variable here
    print('\nDo whatever you want here (e.g.scraping). Pausing for 10 seconds...\n')
    time.sleep(10)

end = time.time()
print("Full time :  to rotate 3 " , end - start)


