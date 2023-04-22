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
import tabula

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
        information = reader.metadata
        number_of_pages = len(information)
        pages = reader.pages
        data = ''
        for page in reader.pages:
            data += page.extract_text() + '\n'

    # txt = f"""
    # Information about {pdf_path}: 

    # Author: {information.author}
    # Creator: {information.creator}
    # Producer: {information.producer}
    # Subject: {information.subject}
    # Title: {information.title}
    # Number of pages: {number_of_pages}
    # """
    
    return data

def export_to_file(_f, _s):
    text_file = open(_f, "w")
    n = text_file.write(_s)
    text_file.close()

if __name__ == '__main__':
    path = 'statements/06-0665-0410557-00_Statement_2023-03-09.pdf'
    data = extract_information(path)
    export_to_file('outputs/text', data)
