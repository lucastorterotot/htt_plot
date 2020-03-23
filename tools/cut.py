''' Defines two classes,
Cut to manage easily cut strings
Cuts to handle several cuts at a time
'''

import copy
import pprint

class Cut(object):
    ''' Wrapper of a string for ROOT cut strings '''
    
    def __init__(self, string, weight = 1):
        self.string = str(string)
        self.weight = str(weight)

    def set_weight(self, weight):
        self.weight = str(weight)

    def get_weight(self):
        return self.weight

    def mul_weight(self, weight):
        if self.get_weight() == '1':
            return str(weight)
        elif weight == '1':
            return self.get_weight()
        else:
            return '({})*({})'.format(self.get_weight(), str(weight))

    def __str__(self):
        if self.weight == '1':
            return self.string
        else:
            return '(({}) * ({}))'.format(self.string, self.weight)

    def __and__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double & stands for ROOT usage '''
        if (self.get_weight() != '1' and other.get_weight() != '1'):
            raise RuntimeError(
                'Two weights set:\n{}\n{}\n What to do?'.format(self.get_weight(), other.get_weight())
            )
        return Cut('({cut1}) && ({cut2})'.format(cut1 = self.string,
                                                 cut2 = other.string),
                   weight = self.mul_weight(other.get_weight()))

    def __or__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double | stands for ROOT usage '''
        if (self.get_weight() != '1' and other.get_weight() != '1'):
            raise RuntimeError(
                'Two weights set:\n{}\n{}\n What to do?'.format(self.get_weight(), other.get_weight())
            )
        return Cut('({cut1}) || ({cut2})'.format(cut1 = self.string,
                                                 cut2 = other.string),
                   weight = self.mul_weight(other.get_weight()))

    def __invert__(self):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cut(
            '!({cut})'.format(cut = self.string),
            weight = self.get_weight())

    def __mul__(self, weight):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cut(self.string, weight = self.mul_weight(weight))

    def __imul__(self, weight):
        self.set_weight(self.mul_weight(weight))
        return self
   
    def __repr__(self):
        '''for easy reading'''
        return str(self)
    
class Cuts(dict):
    ''' A dict of Cuts. '''
    def __init__(self, **kwargs):
        for key, string in kwargs.items():
            kwargs[key] = Cut(string)
        super(Cuts, self).__init__(kwargs)

    def any(self):
        ''' Using a Cut allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self cuts '''
        cuts = [str(cut) for cut in self.values()]
        return Cut('(({}))'.format(') || ('.join(cuts)))

    def all(self):
        ''' Using a Cut allows for operator uses, see the
        corresponding class above. The returned cut is:
        all of self cuts '''
        cuts = [str(cut) for cut in self.values()]
        return Cut('(({}))'.format(') && ('.join(cuts)))

    def __str__(self):
        return pprint.pformat(self)

    def __setitem__(self, key, value):
        super(Cuts, self).__setitem__(key, Cut(value))
