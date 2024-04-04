import csv
import unittest

class TestCSVFile(unittest.TestCase):
    def setUp(self):
        with open('developers.csv', 'r') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)

    def test_csv_file(self):
        self.assertTrue(self.data)  # Sjekkar at fila ikkje er tom
        self.assertIn('language', self.data[0])  # Sjekkar at 'language' er ei av kolonnene

    def test_specific_languages(self):
        languages = {row['language'] for row in self.data}
        self.assertIn('Python', languages)
        self.assertIn('JS', languages)
        # self.assertIn('Java', languages)  # Vil feile

    def test_unexpected_language_value(self):
        expected_languages = {'Python', 'JS', 'Java', 'HTML', 'C', 'Scratch', 'Ruby', 'Go', 'Swift', 'PHP'}
        for row in self.data:
            self.assertIn(row['language'], expected_languages)

    # NB: Denne testen vil aldri feile, dersom ikkje det er fleire felt i fila enn berre språk, t.d. namn foran språk
    # Grunnen til dette er at csv.DictReader automatisk ignorerer rader som ikkje har nokon verdi
    def test_non_empty_languages(self):
        for row in self.data:
            self.assertTrue(row['language'].strip())  # Sjekkar at språket ikkje er ein tom streng

if __name__ == '__main__':
    unittest.main()