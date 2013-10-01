# Exercises for chapter 2:

# Name: Ceceilia Allwein
# github: ceceiliaallwein 

#-------------------------------------------------------------
#EXERCISE 2.1

#header
print ""
print "EXERCISE 2.1 - see comment" 

#only digits zero to seven are recognized in the octal system
#nine is not recognized 
#this is a semantic error 


#EXERCISE 2.2
print ""
print "EXERCISE 2.2"
print 5 
x = 5
print x+1

#-------------------------------------------------------------
#EXERCISE 2.3

#header
print ""
print "EXERCISE 2.3"
print "see script for value type"

#assignments 
width = 17 										#exp 1
height = 12.0									#exp 2
delimiter = '.'									#exp 3
formula = 1+2*5									#exp 4

#statements 
print width/2									#int
print width/2.0  								#float
print height/3									#float
print 1+2*5										#int / expression 
print delimiter*5								#statement / str operation 


#-------------------------------------------------------------
#EXERCISE 2.4.1

#header
print ""
print "EXERCISE 2.4.1"
import math

#assignments
radius = 5

#statements
print ((radius**3)*math.pi*4)/3					#volume of a sphere 	


#-------------------------------------------------------------
#EXERCISE 2.4.2 

#header
print ""
print "EXERCISE 2.4.2"

#assignments 
cov_price = 24.95								#full price 
disc = .6										#40% discount
ship_first = 3.0								#shipping for first book 
ship_add = .75									#shipping for each add'l book 
wh_price = cov_price*disc						#wholesale price after discount

#statements 
print ((wh_price+ship_first)+((wh_price+ship_add)*59))	#wholesale cost of 60 books


#-------------------------------------------------------------
#EXERCISE 2.4.3

#header 
print ""
print "EXERCISE 2.4.3"

#assignments
pace_easy = 8.25								#warmup pace
pace_tempo = 7.2 								#training
dist_easy = 2 									#two miles 
dist_tempo = 3									#three miles
time_st = 6*60+52								#time = six fifty two am 
dur_easy = dist_easy*pace_easy					#duration of easy run	
dur_tempo = dist_tempo*pace_tempo				#duration of tempo run

#statements 
print (time_st+dur_easy+dur_tempo)/60