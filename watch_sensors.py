#!/usr/bin/python
from gi.repository import Notify
from cpu_temp import CPUTemp
import time

def main():
	Notify.init(__name__)
	ct = CPUTemp()
	ct.set_threshold(55);
	message = str()
	need_notify = bool()
	while True:
		datas = ct.get_temp(sensor_name = "coretemp-isa-0000")
		need_notify = False
		for data in datas:
			message = str()
			if data['value'] > ct.get_threshold()  :
				message = "Temp. of " + data['label'] + " is " + str(data['value']) + "\n" + message
				need_notify = True
		if need_notify: 
			if 'notify' in locals():
				notify.close()
			notify = Notify.Notification.new("Warning",message)
			if message:
				notify.show()	
		else:
			if 'notify' in locals():
				notify.close()
			
		time.sleep(2)
		del message

if __name__ == '__main__':
	main()


