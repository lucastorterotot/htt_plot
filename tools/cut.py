import copy


class Cut(object):

    def __init__(self, cutstr):
        self.cutstr = cutstr

    def __and__(self, other):
        newone = copy.deepcopy(self)
        newone.cutstr = '({cut1}) && ({cut2})'.format(cut1=str(self), cut2=str(other))
        return newone

    def __or__(self, other):
        newone = copy.deepcopy(self)
        newone.cutstr = '(({cut1}) || ({cut2}))'.format(cut1=str(self), cut2=str(other))
        return newone

    def __str__(self):
        return self.cutstr
    
    def __invert__(self):
        newone = copy.deepcopy(self)
        newone.cutstr = '!({cut})'.format(cut=str(self))
        return newone
    
    # RIC: this is a bit dangerous as it depends exactly on
    #      how the string is typed in. 
    def replace(self, oldcut, newcut):
        newone = copy.deepcopy(self)
        newone.cutstr = newone.cutstr.replace(oldcut.cutstr, newcut.cutstr)
        return newone
