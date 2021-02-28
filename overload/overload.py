import inspect
from inspect import Parameter Signature 
import functools
from collections import OrderedDict

class OverloadFunction(object):
   
      def __doc__():
         def fget(self):
            return self._doc + ("\n\n".join("%s%s%s" % (f.__qualname__,
                                                        inspect.signature(f), 
                                                       ("\n    %s"%f.__doc__) if hasattr(f, "__doc__") and f.__doc__ else "") for f in self._functions)) 

      def fset(self, x):
         if x != self._functions[0].__doc__:
            self._doc = "%sL %s\n\n" % (self._functions[0].__qualname__, x)
       return locals()
    __doc__ = property(**__doc__())
    __doc = ""


    def __new__(cls, funct):
      if funct.__class__ == OverloadFunction:
            return funct
       self = super().__new__(cls)
       self.functions = [funct]
       return functools.wraps(funct)(self)

    def addfunct(self, funct):
         self._functions.append(funct)

    def __get__(self, instance, owner):
         self.instance = instance
         return self
    
    def _typematch(self, arguments, parameters):
        for name, param in parameters.items():
            if param.annotation is not Parameter.empty:
               test = param.annotation
               if type(test) == type:
                  if not isinstance(arguments[name], test):
                     return False

                  else:
                     if not test(arg):
                        return False

                 return True 
