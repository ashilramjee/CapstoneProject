# This class is used to get different values such as number of males or females
# on different serotypes

from .models import Incident

class DataHandler:

	# gets a list of incident objects, processes them and returns a 2d array on the different counts of each serotype
	def handleData(self, theIncidents):
		list = []
		maleCount = 0
		hivExposedCount = 0
		gugulethuCount = 0
		mandalayCount = 0
		vaccinatedCount = 0
		totalCount = 0
		presenceCount = 0
		femaleCount = 0
		serotypeList = ["ST199","ST361","ST393","ST471","ST1447","ST2059","ST2062","ST2068","ST3358","ST3450","ST3983","ST4088","ST4893","ST5647","ST7052",
						"ST7345","ST8687","ST8838","ST10605","ST10673","ST10823","ST10854","ST13795","ST13797","ST13798","ST13799"]

		# for loop to calculate different counts by going through each incident object
		for i in serotypeList:
			tempSerotype = i[2:]
			for i in theIncidents:
				if (i.sequence == tempSerotype and i.sex == 'Male'):
					maleCount += 1
				if (i.sequence == tempSerotype and i.hivExposed == 'Yes'):
					hivExposedCount += 1
				if (i.sequence == tempSerotype and i.site == 'Gugulethu'):
					gugulethuCount += 1
				if (i.sequence == tempSerotype and i.site == 'Mandalay'):
					mandalayCount += 1
				if (i.sequence == tempSerotype and i.vaccine == 'PCV'):
					vaccinatedCount += 1
				if (i.sequence == tempSerotype.translate(tempSerotype.maketrans('','','*~'))):
					totalCount += 1
				if (i.sequence == tempSerotype and i.presence == 'Yes'):
					presenceCount += 1
				if (i.sequence == tempSerotype and i.sex == 'Female'):
					femaleCount += 1
			list.append([maleCount, hivExposedCount, gugulethuCount, mandalayCount, vaccinatedCount, totalCount, presenceCount, femaleCount])
			maleCount = 0
			hivExposedCount = 0
			gugulethuCount = 0
			mandalayCount = 0
			vaccinatedCount = 0
			totalCount = 0
			presenceCount = 0
			femaleCount = 0
		return list
