from classes.pet import Pet


class Fox(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, 'fox', tricks)

    def noise(self):
        print('Hmm, what does the fox say?')
        return self
