from unittest import TestCase

from wordscrape import WordDocument, write_csv
from collections import OrderedDict

class TestWordscrape(TestCase):
    def test_get_form_data(self):
        doc = WordDocument('wordscrape/tests/sampledocs/Absence request form-David.docx')
        formdata = doc.get_form_data()
        approve_date = formdata['ApproveDate']
        self.assertEqual(approve_date, '11/13/15')