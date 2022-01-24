from hiker import global_answer, Hiker,alphabet
import unittest


class TestHiker(unittest.TestCase):

    def test_global_function(self):
        self.assertEqual(54, global_answer())

    def test_instance_method(self):
        self.assertEqual(54, Hiker().instance_answer())



class alphabet_test():
    
    def test_tableau_class_should_return_alphabetList():
        self.assertEqual(tableauAlphabet, alphabet.tableau())
        
class index_test():
    def devrait_retourner_3_lettre_d():
        self.assertEqual(3, traitement(e).indice(e))

    
if __name__ == '__main__':
    unittest.main()  # pragma: no cover
    
