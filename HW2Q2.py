#Homework 2 Question 2
#remember to use python 2.7 for openpyxl (required?)

import re
import openpyxl
from collections import Counter 
from tabulate import tabulate
from scipy import spatial

wb = openpyxl.load_workbook('/home/chris/CSE581/textcorpus.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')

raw_lines = []
clean_lines = []

#plan: strip down to words in a list, clean out BS, use counts function, the go for weighting

#read in lines from sheet
for x in range(1,31):
	raw_lines.append(sheet.cell(row=x, column=1).value)

for x in range(0,30):
	nextLine = raw_lines[x].split()

	for nextWord in nextLine:
		if nextWord.lower() not in ('a', 'it', 'me', 'that', 'an', 'you', 'your', 'i', 'of', 'had', 'has', 'and', 'or', 'is', 'this', 'the', 'was', 'in', 'to', 'too', 'so', 'for'):
			nextWord = nextWord.strip(',')
			nextWord = nextWord.strip('.')
			nextWord = nextWord.strip('!')
			clean_lines.append(nextWord.lower())


counts = Counter(clean_lines)
keys = []
values = []

#counter works as a dictionary, so this works 
for key, value in counts.items():
	keys.append(key)
	values.append(value)
	print key, value


	
cos_12 = 1 - spatial.distance.cosine(clean_lines[1], clean_lines[2])
cos_23 = 1 - spatial.distance.cosine(clean_lines[2], clean_lines[3])
cos_34 = 1 - spatial.distance.cosine(clean_lines[3], clean_lines[4])
cos_45 = 1 - spatial.distance.cosine(clean_lines[4], clean_lines[5])

print 'Cosine Simularity from 1 to 2: ', cos_12
print 'Cosine Simularity from 2 to 3: ', cos_23
print 'Cosine Simularity from 3 to 4: ', cos_34
print 'Cosine Simularity from 4 to 5: ', cos_45