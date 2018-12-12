import unittest
import BoardCell

class TestBoardCell(unittest.TestCase):
    '''
    Test Class for Board Cell
    '''

    def test_setsmembervariables(self):
        testtype = "LIGHT_WOODS"
        testcell = BoardCell.BoardCell(testtype)
        self.assertEqual(testcell.cell_type, testtype)

if __name__ == 'main':
    unittest.main()