from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = Configuration()

config.section_('General')
config.General.workArea = 'resultsAna_JOBTAG/'
config.General.requestName = 'OUTFILENAME'
config.General.transferOutputs = True
config.General.transferLogs=True
config.General.failureLimit=1

config.section_('JobType')
config.JobType.scriptExe = 'submitFileCrab.sh'
config.JobType.inputFiles = ['/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_8_0_10/src/ZZMatrixElement/MEKD','/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_8_0_10/src/KinZfitter/KinZfitter/ParamZ1','/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_8_0_10/src/KinZfitter/HelperFunction/hists']
config.JobType.psetName = 'CFGFILE'
config.JobType.pluginName = 'Analysis'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['OUTFILENAME.root']

config.section_('Data')
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.inputDataset = 'DATASETNAME'
if ('Run2016' in 'DATASETNAME'):
  config.Data.lumiMask = 'Run2016_09Jul.txt'
  config.Data.splitting = 'EventAwareLumiBased'
  config.Data.unitsPerJob = 400000
else:
  config.Data.splitting = 'FileBased'
  config.Data.unitsPerJob = 5
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/%s/UFHZZAnalysisRun2/JOBTAG/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = True

config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_US_Florida'
config.Site.whitelist = ['T2_US_*']