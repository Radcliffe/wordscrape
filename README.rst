Wordscrape
----------

This package contains utilities for extracting form data from Microsoft Word 2007 documents
with the `.docx` extension. It reads Check Box Form Fields and Text Form Fields, which are
both classified as legacy controls. Subsequent versions will support more kinds of controls.

Basic usage example:
   
    >>> from wordscrape import WordDocument
    >>> doc = WordDocument('form.docx')
    >>> data = doc.get_form_data()

The function `get_form_data` returns an `OrderedDict` containing all field names and values.

Wordscrape can read form data from multiple Word documents, and write the data to a single CSV
file, while ensuring that the field names match.

    >>> from wordscrape import WordDocument, read_dir, write_csv
    >>> path = '/temp/forms/'
    >>> all_data = read_dir(path)
    >>> write_csv(all_data, 'report.csv')
    
The function `all_data` returns a list of ordered dictionaries, and the function `write_csv`
writes the data to a CSV file with a header row.