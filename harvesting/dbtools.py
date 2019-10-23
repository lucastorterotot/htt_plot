from datasetdb import DatasetDB
from getpass import getpass
from htt_plot.tools.dataset import Dataset

print('Dataset reader password:')
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

def fetch_dataset(sample_name,n_events_gen=None,xs=None,channel='tt',sys='nominal'):
    '''returns a dataset created using the db'''
    if 'Embedding_tracking' in sys:
        sys = 'nominal'
    if n_events_gen==None and xs==None and not ('Embedded' in sample_name) and not ('SUSY' in sample_name):
        sys = ''
    infos = dsdb.find('se', {'sample':sample_name,
                        'sample_version':{'$regex':'.*{}.*{}$'.format(channel,sys)}})
    if not infos:
        if sys!='nominal':
            print 'version {} not found in the database for sample {}, looking for nominal'.format(sys,sample_name)
            return fetch_dataset(sample_name,n_events_gen,xs,'nominal')
        raise ValueError('version {} not found in the database for sample {}'.format(sys,sample_name))
    if len(infos)> 1 and sample_name == 'Embedded2017B_tt' and sys=='TES_promptEle_1prong0pi0_down':
        infos = [info for info in infos if info['sample_version'] == 'tt_embed_TES_promptEle_1prong0pi0_down']
    try:
        info = max(infos, key=lambda info: info['sub_date'])
        if sample_name in ['TTHad_pow','TTLep_pow','TTSemi_pow']:
            info = [info for info in infos if info['prod_date']=='190503'][0]
        basedir = info['fakes']['replicas']['lyovis10']['dir']
        if n_events_gen:
            n_events_gen = n_events_gen*efficiency(info['name'])
        return Dataset('{}_{}'.format(sample_name,sys),
                       '{}/{}/NtupleProducer/tree.root '.format(basedir,info['name']),
                       n_events_gen,xs, #those informations should ultimately be retrieved from the db
                       treename='events')
    except KeyError:
        info= infos[0]
        print 'sample {} version {} not fully processed!'.format(info['name'],info['sample_version'])
        newinfos = dsdb.find('se', {'sample':sample_name, 'sample_version':{'$regex':'.*{}.*{}$'.format(channel,'nominal')}})
        newinfo = newinfos[0]
        basedir = newinfo['fakes']['replicas']['lyovis10']['dir']
        if n_events_gen:
            n_events_gen = n_events_gen*efficiency(newinfo['name'])
        return Dataset('{}_{}'.format(sample_name,sys),
                       '{}/{}/NtupleProducer/tree.root '.format(basedir,newinfo['name']),
                       n_events_gen,xs, #those informations should ultimately be retrieved from the db
                       treename='events')
