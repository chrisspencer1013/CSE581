#Homework 2 Question 2
#remember to use python 2.7 for openpyxl (required?)

import re
import openpyxl
from collections import Counter 

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
		if nextWord.lower() not in ('a', 'it', 'that', 'an', 'you', 'your', 'i', 'of', 'had', 'has', 'and', 'or', 'is', 'this', 'the', 'was', 'in', 'to', 'too', 'so', 'for'):
			nextWord = nextWord.strip(',')
			nextWord = nextWord.strip('.')
			nextWord = nextWord.strip('!')
			clean_lines.append(nextWord.lower())


counts = Counter(clean_lines)

#counter works as a dictionary, so this works
for key, value in counts.items():
	print key, value
