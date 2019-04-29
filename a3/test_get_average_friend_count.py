import unittest
import network_functions

class TestGetAverageFriendCount(unittest.TestCase):
    """Excample unittest test methods for get_average_friend_count
    """

    def test_get_average_empty(self):
        """test empty set
        """
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_average_one_person_one_friend(self):
        """test one person one friend
        """
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
   
    def test_get_average_one_person_three_friend(self):
        """test one person more friends
        """
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']}
        actual = network_functions.get_average_friend_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
   
    def test_get_average_three_person_same_number_of_friend(self):
        """test more people same freinds
        """
        param = {'Jay Pritchett': ['Luke Dunphy', 'Claire Dunphy'], \
                 'Claire Dunphy': ['Mitchell Pritchett', 'Phil Dunphy'], \
                 'Gloria Pritchett': ['Cameron Tucker', 'Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)      
    
    def test_get_average_three_person_divided_different_number_of_friend(self):
        """test more people deifferent friends that can be devided
        """
        param = {'Jay Pritchett': ['Luke Dunphy', 'Claire Dunphy'], \
                 'Claire Dunphy': ['Alex Dunphy', 'Mitchell Pritchett', \
                                   'Phil Dunphy', 'Dylan D-Money'], \
                 'Gloria Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
                                      'Luke Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
    
    def test_get_average_three_person_undevided_different_number_of_friend(self):
        """test more people deifferent friends that can not be devided
        """        
        param = {'Jay Pritchett': ['Luke Dunphy', 'Claire Dunphy'], \
                 'Claire Dunphy': ['Alex Dunphy', 'Mitchell Pritchett'], \
                 'Gloria Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
                                      'Luke Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 7/3
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)      

if __name__ == '__main__':
    unittest.main(exit=False)