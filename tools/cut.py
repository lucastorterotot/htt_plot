from collections import OrderedDict
import copy
import pprint 

class Cut(object):
    
    def __init__(self, name, cutstr):
        self.name = name
        self.cutstr = cutstr

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
    
    def __invert__(self):
        newone = copy.deepcopy(self)
        newone.cutstr = '!({cut})'.format(cut=str(self))
        return newone
    

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
        tmp = [ (name, Cut(name, cutstr)) for name, cutstr in items]
        super(CutFlow, self).__init__(items)
        
    def marginal(self, cutname):
        marg_cuts = copy.copy(self)
        del marg_cuts[cutname]
        return marg_cuts

    def __str__(self):
        '''not sure root will accept a multiline string..'''
        tmp = ['({})'.format(cut) for cut in self.values()]
        return ' && \ \n'.join(tmp)
   
