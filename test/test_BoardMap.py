import unittest
import BoardMap

class TestBoardMap(unittest.TestCase):
    '''
    Test class for BoardMap
    '''

    def test_setsmembervariables(self):
        testname = "BoardName"
        testboardmap = BoardMap.BoardMap(testname)
        self.assertEqual(testboardmap.map_name, testname)

if __name__ == 'main':
    unittest.main()