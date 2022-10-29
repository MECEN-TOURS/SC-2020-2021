#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Rappels sur les types de méthodes.


Session:
>>> e = Exemple()
>>> e
<__main__.Exemple object at 0x7f9bbfebbbb0>
>>> dir(e)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'classique', 'de_classe', 'statique']
>>> e.classique()
args: (<__main__.Exemple object at 0x7f9bbfebbbb0>,)
>>> e.statique()
args: ()
>>> e.de_classe()
args: (<class '__main__.Exemple'>,)
>>> e.__class__
<class '__main__.Exemple'>
>>> e.classique("chaine")
args: (<__main__.Exemple object at 0x7f9bbfebbbb0>, 'chaine')
>>> e.statique("chaine")
args: ('chaine',)
>>> e.de_classe("chaine")
args: (<class '__main__.Exemple'>, 'chaine')
>>> Exemple
<class '__main__.Exemple'>
"""


class Exemple:
    def classique(*args):
        print(f"args: {args}")

    @staticmethod
    def statique(*args):
        print(f"args: {args}")

    @classmethod
    def de_classe(*args):
        print(f"args: {args}")
