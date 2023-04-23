# for python3 & macos m1, sudo pip3 install PyPDF2
# for python3 & macos m1, sudo pip3 install tabula.py
# install python3
# install Java
# Error from tabula-java:
# The operation couldn’t be completed. Unable to locate a Java Runtime.
# Please visit http://www.java.com for information on installing Java.

import pandas as pd 
import csv
from PyPDF2 import PdfReader
from datetime import datetime
from DATA_CONSTANTS import *
import re

# def import_all_to_csv(_filename, _dfs):
#     """import entries' data into a csv file
#     """

#     f = open('derp' + '.csv', 'w', newline='')
#     columns = ['Entry Name','Interface','Target Int', 'Address', 'Target Addr', 'From Device','To Device', 'admin group']
#     writer = csv.writer(f)
#     writer.writerow(columns)
#     for name, data in config['entries'].items():
#         entry_name = name
#         int_name = data['int_name']
#         target_interface = data['target_interface']
#         int_addr = data['int_addr']
#         target_addr = data['target_addr']
#         origin_device = data['origin_device']
#         target_device = data['target_device']
#         admin_group = data['admin_group']
#         row = [
#             entry_name,
#             int_name,
#             target_interface,
#             int_addr,
#             target_addr,
#             origin_device,
#             target_device,
#             admin_group
#             ]
#         writer.writerow(row)
    
#     #data frame
#     f.close()
#     r = pd.read_csv(config['output_path']+ config['file_name'] + '.csv')
#     print(r)


def import_to_excel(_f, _dfs):
    """import entries' data into a xlxs file
    """
    # debug_log('import_all_to_excel', 'importing')
    f = _f + '.xlsx'
    columns = ['Interface','Address','From Device','To Device', 'Target', 'Admin Group']
    
    #data frame
    df = pd.DataFrame(_dfs,columns= list[1])
    df.to_excel(_f, sheet_name='unnamed_sheet')
    # debug_log('import_all_to_excel', df)


def tabula():

    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf("statements/06-0665-0410557-00_Statement_2023-03-09.pdf", pages='all')
    print(dfs)
    import_to_excel('input', dfs)
    # Read remote pdf into list of DataFrame
    # dfs2 = tabula.read_pdf("statements/06-0665-0410557-00_Statement_2023-03-09")

    # convert PDF into CSV file
    # tabula.convert_into(dfs, "output.csv", output_format="csv", pages='all')

    # convert all PDFs in a directory
    # tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        # information = reader.metadata
        # number_of_pages = len(information)
        pages = reader.pages
        content = ''
        for page in reader.pages:
            content += page.extract_text() + '\n'

    # Get Statement Period
    statement_period = ()
    statement_period = get_statement_period(content)
    
    # Define the pattern to search for (eg. 10 Dec Openingbalance 8,046.33)
    pattern = r"\d+\s\w+\s[\w\s]+\s\d"

    # Search for the pattern in the string
    matches = re.findall(pattern, content)

    for match in matches:
        print(match)

    return data


def get_statement_period(_content):
    # get statement period
    statement_period = getSubstringBetweenTwoChars('Statementperiod ', '\n', _content)

    # get start date
    start_date = statement_period.split(' -')[0]
    start_date = convert_date(start_date)

    # get end date
    end_date = statement_period.split('- ')[1]
    end_date = convert_date(start_date)

    # return a tuple
    statement_period = (start_date, end_date)
    return statement_period


def convert_date(date_str):
    # Parse the input date string
    date = datetime.strptime(date_str, "%d %b %Y")

    # Convert the date to the desired format
    new_date_str = date.strftime("%y-%m-%d")

    return new_date_str


def getSubstringBetweenTwoChars(ch1,ch2,_str):
    """useful function to get substring between 2 different given chars
    Args:
        ch1 (str): 1st given character
        ch2 (str): 2nd given character
        _str (str): given string
    Returns:
        str: substring between the 2 chars
    """
    return _str.split(ch1)[1].split(ch2)[0]

def export_to_file(_f, _s):
    text_file = open(_f, "w")
    n = text_file.write(_s)
    text_file.close()

def has_date_been_checked(_date_str):
    # if(_date_str in MONTH_YEAR_CHECKED):
    #     return True
    # else:
    #     return False
    pass

def is_date_valid(_date_str):
    # Convert the input string to a datetime object
    try:
        date = datetime.strptime(_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date!")
        return False
    else:
        # Check if the year, month, and day are valid
        if date.year < 1 or date.month < 1 or date.month > 12 or date.day < 1 or date.day > 31:
            print("Impossible date!")
            return False
        elif date.month in [4, 6, 9, 11] and date.day > 30:
            print("Impossible date!")
            return False
        elif date.month == 2 and date.day > 29:
            print("Impossible date!")
            return False
        elif date.month == 2 and date.day == 29 and not (date.year % 4 == 0 and (date.year % 100 != 0 or date.year % 400 == 0)):
            print("Impossible date!")
            return False
        else:
            print("Valid date!")
            return True
        
    

if __name__ == '__main__':
    folder = 'statements'
    path = folder + '/' + '06-0665-0410557-00_Statement_2023-03-09.pdf'
    data = extract_information(path)
    export_to_file('outputs/text', data)

