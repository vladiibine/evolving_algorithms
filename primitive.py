__author__ = 'shefuto'


class Solver(object):
    _functions = []
    _objects = []

    def __call__(self, *args):
        pass


class Operation(object):
    pass


class FuncDef(Operation):
    pass


class ObjDef(Operation):
    pass