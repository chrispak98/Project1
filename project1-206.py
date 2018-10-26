import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	f = open(file, "r")
	lines = f.readlines()
	f.close()
	dictobjects = []

	for x in range(1, len(lines)):
		dict = {}

		line = lines[x]
		values = line.split(",")

		dict['First'] = values[0]
		dict['Last'] = values[1]
		dict['Email'] = values[2]
		dict['Class'] = values[3]
		dict['DOB'] = values[4]

		dictobjects.append(dict)
	return dictobjects

def mySort(data,col):
	sort = sorted(data, key = lambda x: x[col],)
	dictlist = sort[0]
	return dictlist["First"] + " " + dictlist["Last"]


def classSizes(data):
	ClassSize = {}

	for x in data:
		if x["Class"] in ClassSize:
			ClassSize[x["Class"]] = ClassSize.get(x["Class"]) + 1
		else:
			ClassSize[x["Class"]] = 1
	sort = sorted(ClassSize.items(), key = lambda x: x[1], reverse = True)

	return sort


def findMonth(a):
	monthdict = {}

	for x in a:
		birth = x['DOB'].split('/')[0]

		if birth in monthdict:
			monthdict[birth] = monthdict.get(birth) + 1
		else:
			monthdict[birth] = 1
	sort = sorted(monthdict.items(), key = lambda x: x[1], reverse = True)
	return int(sort[0][0])




def mySortPrint(a,col,fileName):
	outFile = open(fileName, 'w')
	sort = sorted(a, key = lambda x: x[col])

	for x in sort:
		outFile.write(x['First'] + ',' + x['Last'] + ',' + x['Email'] + '\n')

	outFile.close()



def findAge(a):
	sum = 0
	for x in a:
		age = int(x['DOB'].split('/')[2])
		ages = 2018 - age
		sum = sum + ages
	return int(sum / len(a))


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
