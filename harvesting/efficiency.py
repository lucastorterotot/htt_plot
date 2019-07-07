from datasetdb import DatasetDB
from getpass import getpass

pwd = getpass()
dsdb = DatasetDB('reader', pwd, db='datasets')

def get_nchunks(info):
    '''returns number of chunks for a dataset info.
    Sums up all chunks in subdirectories 0000, 0001, etc
    '''
    tgzs = info.get('tgzs', None)
    if tgzs is None: 
        return 0
    nchunks = 0
    for subd, subdchunks in tgzs.iteritems(): 
        nchunks += len(subdchunks) 
    return nchunks

def efficiency(name):
    '''returns efficiency for dataset with this name.
    name should be like 190503%HiggsSUSYGG1400%tt_mssm_signals_CMS_scale_j_RelativeSample_13TeV_up
    '''
    infos = dsdb.find('se', {'name':name})
    if not infos: 
        raise ValueError(name + ' not found in the database')
    info = infos[0]
    nchunks = get_nchunks(info)
    njobs = info['njobs']
    if njobs is None: 
        njobs = 99
    return float(nchunks)/njobs
