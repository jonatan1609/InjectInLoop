from inspect import stack
from re import compile
import __main__ as main


class Base:
    pattern = compile(r" *for +(\(*.+\)*(\.\w+)+(?:, *\(*.+\)*(\.\w+)+)*\)*)|(\w+[, \w]*) +in")
    function = False
    functions = []

    def __init__(self, *params, unpack="", f_params: dict = None):
        assert self.function or self.functions, "You must set a function or a list of functions to be called each iteration"
        self.__setattr__("params", params, True)
        self.__setattr__("f_params", f_params, True)
        self.__setattr__("vars", [], True)
        self.__setattr__("unpack", unpack, True)

    def __getattr__(self, item):
        self.vars.append(item)
        return self

    def __setattr__(self, item, value, init: bool = False):
        if not init:
            if item not in self.vars:
                self.vars.append(item)
            assert self.pattern.match(stack()[-1].code_context[0]), "You can't use this object outside a loop"
            args = ",".join(var if var != self.unpack else "*"+var for var in self.vars)
            if isinstance(value, str):
                value = repr(value)
            exec(f"{args}={value}", main.__dict__)
            if callable(self.function):
                self.function(*self.params)
            if self.functions:
                for func in self.functions:
                    func(*self.f_params[func.__name__])
        return object.__setattr__(self, item, value)
