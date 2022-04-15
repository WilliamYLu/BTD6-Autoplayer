import mouse
import keyboard
import time
print(mouse.get_position())
#Preselect Quincy as hero, MK not required. Places a 204 SUB and 042 mauler, will leak a bit at the end but won't die ever.
def mouse_action(x,y,time_sleep=.5):
	mouse.move(x, y, absolute=True, duration=0)
	mouse.click(button='left')
	time.sleep(time_sleep)
while True:
	#GET TO MAIN MENU WITHIN 5 SECONDS OF STARTING
	time.sleep(5)
	#Menuing
	#Play
	mouse_action(1102, 1241)
	#Left Arrow
	mouse_action(370, 558)
	#Dark Castle
	mouse_action(1302, 343)
	#Easy
	mouse_action(861, 565)
	#Standard
	mouse_action(867, 772, 5)
	#Click Hero
	mouse_action(2280, 292)
	#Put Hero (lets use chad Quincy!)
	mouse_action(755, 835)
	#Play
	mouse_action(2455, 1336)
	#Speed Up
	mouse_action(2455, 1336, 15)
	#Click Sub Menu
	mouse_action(2274, 967)
	#Place Sub
	mouse_action(1507, 522, 25)
	#Click on Sub
	mouse_action(1507, 522)
	#100
	mouse_action(392, 611)
	#200
	mouse_action(392, 611, 50)
	#Upgrade 201
	mouse_action(420, 1059)
	#Upgrade 202
	mouse_action(420, 1059, 55)
	#Upgrade 203
	mouse_action(420, 1059, 20)
	#Select Bomb
	mouse_action(2449, 478)
	#Place Bomb
	mouse_action(1048, 896, 10)
	#Click on Sub
	mouse_action(1507, 522,15)
	#Upgrade 204, spam click so we dont miss anything
	mouse_action(420, 1059)
	mouse_action(420, 1059, 40)
	mouse_action(420, 1059, 1)
	#Select Bomb
	mouse_action(1048, 896)
	#Upgrade 030
	mouse_action(468, 830)
	mouse_action(468, 830)
	mouse_action(468, 830, 50)
	#Upgrade 042
	mouse_action(468, 830)
	mouse_action(420, 1059)
	mouse_action(420, 1059, 50)
	#Click Next
	mouse_action(1273, 1202)
	mouse_action(932, 1130, 5)
	#In case there is a collection, continue
	mouse_action(1268, 894)
	#Spam click all possible monkeys earned in collection
	mouse_action(614, 753)
	mouse_action(714, 753)
	mouse_action(814, 753)
	mouse_action(914, 753)
	mouse_action(1014, 753)
	mouse_action(1114, 753)
	mouse_action(1214, 753)
	mouse_action(1314, 753)
	mouse_action(1414, 753)
	mouse_action(1514, 753)
	mouse_action(1614, 753)
	mouse_action(1714, 753)
	mouse_action(1814, 753)
	mouse_action(1914, 753)
	mouse_action(2014, 753)
	# Hit Play 
	mouse_action(2451, 1291, 3)
	#Hit Escape to reset if we are in collection
	keyboard.press_and_release('esc')
	time.sleep(2)
	# Hit Cancel if we weren't in collection
	mouse_action(1047, 973, 2)
