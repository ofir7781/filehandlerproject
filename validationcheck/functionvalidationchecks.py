
def check_input_is_integer( input ):
	result = True
	try:
		int( input )
	except ValueError:
		result = False
	return result
