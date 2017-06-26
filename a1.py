""" ASSIGNMENT 1- CSE 101 - INTRODUCTION TO PROGRAMMING
Task 1
Neelabhro Roy -2016171
Dewangee Agarwal-2016034"""

"""The function we have defined below,uses the output generated online with the help
of the document provided to us,
and then converts it into JSON form,which we further convert to the string form.
We have also 'called' the functions defined and described in the subsequent parts, in Part A."""


#Part A
from urllib.request import *
def exchange (currency_from, currency_to, amount_from):
	#we are calling the function
	#jss:json string
	jss=currency_response(currency_from, currency_to, amount_from)
	check=has_error(jss)
	#we have converted the json form into a string
	q=str(jss)
	if(check==True):
		return -1
	else:
		return (before_space (q))

def currency_response(currency_from, currency_to, amount_from):
	zup= 'http://cs1110.cs.cornell.edu/2015fa/a1server.php?'
	l=zup+'from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)
	t=urlopen(l)
	j=t.read().decode()
	return j


"""We have already obtained the JSON string, in this part, we check if the value we have input has any kind of error associated with it,
(an improper value or possibly a wrong data type.)
so that proper rectification and perfection could be done/achieved."""

#Part B
def has_error(j):
	v=str(j)
	if v.find("false")>0 :
		return True
	else:
		return False

"""We bring string slicing into use in this part, and is the final part of the program."""

#Part C
def before_space(r):
	x=str(r[(r.find('rhs'))+8:r.find('valid')-4])	
	var=x[:x.find(" ")]
	y=float(var)
	return (y)

if __name__ == '__main__':
	a=input('Enter the currency to be converted:')
	b=input('Enter the currency to be converted to:')
	amt=input('Enter the amount to be converted:')
	ch=exchange(a,b,amt)
	print (ch)

		