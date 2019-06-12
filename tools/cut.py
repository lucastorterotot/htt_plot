import copy

class Cutstring(object):
    def __init__(self, string):
        self.string = string

    def __and__(self, other):
        return Cutstring('({cut1}) && ({cut2})'.format(cut1=str(self),
                                             cut2=str(other)))

    def __or__(self, other):
        return Cutstring('({cut1}) || ({cut2})'.format(cut1=str(self),
                                             cut2=str(other)))

    def __str__(self):
        return '{cut}'.format(cut = self.string)

    def __invert__(self):
        return Cutstring('!({cut})'.format(cut = self.string))

    def __sub__(self, other):
        return self + ~other
    
    def __isub__(self, other):
        self = self - other
        return self  

    def __add__(self, other):
        return self & other
    
    def __iadd__(self, other):
        self = self + other
        return self  

    def __mul__(self, other):
        return Cutstring('(' + str(self) + ') * (' + str(other) + ')')

    def __imul__(self, other):
        self = self * other
        return self
   
    def __repr__(self):
        '''for easy reading'''
        return str(self)
    
class Cuts(dict):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            kwargs[key] = Cutstring(value)
        super(Cuts, self).__init__(kwargs)
        
    def print_cuts(self):
        print self

    def __and__(self, other):
        return Cutstring('({cut1}) && ({cut2})'.format(cut1=str(self),
                                             cut2=str(other)))

    def __or__(self, other):
        return Cutstring('({cut1}) || ({cut2})'.format(cut1=str(self),
                                             cut2=str(other)))

    def any(self):
        cuts = [str(value) for value in sorted(self.values())]
        return Cutstring('(' + ') || ('.join(cuts) + ')')

    def all(self):
        cuts = [str(value) for value in sorted(self.values())]
        return Cutstring('(' + ') && ('.join(cuts) + ')')

    def __str__(self):
        return self.all().string
    
    def __invert__(self):
        newone = copy.deepcopy(self)
        for key, value in newone.iteritems():
            newone[key] = Cutstring('!({cut})'.format(cut=value))
        return newone

    def __sub__(self, other):
        newone = copy.deepcopy(self)
        newone -= other
        return newone
    
    def __isub__(self, other):
        for key in other:
            if key in self:
                del self[key]
        return self  

    def __add__(self, other):
        newone = copy.deepcopy(self)
        newone += other
        return newone
    
    def __iadd__(self, other):
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
        elif isinstance(other, Cutstring):
            self[str(other)] = str(other)
        return self

    def __mul__(self, other):
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
        return copy.deepcopy(self)
