#Homework 2
#Author: Chris Spencer

import re
from tabulate import tabulate
import numpy
import matplotlib.pyplot
import pylab

print '\n\n\nHomework #2\n'
print 'Author: Chris Spencer\n\n'

print 'Question 1:\n'

#Pelvic Incidence
pel_inc = [] 
pel_inc_no = [] 
pel_inc_ab = []

#Pelvic Tilt
pel_tilt = [] 
pel_tilt_no = [] 
pel_tilt_ab = [] 

#Lumbar Lordosis Angle
ll_angle = [] 
ll_angle_no = [] 
ll_angle_ab = [] 

#Sacral Slope
s_slope = [] 
s_slope_no = [] 
s_slope_ab = []  

#Pelvic Radius
pel_rad = [] 
pel_rad_no = [] 
pel_rad_ab = [] 

#Degree Spondytolisthesis
deg_spon = [] 
deg_spon_no = [] 
deg_spon_ab = [] 

classAttrib = [] 

#mean calculations
for line in open('/home/chris/Documents/CSE581/HW2/Dataset/column_2C.dat', 'r'):
	item = line.rstrip()
	
	row = re.split(' ',item)

	pel_inc.append(float(row[0]))
	pel_tilt.append(float(row[1]))
	ll_angle.append(float(row[2])) 
	s_slope.append(float(row[3])) 
	pel_rad.append(float(row[4]))
	deg_spon.append(float(row[5]))
	classAttrib.append(row[6])

for index,item in enumerate(classAttrib):
	if classAttrib[index] == 'NO':
		pel_inc_no.append(pel_inc[index])
		pel_tilt_no.append(pel_tilt[index])
		ll_angle_no.append(ll_angle[index])
		s_slope_no.append(s_slope[index])
		pel_rad_no.append(pel_rad[index])
		deg_spon_no.append(deg_spon[index])
	elif classAttrib[index] == 'AB':
		pel_inc_ab.append(pel_inc[index])
		pel_tilt_ab.append(pel_tilt[index])
		ll_angle_ab.append(ll_angle[index])
		s_slope_ab.append(s_slope[index])
		pel_rad_ab.append(pel_rad[index])
		deg_spon_ab.append(deg_spon[index])
	else:
		print 'ERROR 1'

#Average Calculations
avg_pel_inc = float(sum(pel_inc)/len(pel_inc))
avg_pel_tilt = float(sum(pel_tilt)/len(pel_tilt))
avg_ll_angle = float(sum(ll_angle)/len(ll_angle))
avg_s_slope = float(sum(s_slope)/len(s_slope))
avg_pel_rad = float(sum(pel_rad)/len(pel_rad))
avg_deg_spon = float(sum(deg_spon)/len(deg_spon))

avg_pel_inc_no = float(sum(pel_inc_no)/len(pel_inc_no))
avg_pel_tilt_no = float(sum(pel_tilt_no)/len(pel_tilt_no))
avg_ll_angle_no = float(sum(ll_angle_no)/len(ll_angle_no))
avg_s_slope_no = float(sum(s_slope_no)/len(s_slope_no))
avg_pel_rad_no = float(sum(pel_rad_no)/len(pel_rad_no))
avg_deg_spon_no = float(sum(deg_spon_no)/len(deg_spon_no))

avg_pel_inc_ab = float(sum(pel_inc_ab)/len(pel_inc_ab))
avg_pel_tilt_ab = float(sum(pel_tilt_ab)/len(pel_tilt_ab))
avg_ll_angle_ab = float(sum(ll_angle_ab)/len(ll_angle_ab))
avg_s_slope_ab = float(sum(s_slope_ab)/len(s_slope_ab))
avg_pel_rad_ab = float(sum(pel_rad_ab)/len(pel_rad_ab))
avg_deg_spon_ab = float(sum(deg_spon_ab)/len(deg_spon_ab))

#Standard Deviation Calculations
std_pel_inc = numpy.std(pel_inc)
std_pel_tilt = numpy.std(pel_tilt)
std_ll_angle = numpy.std(ll_angle)
std_s_slope = numpy.std(s_slope)
std_pel_rad = numpy.std(pel_rad)
std_deg_spon = numpy.std(deg_spon)

std_pel_inc_no = numpy.std(pel_inc_no)
std_pel_tilt_no = numpy.std(pel_tilt_no)
std_ll_angle_no = numpy.std(ll_angle_no)
std_s_slope_no = numpy.std(s_slope_no)
std_pel_rad_no = numpy.std(pel_rad_no)
std_deg_spon_no = numpy.std(deg_spon_no)

std_pel_inc_ab = numpy.std(pel_inc_ab)
std_pel_tilt_ab = numpy.std(pel_tilt_ab)
std_ll_angle_ab = numpy.std(ll_angle_ab)
std_s_slope_ab = numpy.std(s_slope_ab)
std_pel_rad_ab = numpy.std(pel_rad_ab)
std_deg_spon_ab = numpy.std(deg_spon_ab)


