'''
Need: to read from_date and to_date from metadata file
'''

import os, sys
from finance_complaint.exception import FinanceException


class DataIngestionMetaData:

    def __init__(self, metadata_file_path):
        self.metadata_file_path = metadata_file_path


    def is_metadata_file_present(self):
        return os.path.exists(self.metadata_file_path)

    def write_metadata_info(self, from_date: string, to_date: string):
        try:
            pass

        except Exception as ex:
            raise FinanceException(e, sys)



    def get_metadata_info(self, from_date: string, to_date: string):
        try:
            pass

        except Exception as ex:
            raise FinanceException(e, sys)
            
