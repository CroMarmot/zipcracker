import zipfile
import itertools

##############

zipName = 'passworded.zip'
pwStart = 'bb'
pwEnd = ''
maxLen = 3

##############

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()
alphabet += '0123456789'

def extract(zFile, password):
	try:
		password = password.encode('utf-8')
		zFile.extractall(pwd=password)
		return True

	except Exception as e:
		if 'Bad password' in str(e) or 'Bad CRC-32' in str(e):
			pass # wrong password
		else:
			print(e) # unknown error - print it

		return False

zFile = zipfile.ZipFile(zipName)
combinations = pow(len(alphabet),maxLen)

count = 0

userUpdate = "Cracking "+zipName+" with "+str(combinations)+" combinations. Press enter to begin!"
input(userUpdate)

foundpass = False
for combLen in range (1,maxLen+1):
	for combination in itertools.product(alphabet,repeat=combLen):
		count += 1
		percentageComplete = round(count/combinations * 100,2)
		checkPass = pwStart + ''.join(combination) + pwEnd

		print('{0:.2f}'.format(percentageComplete) + '% done (current attempt: '+checkPass+')'+' ',end='\r')

		if extract(zFile, checkPass):
			print('Unzip successful!'+" "*20+'\n')
			print('Password is:')
			print(checkPass)
			foundpass = True
			break
	if foundpass == True:
		break
