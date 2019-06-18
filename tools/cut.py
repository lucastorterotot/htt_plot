''' Defines two classes,
Cutstring to manage easily cut strings
Cuts to handle several cuts at a time
'''

import copy

class Cutstring(object):
    ''' Wrapper of a string for ROOT cut strings '''
    
    def __init__(self, string):
        self.string = str(string)

    def __str__(self):
        return self.string

    def __and__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double & stands for ROOT usage '''
        return Cutstring('({cut1}) && ({cut2})'.format(cut1=str(self),
                                                       cut2=str(other)))

    def __or__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. The double | stands for ROOT usage '''
        return Cutstring('({cut1}) || ({cut2})'.format(cut1=str(self),
                                                       cut2=str(other)))

    def __add__(self, other):
        ''' cut1 + cut2 usually means cut1 and cut2 '''
        return self & other
    
    def __iadd__(self, other):
        self = self + other
        return self

    def __invert__(self):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cutstring('!({cut})'.format(cut = self.string))

    def __sub__(self, other):
        ''' cut1 - cut2 usually means cut1 and not cut2 '''
        return self + ~other
    
    def __isub__(self, other):
        self = self - other
        return self  

    def __mul__(self, other):
        ''' Conserving a object of the same class allows to 
        make other operations later. '''
        return Cutstring('(' + str(self) + ') * (' + str(other) + ')')

    def __imul__(self, other):
        # self.string to be replaced
        self = self * other
        return self
   
    def __repr__(self):
        '''for easy reading'''
        return str(self)
    
class Cuts(dict):
    ''' A dict of Cutstrings. '''
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            kwargs[key] = Cutstring(value)
        super(Cuts, self).__init__(kwargs)

    def __or__(self, other):
        ''' Using a Cutstring allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self cuts OR all other cuts'''
        return Cutstring('({cut1}) || ({cut2})'.format(cut1=str(self),
                                                       cut2=str(other)))

    def any(self):
        ''' Using a Cutstring allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self cuts '''
        cuts = [str(value) for value in sorted(self.values())]
        return Cutstring('(' + ') || ('.join(cuts) + ')')

    def __and__(self, other):
        ''' Using a Cutstring allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self AND all other'''
        return Cutstring('({cut1}) && ({cut2})'.format(cut1=str(self),
                                                       cut2=str(other)))

    def all(self):
        ''' Using a Cutstring allows for operator uses, see the
        corresponding class above. The returned cut is:
        all of self cuts '''
        cuts = [str(value) for value in sorted(self.values())]
        return Cutstring('(' + ') && ('.join(cuts) + ')')

    def __str__(self):
        '''Returns a string requiring all cuts in this dict to pass.'''
        return self.all().string
        
    def print_cuts(self):
        print self
    
    def __invert__(self):
        '''Inverts all cuts contained in this dict'''
        newone = copy.deepcopy(self)
        for key, value in newone.iteritems():
            newone[key] = Cutstring('!({cut})'.format(cut=value))
        return newone

    def __sub__(self, other):
        ''' Produces a new cut dict, in which all cuts from self
        are present if not in other'''
        newone = copy.deepcopy(self)
        newone -= other
        return newone
    
    def __isub__(self, other):
        ''' Removes all cuts of self present in other '''
        for key in other:
            if key in self:
                del self[key]
        return self  

    def __add__(self, other):
        ''' Removes all cuts of other in self : this is a merging '''
        newone = copy.deepcopy(self)
        newone += other
        return newone
    
    def __iadd__(self, other):
        '''Adds new cuts in this dict.
        If a key is common and the corresponding value in other
        is the same, nothing happens. If one tries to add a cutstring,
        a key is automatically created. '''
        if isinstance(other, Cuts):
            for key, value in other.iteritems():
                if not key in self:
                    self[key] = value
                elif not self[key] == value:
                    self[key] = Cutstring(
                        '({cut1}) && ({cut2})'.format(
                            cut1 = self[key],
                            cut2 = value
                        )
                    )
        elif isinstance(other, Cutstring) and str(other) not in self:
            self[str(other)] = str(other)
        return self

    def __mul__(self, other):
        ''' Using a Cutstring allows for operator uses, see the
        corresponding class above. The returned cut is:
        any of all self TIMES all other'''
        return Cutstring('(' + str(self) + ') * (' + str(other) + ')')
   
    def __repr__(self):
        '''for easy reading'''
        string = ''
        for name, val in sorted(self.iteritems()):
            string += name
            string += '\n'
            string += str(val)
            string += '\n'
            string += '\n'
        return string

    def clone(self):
        ''' Allows to get a new dict, independant of self'''
        return copy.deepcopy(self)