#Median Calculations
med_pel_inc = numpy.median(pel_inc)
med_pel_tilt = numpy.median(pel_tilt)
med_ll_angle = numpy.median(ll_angle)
med_s_slope = numpy.median(s_slope)
med_pel_rad = numpy.median(pel_rad)
med_deg_spon = numpy.median(deg_spon)

med_pel_inc_no = numpy.median(pel_inc_no)
med_pel_tilt_no = numpy.median(pel_tilt_no)
med_ll_angle_no = numpy.median(ll_angle_no)
med_s_slope_no = numpy.median(s_slope_no)
med_pel_rad_no = numpy.median(pel_rad_no)
med_deg_spon_no = numpy.median(deg_spon_no)

med_pel_inc_ab = numpy.median(pel_inc_ab)
med_pel_tilt_ab = numpy.median(pel_tilt_ab)
med_ll_angle_ab = numpy.median(ll_angle_ab)
med_s_slope_ab = numpy.median(s_slope_ab)
med_pel_rad_ab = numpy.median(pel_rad_ab)
med_deg_spon_ab = numpy.median(deg_spon_ab)




avg_table = [
					['Name', 'All-AVG', 'Normal-AVG', 'Abnormal-AVG'],
					['Pelvic Incidence: ', avg_pel_inc, avg_pel_inc_no, avg_pel_inc_ab], 
					['Pelvic Tilt: ', avg_pel_tilt, avg_pel_tilt_no, avg_pel_tilt_ab], 
					['Lumbar Lordosis Angle: ', avg_ll_angle, avg_ll_angle_no, avg_ll_angle_ab], 
					['Sacral Slope: ', avg_s_slope, avg_s_slope_no, avg_s_slope_ab], 
					['Pelvic Radius: ', avg_pel_rad, avg_pel_rad_no, avg_pel_rad_ab], 
					['Degree Spondytolisthesis: ', avg_deg_spon, avg_deg_spon_no, avg_deg_spon_ab]
			]

stdev_table = [
					['Name', 'All-STDEV', 'Normal-STDEV', 'Abnormal-STDEV'],
					['Pelvic Incidence: ', std_pel_inc, std_pel_inc_no, std_pel_inc_ab], 
					['Pelvic Tilt: ', std_pel_tilt, std_pel_tilt_ab, std_pel_tilt_no], 
					['Lumbar Lordosis Angle: ', std_ll_angle, std_ll_angle_no, std_pel_tilt_ab], 
					['Sacral Slope: ', std_s_slope, std_s_slope_no, std_s_slope_ab], 
					['Pelvic Radius: ', std_pel_rad, std_pel_rad_no, std_pel_rad_ab], 
					['Degree Spondytolisthesis: ', std_deg_spon, std_deg_spon_no, std_deg_spon_ab]
			]

med_table = [
					['Name', 'All-Median', 'Normal-Median', 'Abnormal-Median'],
					['Pelvic Incidence: ', med_pel_inc, med_pel_inc_no, med_pel_inc_ab], 
					['Pelvic Tilt: ', med_pel_tilt, med_pel_tilt_ab, med_pel_tilt_no], 
					['Lumbar Lordosis Angle: ', med_ll_angle, med_ll_angle_no, med_pel_tilt_ab], 
					['Sacral Slope: ', med_s_slope, med_s_slope_no, med_s_slope_ab], 
					['Pelvic Radius: ', med_pel_rad, med_pel_rad_no, med_pel_rad_ab], 
					['Degree Spondytolisthesis: ', med_deg_spon, med_deg_spon_no, med_deg_spon_ab]
			]
print 'Part a:\n'
print 'i: Average\n'
print tabulate(avg_table, headers="firstrow"), '\n'
print 'ii: Standard Deviation\n'
print tabulate(stdev_table, headers="firstrow"), '\n'
print 'iii: Median\n'
print tabulate(med_table, headers="firstrow"), '\n'

classes_table = [
					['Classes:', ' Counts:'],
 					['Normal Count: ',  classAttrib.count('NO')],
					['Abnormal Count: ',  classAttrib.count('AB')]
 					#['Hernia Count: ',  classAttrib.count('DH')],
 					#['Spondylolisthesis Count: ', classAttrib.count('SL')]
				]

print tabulate(classes_table, headers="firstrow"), '\n'

print '\nQuestion 1 Part b: Scatter Plots'
print 'See RapidMiner for this one' 

#matplotlib.pyplot.scatter(pel_inc_no, pel_inc_ab)
#matplotlib.pyplot.scatter(pel_tilt_no, pel_tilt_ab)
#matplotlib.pyplot.scatter(ll_angle_no, ll_angle_no)

#matplotlib.pyplot.show()

print '\n\n'

print 'Question 1 Part c:'
print '\tSee document\n'

