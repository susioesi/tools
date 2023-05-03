class abc:
    money = 100
    name = 'God'
    _age = 10

    @property
    def age(self):
        return self._age

    def fly(self):
        print('I am flying')

    # @staticmethod
    def stmd():
        print('StaticMethod')
    # @age.setter
    # def age(self, value):
    #     self._age = value


class d(abc):
    pass


a = abc()
dd = d()
# a.age = 100
a.__getattribute__('fly')()
abc.stmd()
dd.stmd()
