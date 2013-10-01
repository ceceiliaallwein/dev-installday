# Exercises for chapter 3:

# Name: Ceceilia Allwein 
# github: ceceiliaallwein


#-------------------------------------------------------------
#EXERCISE 3.1

#header
print ""
print "EXERCISE 3.1 - script comments"

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
print "EXERCISE 3.2 - see comments"

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

#output
right_justify(s)


#-------------------------------------------------------------
#EXERCISE 3.4 


#header
print ""
print "EXERCISE 3.4"


#function
def do_twice(f):
	f()
	f()

def print_spam (): 
	print 'spam' 			

#output
do_twice(print_spam)
print ""


#functions - exercise 3.4.2 and 3.4.3
def do_twice(f, arg):							
	f(arg)
	f(arg)

def print_twice(arg):
	print arg
	print arg

#output - exercise 3.4.4
do_twice(print_twice, 'spam')					
print ""


#functions - exercise 3.5.5
def do_four(f, arg):							
	do_twice(f, arg)
	do_twice(f, arg)

#output - prints 8 spams 
do_four(print_twice, 'spam')					
print ""


#-------------------------------------------------------------
#EXERCISE 3.5.1 

#header 
print ""
print "EXERCISE 3.5"


#assignments 
j_block = '+'									#joint
v_block = '|'									#vertical building block
h_block = ' -'									#horizontal building block
space_bm = ' '									#beginning or ending space	
space_wh = ' '*12 								#white space between pillars 
h_seg = (h_block + space_bm)*4 					#horizontal segment between joints 
beam_h = ((j_block + h_seg)*2)+j_block			#complete horizontal layer
beam_v = ((v_block + space_wh)*2)+v_block		#complete vertical layer 
beam_h_lg = ((j_block + h_seg)*2)				#removes closing joint for incremental scaling
beam_v_lg = ((v_block + space_wh)*2)			#removes closing pillar for incremental scaling 

#test - checks assignments for accuracy 
print ""
print "grid - alignment test"
print beam_h								 
print beam_v
print ""


#header
print ""
print "grid - 2x2"		

#functions 
def print_grid (arg1, arg2):
	print arg1
	print_four(arg2)
	print arg1
	print_four(arg2)
	print arg1

def print_four(arg):						 
	print arg
	print arg
	print arg
	print arg

#output
print_grid(beam_h, beam_v)	
print ""									


#-------------------------------------------------------------
#EXERCISE 3.5.2 


#header 
print ""
print "grid - 4x4"

#functions 
def print_large (arg1, arg2, arg3, arg4):		#scales the grid vertically
	print_grid2 (arg1, arg2, arg3, arg4)
	print_grid2 (arg1, arg2, arg3, arg4)
	print arg1+arg1+arg3						#adds the bottom edge

def print_grid2 (arg1, arg2, arg3, arg4):		#unlike 3.5.1 this omits the bottom edge
	print_one (arg1+arg1+arg3)					#accommodates repeated functions w/o duplicating material
	print_four(arg2+arg2+arg4)					#arithmetic adds additional elements 
	print_one (arg1+arg1+arg3)
	print_four(arg2+arg2+arg4)					

def print_four(arg):
	print arg
	print arg
	print arg
	print arg

def print_one(arg):
	print arg

#output
print_large(beam_h_lg, beam_v_lg, j_block, v_block)
print ""