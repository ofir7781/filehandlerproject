import requests

from validationcheck.functionvalidationchecks import check_input_is_integer


INVALID_ARGS = "INVALID ARGUMENTS"
FALSE = "FALSE"
TRUE = "TRUE"
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def int_in_range( args_list ):
	result = INVALID_ARGS
	check_input_validation = all( check_input_is_integer( arg ) for arg in args_list )
	if len( args_list ) == 3 and check_input_validation:
		result = TRUE if int( args_list[ 2 ] ) >= int( args_list[ 0 ] ) and int( args_list[ 2 ] ) <= int( args_list[ 1 ] ) else FALSE
	return result


def get_pokemon_name( args_list ):
	result = INVALID_ARGS
	check_input_validation = all( check_input_is_integer( arg ) for arg in args_list )
	if len( args_list ) == 1 and check_input_validation:
		api_url = POKEMON_API_URL + args_list[ 0 ]
		response = requests.get( api_url ).json()
		result = response.get( "forms" )[ 0 ].get( "name" )
	return result.capitalize()


def get_pokemon_weight( args_list ):
	result = INVALID_ARGS
	if len( args_list ) == 1:
		api_url = POKEMON_API_URL + args_list[ 0 ].lower()
		response = requests.get( api_url ).json()
		result = response.get( "weight" )
	return result


def string_in( args_list ):
	result = INVALID_ARGS
	if len( args_list ) == 2:
		result = TRUE if args_list[ 1 ] in args_list[ 0 ] else FALSE
	return result


def list_of_ints_in_range( args_list ):
	result = TRUE
	bottom_range = args_list[ -2 ]
	top_range = args_list[ -1 ]
	args_list = args_list[ :-2 ]
	for arg in args_list:
		params = [ bottom_range, top_range ]
		if '[' in arg:
			arg = arg.replace( '[', '' )
		if ']' in arg:
			arg = arg.replace( ']', '' )
		params.append( arg )
		method_result = int_in_range( params )
		if method_result == FALSE:
			result = FALSE
			break
		if method_result == INVALID_ARGS:
			result = INVALID_ARGS
			break
	return result
