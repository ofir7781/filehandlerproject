import os
import sys

from filehandler import textfilehandler, jsonfilehandler


def check_file_and_perform_action( file, file_number ):
    file_name = f'outputfiles/output_result_{file_number}'
    if os.path.exists( file ):
        if file.endswith( ".txt" ):
            textfilehandler.TextFileHandler().create_output( file, file_name )
        elif file.endswith( ".json" ):
            jsonfilehandler.JsonFileHandler().create_output( file, file_name )
    else:
        with open( file_name, 'w' ) as f:
            f.write( f'File: {file} does not exist\n' )


if __name__ == '__main__':
    file_number = 1
    for file in sys.argv[ 1: ]:
        check_file_and_perform_action( file, file_number )
        file_number += 1
