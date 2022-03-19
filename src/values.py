

class Bonus:
    def __init__(self, val=0, name='', target='', btype='', stacks=False):
        self.val = val
        self.name = name
        self.target = target
        self.stacks = stacks
        self.btype = btype


class Attribute:
    def __init__(self, val=0, adjustments=0, name='', bonuses=[]):
        self.val = val
        self.adjustments = adjustments
        self.name = name
        self.bonuses = bonuses

    def add_bonus(self, bonus):
        if bonus.target == self.name:
            self.bonuses.append(bonus)

    def remove_bonus_by_name(self, bonus_name):
        self.bonuses = [bonus for bonus in self.bonuses if bonus.name != bonus_name]

    def set_adjustments(self):
        adjustments = 0
        btypes = {}
        for bonus in self.bonuses:
            if bonus.stacks:
                adjustments += bonus.val
            elif bonus.btype not in btypes:
                adjustments += bonus.val
                btypes[bonus.btype] = bonus.val
            elif btypes[bonus.btype] < bonus.val:
                adjustments -= btypes[bonus.btype]
                adjustments += bonus.val
                btypes[bonus.btype] = bonus.val
        self.adjustments = adjustments


class AbilityScore(Attribute):
    def __init__(self, val=10, adjustments=0, name=''):
        super().__init__(val, adjustments, name)
        self.mod = 0

    def calculate_mod(self):
        self.mod = int((self.val + self.adjustments - 10) / 2)


