#!/usr/bin/env python3
import zipfile
import itertools
import argparse

##############

pwStart = ''
pwEnd = ''
maxLen = 6

##############

def extract(zFile, password):
    try:
        password = password.encode('utf-8')
        zFile.extractall(pwd=password)
        return True

    except Exception as e:
        stre = str(e)
        if 'Bad password' in stre :
            pass
        elif 'Bad CRC-32' in stre:
            pass
        elif 'invalid code lengths set' in stre:
            pass
        elif 'invalid stored block lengths' in stre:
            pass
        elif 'invalid block type' in stre:
            pass
        elif 'too many length or distance symbols' in stre:
            pass
        elif 'invalid distance too far back' in stre:
            pass
        elif 'invalid literal/length code' in stre:
            pass
        elif 'invalid distance code' in stre:
            pass
        elif 'invalid bit length repeat' in stre:
            pass
        else:
            print(f"Bad password {password}") # unknown error - print it
            print(stre) # unknown error - print it

        return False

def main():
    alphabet = ''
    alphabet += 'abcdefghijklmnopqrstuvwxyz'
    alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += '0123456789'

    parser = argparse.ArgumentParser()
    parser.add_argument("zipPath")
    args = parser.parse_args()
    zipName = args.zipPath

    zFile = zipfile.ZipFile(zipName)
    # x+x^2+x^3+x^4+x^n = x(x^n-1)/(x-1)
    s = len(alphabet)
    combinations = s * ((s**maxLen-1)//(s-1))

    count = 0

    userUpdate = "Cracking "+zipName+" with "+str(combinations)+" combinations. Press enter to begin!"
    input(userUpdate)

    lastPercentageComplete = -1

    for combLen in range (maxLen):
        for combination in itertools.product(alphabet,repeat=combLen+1):
            count += 1
            percentageComplete = round(count/combinations * 100,2)
            checkPass = pwStart + ''.join(combination) + pwEnd

            if '{0:.2f}'.format(percentageComplete) != '{0:.2f}'.format(lastPercentageComplete):
                # print cost a lot of time
                print('{0:.2f}'.format(percentageComplete) + '% done (current attempt: '+checkPass+')'+' ', end='\r')
                lastPercentageComplete = percentageComplete

            if extract(zFile, checkPass):
                print('Unzip successful!'+" "*20+'\n')
                print('Password is:')
                print(checkPass)
                return

main()
