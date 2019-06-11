import copy

class Cuts(dict):

    def __init__(self, **kwargs):
        super(Cuts, self).__init__(kwargs)
        
    def print_cuts(self):
        for key, value in sorted(self.iteritems()):
            print key, value
    
    def marginal(self, cutname):
        marg_cuts = copy.copy(self)
        del marg_cuts[cutname]
        return marg_cuts

    def __str__(self):
        cuts = [value for _, value in sorted(self.iteritems())]
        return '(' + ') && ('.join(cuts) + ')'
