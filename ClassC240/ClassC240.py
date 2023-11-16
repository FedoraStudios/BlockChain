class Vehicles:
	#a simple class
	#An attribute
	car_name1 = 'Tesla Model 3'
	car_name2 = '1968 Mustang Shelby GT500'

	#sample method
	def main(self):
		print('I have a: ', self.car_name1)
		print('I have a: ', self.car_name2)

#driver code
#object instesiation
vehicleClassObject = Vehicles()

#accesing class attributes and method through objects:
print('your vehicle is: ', vehicleClassObject.car_name2)
vehicleClassObject.main()