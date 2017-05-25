import unittest
from languages.asp.ASPMapper import ASPMapper
from test.specialization.dlv.Cell import Cell



class ASPMapperTest(unittest.TestCase):

    def test(self):
        
        instance = ASPMapper.getInstance()
        
        try:
            instance.registerClass(Cell)
            
            object = instance.getObject("cell(1,2,5)")
        
            self.assertTrue(isinstance(object, Cell))
            
            self.assertEqual(1, object.getRow())
            
            self.assertEqual(2, object.getColumn())
            
            self.assertEqual(5, object.getValue())
            
            self.assertEqual("cell(1,2,5)", instance.getString(object))
            
            instance.unregisterClass(Cell)
            
            noneObject = instance.getObject("cell(1,2,5)")
            
            self.assertIsNone(noneObject)
            
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()