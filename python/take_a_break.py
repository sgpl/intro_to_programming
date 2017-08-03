import time 
import webbrowser

total_breaks = 3
break_count = 0

print "This program started on " + time.ctime()
while break_count < total_breaks:
	time.sleep(2*60*60) # 2 * 60 * 60 = 2 hours
	print "The time is now " + time.ctime()
	print "Get ready to dance...."
	time.sleep(3) # 
	webbrowser.open('https://youtu.be/xo1VInw-SKc', new=2)
	break_count += 1 