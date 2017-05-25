import unittest
from languages.pddl.PDDLMapper import PDDLMapper
from unitTests.specialization.solver_planning_domains.PickUp import PickUp


class PDDLMapperTest(unittest.TestCase):

    def test(self):
        
        instance = PDDLMapper.getInstance()
        
        try:
            instance.registerClass(PickUp)
            
            object = instance.getObject("(pick-up b)")
        
            self.assertTrue(isinstance(object, PickUp))
            
            self.assertEqual("b", object.getBlock())
            
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()