from src.values import Attribute, Bonus, AbilityScore
import unittest


class TestAttribute(unittest.TestCase):
    def setUp(self):
        self.attribute = Attribute(val=10, name='eac')

    def test_add_bonus(self):
        bonus = Bonus(val=1, name='test_bonus', target='eac', source='inspiration')
        self.attribute.add_bonus(bonus)
        self.assertEqual([bonus], self.attribute.bonuses)

    def test_remove_bonus(self):
        self.attribute.remove_bonus_by_name('test_bonus')
        self.assertEqual([], self.attribute.bonuses)

    def test_adjustment(self):
        b1 = Bonus(val=1, name='test_bonus1', target='eac', source='inspiration')
        b2 = Bonus(val=1, name='test_bonus2', target='eac', source='armor')
        self.attribute.add_bonus(b1)
        self.attribute.add_bonus(b2)
        self.attribute.set_adjustments()
        self.assertEqual(self.attribute.adjustments, 2)


class TestAbilityScore(unittest.TestCase):
    def setUp(self):
        self.abs = AbilityScore(val=10, name='eac')



if __name__ == "__main__":
    unittest.main()