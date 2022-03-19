from src.values import Attribute, Bonus, AbilityScore
import unittest


class TestAttribute(unittest.TestCase):
    def setUp(self):
        self.att = Attribute(val=10, name='eac')
        self.att.bonuses = []

    def test_add_bonus(self):
        bonus = Bonus(val=1, name='test_bonus', target='eac', btype='inspiration')
        self.att.add_bonus(bonus)
        self.assertEqual([bonus], self.att.bonuses)

    def test_remove_bonus(self):
        bonus = Bonus(val=1, name='test_bonus', target='eac', btype='inspiration')
        self.att.add_bonus(bonus)
        self.assertEqual(len(self.att.bonuses), 1)
        self.att.remove_bonus_by_name('test_bonus')
        self.assertEqual(len(self.att.bonuses), 0)

    def test_adjustment(self):
        b1 = Bonus(val=1, name='test_bonus1', target='eac', btype='inspiration')
        self.att.add_bonus(b1)
        self.att.set_adjustments()
        self.assertEqual(self.att.adjustments, 1)

    def test_non_stacking_adjustment(self):
        b1 = Bonus(val=1, name='test_bonus1', target='eac', btype='inspiration')
        b2 = Bonus(val=2, name='test_bonus2', target='eac', btype='inspiration')
        for b in [b1,b2]:
            self.att.add_bonus(b)
        self.att.set_adjustments()
        self.assertEqual(self.att.adjustments, 2)

    def test_stacking_adjustment(self):
        b1 = Bonus(val=1, name='test_bonus1', target='eac', btype='inspiration', stacks=True)
        b2 = Bonus(val=2, name='test_bonus2', target='eac', btype='inspiration')
        for b in [b1,b2]:
            self.att.add_bonus(b)
        self.att.set_adjustments()
        self.assertEqual(self.att.adjustments, 3)

    def test_diff_bonus_types_adjustment(self):
        b1 = Bonus(val=1, name='test_bonus1', target='eac', btype='inspiration')
        b2 = Bonus(val=1, name='test_bonus2', target='eac', btype='armor')
        self.att.add_bonus(b1)
        self.att.add_bonus(b2)
        self.att.set_adjustments()
        self.assertEqual(self.att.adjustments, 2)


class TestAbilityScore(unittest.TestCase):
    def setUp(self):
        self.dex = AbilityScore(name='dex')
        self.dex.adjustments = 0
        self.dex.bonuses = []

    def test_mod_8(self):
        self.dex.val = 8
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, -1)

    def test_mod_9(self):
        self.dex.val = 9
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, 0)

    def test_mod_11(self):
        self.dex.val = 11
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, 0)

    def test_mod_12(self):
        self.dex.val = 12
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, 1)

    def test_mod_with_adjustments(self):
        b1 = Bonus(val=2, name='test_bonus1', target='dex', btype='inspiration')
        self.dex.val = 12
        self.dex.add_bonus(b1)
        self.dex.set_adjustments()
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, 2)

    def test_mod_with_negative_adjustments(self):
        b1 = Bonus(val=-2, name='test_bonus1', target='dex', btype='inspiration')
        self.dex.val = 12
        self.dex.add_bonus(b1)
        self.dex.set_adjustments()
        self.dex.calculate_mod()
        self.assertEqual(self.dex.mod, 0)


if __name__ == "__main__":
    unittest.main()