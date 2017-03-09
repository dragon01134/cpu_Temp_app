import sensors
import time
import os




class CPUTemp():
	def __init__(self):
		"""Init function for cpu temprature"""
		sensors.init()
	def get_temp(self,sensor_name):
		""" doc """
		data_list = list()
		for chip in sensors.iter_detected_chips():
			if str(chip) == sensor_name:
				for feature in chip:
					sensor_data = dict()
					sensor_data['label'] = feature.label
					sensor_data['value'] = feature.get_value()
					data_list.append(sensor_data)
		
		return data_list
	def set_threshold(self,threshold = 55 ):
		""" This function allow to set threshold valuef of temp"""
		self.threshold = threshold
	def get_threshold(self):
		"""get threshold value"""
		return self.threshold 
	def clean_up():
		"""Clean up sensors """
    		sensors.cleanup()
		

if __name__ == '__main__':
	ct = CPUTemp()
	ct.set_threshold(52);
	while True:
		datas = ct.get_temp(sensor_name = "coretemp-isa-0000")
		for data in datas:
			if data['value'] > ct.get_threshold()  :
				print  data['label'] + "->" + str(data['value'])
		time.sleep(1)
	

