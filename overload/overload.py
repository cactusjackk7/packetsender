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


