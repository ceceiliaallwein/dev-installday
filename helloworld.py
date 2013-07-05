# Hello World in Python -- Install day 12/17/12
print "Hello World!"


#-------------------------------------------------------------
#EXERCISE 2.1

#header
print ""
print "EXERCISE 2.1 - see script" 

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
width = 17 				#exp 1
height = 12.0			#exp 2
delimiter = '.'			#exp 3
formula = 1+2*5			#exp 4

#statements 
print width/2			#int
print width/2.0  		#float
print height/3			#float
print 1+2*5				#int / expression 
print delimiter*5		#statement / str operation 


#-------------------------------------------------------------
#EXERCISE 2.4.1

#header
print ""
print "EXERCISE 2.4.1"
import math

#assignments
radius = 5

#statements
print ((radius**3)*math.pi*4)/3		#volume of a sphere 	


#-------------------------------------------------------------
#EXERCISE 2.4.2 

#header
print ""
print "EXERCISE 2.4.2"

#assignments 
cov_price = 24.95					#full price 
disc = .6							#40% discount
ship_first = 3.0					#shipping for first book 
ship_add = .75						#shipping for each add'l book 
wh_price = cov_price*disc			#wholesale price after discount

#statements 
print ((wh_price+ship_first)+((wh_price+ship_add)*59))	#wholesale cost of 60 books


#-------------------------------------------------------------
#EXERCISE 2.4.3

#header 
print ""
print "EXERCISE 2.4.3"

#assignments
pace_easy = 8.25					#warmup pace
pace_tempo = 7.2 					#training
dist_easy = 2 						#two miles 
dist_tempo = 3						#three miles
time_st = 6*60+52					#time = six fifty two am 
dur_easy = dist_easy*pace_easy		#duration of easy run	
dur_tempo = dist_tempo*pace_tempo	#duration of tempo run

#statements 
print (time_st+dur_easy+dur_tempo)/60

#-------------------------------------------------------------
#EXERCISE 3.1

#header
print ""
print "EXERCISE 3.1 - script commented out"

#functions 
#repeat_lyrics()

#definitions
#def print_lyrics():
#	print "I'm a lumberjack, and I'm okay."
#	print "I sleep all night, and I work all day."

#def repeat_lyrics():
#	print_lyrics
#	print_lyrics

#error message
print "'repeat_lyrics' is not defined"


#-------------------------------------------------------------
#EXERCISE 3.2 
#header
print ""
print "EXERCISE 3.2 - script commented out"

#definitions  
#def repeat_lyrics():
#	print_lyrics
#	print_lyrics

#def print_lyrics():
#	print "I'm a lumberjack, and I'm okay."
#	print "I sleep all night, and I work all day."

#functions
#repeat_lyrics()

#error message
print "'repeat_lyrics' is not defined" 


#-------------------------------------------------------------
#EXERCISE 3.3
#header
print ""
print 'EXERCISE 3.3'

#assignments 
s = 'allen'
space = ' '

#statements 
padding = space * (70 - (len('allen'))) 

#functions
def right_justify(s):
	print padding + s

right_justify(s)


#-------------------------------------------------------------
#EXERCISE 3.4 


#header
print ""
print "EXERCISE 3.4"


#function
def do_twice(f):			#defining function, function object as arguement 
	f()						#calling function object 2x 
	f()						#no arguement

def print_spam (): 			#defining first function, no arguement
	print 'spam' 			

do_twice(print_spam)
print ""


#function
def do_twice(f, arg):			#exercise 3.4.2
	f(arg)
	f(arg)

def print_twice(arg):			#exercise 3.4.3
	print arg
	print arg

do_twice(print_twice, 'spam')	#exercise 3.4.4
print ""


#function
def do_four(f, arg):			#exercise 3.5.5
	do_twice(f, arg)
	do_twice(f, arg)


do_four(print_twice, 'spam')	#prints 8 spams (2*2*2 or do*print*do)
print ""


#-------------------------------------------------------------
#EXERCISE 3.5.1 

#header 
print ""
print "EXERCISE 3.5"


#assignments 
j_block = '+'								#joint
v_block = '|'								#vertical building block
h_block = ' -'								#horizontal building block
space_bm = ' '								#beginning or ending space	
space_wh = ' '*12 							#white space between pillars 
h_seg = (h_block + space_bm)*4 				#horizontal segment between joints 
beam_h = ((j_block + h_seg)*2)+j_block		#complete horizontal layer
beam_v = ((v_block + space_wh)*2)+v_block	#complete vertical layer 
beam_h_lg = ((j_block + h_seg)*2)			#removes closing joint for incremental scaling
beam_v_lg = ((v_block + space_wh)*2)		#removes closing pillar for incremental scaling 

#test
print ""
print "grid - alignment test"				#checks assignments for accuracy
print beam_h								 
print beam_v
print ""


#function header 
print ""
print "grid - 2x2"							#labels the return from the following function call 

#functions 
def print_grid (arg1, arg2):				#orders the printing of segments 
	print arg1
	print_four(arg2)
	print arg1
	print_four(arg2)
	print arg1

def print_four(arg):						#automates the repeated task of multiple pillar segments 
	print arg
	print arg
	print arg
	print arg

print_grid(beam_h, beam_v)				#calls the function sequence with the variables in assignments
print ""										#tip: keep the args abstract until the actual call 


#-------------------------------------------------------------
#EXERCISE 3.5.2 


#function header 
print ""
print "grid - 4x4"

#functions 
def print_large (arg1, arg2, arg3, arg4):			#scales the grid vertically
	print_grid2 (arg1, arg2, arg3, arg4)
	print_grid2 (arg1, arg2, arg3, arg4)
	print arg1+arg1+arg3							#adds the bottom edge

def print_grid2 (arg1, arg2, arg3, arg4):			#unlike 3.5.1 this omits the bottom edge
	print_one (arg1+arg1+arg3)						#this accommodates repeated functions w/o duplicating material
	print_four(arg2+arg2+arg4)						#arithmetic adds additional elements 
	print_one (arg1+arg1+arg3)
	print_four(arg2+arg2+arg4)					

def print_four(arg):
	print arg
	print arg
	print arg
	print arg

def print_one(arg):
	print arg

print_large(beam_h_lg, beam_v_lg, j_block, v_block)
print ""


















