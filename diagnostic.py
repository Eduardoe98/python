# Create a class to gather data

class Data:

	def __init__(self, name, age, weight, bloop, beatspm, cardiacout):
        	self.name = patients
                self.age = ages
                self.weight = weights
                self.bloop = bloop
                self.beatspm = beatspm
                self.cardiacout = cardiacout

# Define patients' info

patients = ['Laura', 'Peter','Kevin','Emma']

ages = [28, 35, 29, 30]

weights = [60, 78, 85, 57]

bloop = [98, 162, 71, 116]

beatspm = [100, 81, 170, 134]

cardiacout = [6, 9, 2, 7]

f = 'Laura'
f2 = 'Emma'
m = 'Peter'
m2 = 'Kevin'

if f or f2 in patients:
	gender = 'female'
if m or m2 in patients:
	gender = 'male'


num  = 0

for num in range(0,3):
   
                def overview(self):
				if gender == female:
	                                return 'Name: {0}  Age: {1} years old  Gender: female Weight: {2} kg  Blood Pressure: {3} mmHg  Beats per minute: {4}  Cardiac Output: {5} liters per minute '.format(self.name, self.age, self.weight, self.bloop, self.beatspm, self.cardiacout)
				else: 
					return 'Name: {0}  Age: {1} years old  Gender: male Weight: {2} kg  Blood Pressure: {3} mmHg  Beats per minute: {4}  Cardiac Output: {5} liters per minute '.format(self.name, self.age, self.weight, self.bloop, self.beatspm, self.cardiacout)

# Initialize patient

       		Patient_data= Data(patients [num], ages [num], weights [num], bloop [num], beatspm [num], cardiacout [num])

# Conditionals for each parameter and print on screen

	        if bloop[num] > 90 and  bloop[num] < 120:
                	print(Patient_data.overview() + 'your blood pressure status is ok')
       		else:
           		print(Patient_data.overview() + 'your blood pressure status is not ok')

        	if beatspm[num] > 90 and beatspm[num] < 150:
                	print(Patient_data.overview() + 'your beats per minute are in range')
        	else:
             		print(Patient_data.overview() + 'your beats per minute are not in range')

        	if cardiacout[num] > 4 and  cardiacout[num] < 8:
                	print(Patient_data.overview() + 'your cardiac output is ok' )
        	else:
             		print(Patient_data.overview() + 'your cardiac output is not ok') 

     		if bloop[num] > 90 and  bloop[num] < 120:  
                	print(Patient_data.overview() + 'your blood pressure status is ok' )
       		else:
                	print(Patient_data.overview() + 'your blood pressure status is not ok' )

        	if beatspm[num] > 90 and beatspm[num] < 150:  
                	print(Patient_data.overview() + 'your beats per minute are in range' )
        	else:
                	print(Patient_data.overview() + 'your beats per minute are not in range' )

        	if cardiacout[num] > 4 and  cardiacout[num] < 8:
                	print(Patient_data.overview() + 'your cardiac output is ok' )
        	else:
                	print(Patient_data.overview() + 'your cardiac output is not ok' )


