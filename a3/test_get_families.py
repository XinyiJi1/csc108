import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):
    """example unittest test methods for get_families
    """

    def test_get_families_empty(self):
        """test empty set
        """
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        """test one perpson one friend different last name
        """
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_get_families_one_person_one_friend_sam_family(self):
        """test one perpson one friend same last name
        """        
        param = {'Jay Pritchett': ['Claire Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Claire', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_get_families_three_person_to_friends_sam_family(self):
        """test more peoplr more friend same last name
        """         
        param = {'Jay Pritchett': ['Claire Pritchett'], 'Gloria Pritchett':\
                 ['Manny Pritchett','Claire Pritchett'], 'Mitchell Pritchett': \
                 ['Cameron Pritchett', 'Gilbert Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Cameron', 'Claire', 'Gilbert', 'Gloria',\
                                  'Jay', 'Manny', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_get_families_three_person_to_friend_diff_family(self):
        """test more peoplr more friend different last name
        """        
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
                                   'Manny Delgado'], 'Claire Dunphy':\
                 ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
                 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', \
                                   'Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 'Dunphy': \
                    ['Claire', 'Luke', 'Phil'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_get_families_key_to_value(self):
        """test for fare that the situation of just include the value or the key
        """
        param = {'Jay Pritchett': ['Claire Dunphy', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)