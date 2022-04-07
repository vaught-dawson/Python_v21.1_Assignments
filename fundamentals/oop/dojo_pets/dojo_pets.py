from classes.ninja import Ninja
from classes.fox import Fox


fox = Fox('foxxy', 'dig')
person = Ninja('Dawson', 'Vaught', None, None, fox)

person.feed().walk().bathe()
