from typing import Any, Callable, Tuple


class OverloadException(Exception):
   pass


class OverloadedFunction:
   def __init__(self, name):
     self._name = name
        self._overloads = {}

    def add_overload(self, signature: Tuple[Any, ...], func: Callable[[Any], Any]):
        if signature in self._overloads:
            raise OverloadException(f"Overloaded function '{self._name}' has already been overloaded with signature {signature}")
        self._overloads[signature] = func

    def __call__(self, *args):
        signature = tuple(map(type, args))
        func = self._overloads.get(signature, None)
        if func is None:
            raise OverloadException(f"Overloaded function '{self._name}' does not provide an overload for the signature {signature}")
        else:
            return func(*args) 
