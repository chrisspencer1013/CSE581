#Homework 2
#Author: Chris Spencer
import re
from tabulate import tabulate

#import statistics
print '\n\t\tHomework #2\n'
print '\t\tAuthor: Chris Spencer\n\n'

print 'Question 1:'
print '\t Part a:'
print '\t\t Part i:'


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

average_table = [
		['Name', 'Total Average', 'Normal Average', 'Abnormal Average'],
		['Pelvic Incidence: ', avg_pel_inc, avg_pel_inc_no, avg_pel_inc_ab], 
		['Pelvic Tilt: ', avg_pel_tilt, avg_pel_tilt_no, avg_pel_tilt_ab], 
		['Lumbar Lordosis Angle: ', avg_ll_angle, avg_ll_angle_no, avg_ll_angle_ab], 
		['Sacral Slope: ', avg_s_slope, avg_s_slope_no, avg_s_slope_ab], 
		['Pelvic Radius: ', avg_pel_rad, avg_pel_rad_no, avg_pel_rad_ab], 
		['Degree Spondytolisthesis: ', avg_deg_spon, avg_deg_spon_no, avg_deg_spon_ab]
	]

print tabulate(average_table, headers="firstrow")

print 'Classes:'
print '\tNormal Count: ',  classAttrib.count('NO')
print '\tAbnormal Count: ',  classAttrib.count('AB')
print '\tHernia Count: ',  classAttrib.count('DH')
print '\tSpondylolisthesis Count: ', classAttrib.count('SL')






