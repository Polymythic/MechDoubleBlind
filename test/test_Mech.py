import unittest
import Mech

class TestMech(unittest.TestCase):
    '''
    Test class for Mech
    '''

    def test_setsmembervariables(self):
        testname = "TestMech"
        testtonnage = 10
        testmech = Mech.Mech(testname, testtonnage)
        self.assertEqual(testmech.name, testname)
        self.assertEqual(testmech.tonnage, testtonnage)

if __name__ == 'main':
    unittest.main()
