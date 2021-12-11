# PythonPDF
This tool contains a python-script, with which various operations with PDF-documents are possible, e.g. merge, extract, split and convert.

# Dependencies
   
    - PyPDF2

# Functions

            merge(doc_names, result_name)
Merges a list of documents in the given order and saves them as result_name.
    
    
            extract(doc_name, pages, result_name)
Extracts every page in list pages of file named doc_name and saves them as result_name.
    
    
            split(doc_name, page, result_names)
Splits document with name doc_name after given page and saves the resulting pds as result_names.
