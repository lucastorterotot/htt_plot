import pprint
import collections

class Task(object):
    '''Base Task class'''
    
    names = []
    
    def __init__(self, name, dinput, doutput):
        if name in self.__class__.names:
            raise ValueError('a task with name {} already exists, choose another one'.format(name))
        else:
            self.__class__.names.append(name)
        self.name = name
        if not isinstance(dinput, collections.Mapping):
            raise ValueError('dinput argument should be of a mapping type (e.g. dict)')
        if not isinstance(dinput, collections.Mapping):
            raise ValueError('doutput argument should be of a mapping type (e.g. dict)')
        self.dinput = dinput
        self.doutput = doutput    

    def run(self):
        pass
    
    def __str__(self):
        header = 'task {}'.format(self.name)
        sin = pprint.pformat(self.dinput)
        sout = pprint.pformat(self.doutput)
        return '\n'.join([header, sin, sout])
