import os

from functions import functionscollection
from filehandler.abstractfile import AbstractFile


class TextFileHandler( AbstractFile ):

	def create_output( self, file, file_name ):
		output_file = open( file_name, "w" )
		valid_funations_names_list = [ name for name, val in functionscollection.__dict__.items() if callable( val ) ]
		if os.stat( file ).st_size > 0:
			self.__parse_file_and_execute_every_line( file, valid_funations_names_list, output_file )
		else:
			output_file.write( "EMPTY INPUT FILE\n" )
		output_file.close()

	def __convert_file_line_to_list_of_str( self, file_line ):
		file_line_as_list = file_line.split( "," )
		file_line_as_list[ -1 ].replace( '\n', '' )
		file_line_as_list = [ arg.replace( '"', '' ) if arg.__contains__( '"' ) else arg for arg in file_line_as_list ]
		return [ arg.strip() for arg in file_line_as_list ]

	def __parse_file_and_execute_every_line( self, file, valid_funations_names_list, output_file ):
		with open( file ) as input_file:
			for line in input_file:
				file_line_as_list = self.__convert_file_line_to_list_of_str( line )
				if file_line_as_list[ 0 ] not in valid_funations_names_list:
					output_file.write( "INVALID FUNCTION\n" )
				else:
					func_name = file_line_as_list[ 0 ]
					func = getattr( functionscollection, func_name )
					func_result = func( file_line_as_list[ 1: ] )
					output_file.write( f'{func_result}\n' )
