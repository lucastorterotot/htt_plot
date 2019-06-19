''' Defines two classes,
Cut to manage easily cut strings
Cuts to handle several cuts at a time
'''

import copy
import pprint

class Cut(object):
    ''' Wrapper of a string for ROOT cut strings '''
    
    def __init__(self, string):
        self.string = str(string)

    def __str__(self):
        return self.string

    def __and__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double & stands for ROOT usage '''
        return Cut('({cut1}) && ({cut2})'.format(cut1 = str(self),
                                                 cut2 = str(other)))

    def __or__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double | stands for ROOT usage '''
        return Cut('({cut1}) || ({cut2})'.format(cut1 = str(self),
                                                 cut2 = str(other)))

    def __invert__(self):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cut('!({cut})'.format(cut = str(self)))

    def __mul__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cut('({cut1}) * ({cut2})'.format(cut1 = str(self),
                                                cut2 = str(other)))

    def __imul__(self, other):
        # self.string to be replaced
        self.string = '({cut1}) * ({cut2})'.format(cut1 = str(self),
                                                   cut2 = str(other))
        return self
   
    def __repr__(self):
        '''for easy reading'''
        return str(self)
    
class Cuts(dict):
    ''' A dict of Cuts. '''
    def __init__(self, **kwargs):
        for key, string in kwargs.iteritems():
            kwargs[key] = Cut(string)
        super(Cuts, self).__init__(kwargs)

    def any(self):
        ''' Using a Cut allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self cuts '''
        cuts = [str(cut) for cut in sorted(self.values())]
        return Cut('(({}))'.format(') || ('.join(cuts)))

    def all(self):
        ''' Using a Cut allows for operator uses, see the
        corresponding class above. The returned cut is:
        all of self cuts '''
        cuts = [str(cut) for cut in sorted(self.values())]
        return Cut('(({}))'.format(') && ('.join(cuts)))

    def __str__(self):
        return pprint.pformat(self)

    def __setitem__(self, key, value):
        super(Cuts, self).__setitem__(key, Cut(value))
