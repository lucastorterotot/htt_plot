from collections import OrderedDict
import copy
import pprint 

class Meta(type):
    def __getitem__(self, name):
        return self.instances[name]

class Cut(object):
    
    __metaclass__ = Meta
    
    instances = dict()
    
    def __init__(self, name, cutstr):
        self.name = name
        self.cutstr = cutstr
        self.__class__.instances[name] = self

    def __and__(self, other):
        newone = copy.deepcopy(self)
        newone.cutstr = '({cut1}) && ({cut2})'.format(cut1=str(self),
                                                      cut2=str(other))
        return newone

    def __or__(self, other):
        newone = copy.deepcopy(self)
        newone.cutstr = '(({cut1}) || ({cut2}))'.format(cut1=str(self),
                                                        cut2=str(other))
        return newone

    def __str__(self):
        return self.cutstr
    
    def __repr__(self):
        return '{}: {}'.format(self.name, self.cutstr)

    def __invert__(self):
        newone = copy.deepcopy(self)
        newone.cutstr = '!({cut})'.format(cut=str(self))
        return newone
    
    @classmethod
    def available_cuts(cls):
        '''list all defined cuts.
        to access one of them, do Cut[cut_name]
        (note the use of the Cut class, not a cut instance)
        '''
        return cls.instances
    

class CutFlow(OrderedDict):
    '''Represents a cut flow.
    The cuts are Cut objects, and are ordered.
    a new cut can be added by doing:
    
    cut['newcut'] = 'abs(eta)<0.5'
    
    a cut can be deleted by doing:
    
    del cut['newcut']
    '''
    def __init__(self, items):
        '''e.g.
        cuts = Cuts([
            ('pcut', 'p>1'),
            ('ecut', 'e<0')
        ])
        '''
        tmp = []
        for name, cut in items:
            if not isinstance(cut, Cut):
                cut = Cut(name, cut)
            tmp.append( (name, cut) ) 
        super(CutFlow, self).__init__(tmp)
        
    def marginal(self, cutname):
        marg_cuts = copy.copy(self)
        del marg_cuts[cutname]
        return marg_cuts

    def __add__(self, other):
        result = copy.copy(self)
        if isinstance(other, CutFlow):
            result.update(other)
        else:
            # adding a cut
            result[other.name] = other
        return result
    
    def __iadd__(self, other):
        if isinstance(other, CutFlow):
            self.update(other)
        else:
            # adding a cut
            self[other.name] = other
        return self        

    def __str__(self):
        '''not sure root will accept a multiline string..'''
        tmp = ['({})'.format(str(cut)) for cut in self.values()]
        return ' && '.join(tmp)
   
    def __repr__(self):
        '''for easy reading'''
        string = ''
        for name, val in self.iteritems():
            string += name
            string += '\n'
            string += str(val)
            string += '\n'
            string += '\n'
        return string
