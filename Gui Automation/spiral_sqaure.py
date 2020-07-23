import pyautogui as gui
gui.moveTo(112,346)
#set the coordinates according to your screen, mine might not works on yours
gui.click()
distance = 400
slow_one = true
while distance > 0:
    if slow_one == true:
        print('right, ',end = '')
        gui.dragRel(distance,0,duration = 1)
        distance = distance - 10
        print('down, ',end = '')
        gui.dragRel(0,distance,duration = 1)
        print('left, ',end = '')
        gui.dragRel(-distance,0,duration = 1)
        distance =distance - 10
        print('up, ',end = '')
        gui.dragRel(0,-distance,duration = 1)
        slow_one = false
    else:
        print('right, ',end = '')
        gui.dragRel(distance,0,duration = 0.1)
        distance = distance - 10
        print('down, ',end = '')
        gui.dragRel(0,distance,duration = 0.1)
        print('left, ',end = '')
        gui.dragRel(-distance,0,duration = 0.1)
        distance =distance - 10
        print('up ',end = '')
        gui.dragRel(0,-distance,duration = 0.1) 
