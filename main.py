import glob
import os
import pandas as pd

folder_list = os.listdir('SampleInputDirectory')

for i in folder_list:
	fol = 'E:\\python\\test\\SampleInputDirectory\\'+i+'\\'
	os.chdir(fol)
	result = pd.DataFrame()

	for counter, file in enumerate(glob.glob("*")):
		filename = file
		sp = filename.split()
		symbol = sp[0]
		expireDate = sp[1]+'-'+sp[2]+'-'+sp[3]
		optionType = sp[4]
		namedf = pd.read_csv(file,skiprows=0)

		namedf['Symbol'] = symbol
		namedf['ExpiryDate'] = expireDate
		namedf['OptionType'] = optionType
		result = result.append(namedf)


	output = 'E:\\python\\test\\output\\'+i+'.csv'
	result.to_csv(output)
