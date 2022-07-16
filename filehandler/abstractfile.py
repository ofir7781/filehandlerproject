from abc import ABC, abstractmethod


class AbstractFile( ABC ):

	@abstractmethod
	def create_output( self, file, file_name ):
		pass
