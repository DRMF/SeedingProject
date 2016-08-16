
__author__ = 'Edward Bian'
__status__ = 'Development'

from unittest import TestCase
from updateChapters import new_keywords
from updateChapters import extraneous_section_deleter
from updateChapters import cut_words

class TestNewKeywords(TestCase):

    def test_new_keywords(self):
        self.assertEquals(new_keywords(['\\subsubsection*{ThisIsATest}\n'],[]), ['ThisIsATest', 'Limit Relation'])


class TestExtraneousSectionDeleter(TestCase):

    def test_extraneous_section_deleter(self):
        self.assertEquals(extraneous_section_deleter(['reference', 'bananas', 'limit relation', '458673',
            'limit relations', 'apple']), ['bananas', '458673', 'apple'])


class TestCutWords(TestCase):

    def test_cut_words(self):
        self.assertEquals(cut_words('MoreWords','WordsAndSomeMoreWords'), 'WordsAndSome')
        self.assertEquals(cut_words('SupposedToFail', 'WordsAndSomeMoreWords'), 'WordsAndSomeMoreWords')
        self.assertEquals(cut_words('StuffFromAddenum', '''\\paragraph{\\large\\bf KLSadd: TestCase}StuffFromAddenum\\begin{equation}\\end{equation}'''),
                                                        '''\\begin{equation}\\end{equation}''')