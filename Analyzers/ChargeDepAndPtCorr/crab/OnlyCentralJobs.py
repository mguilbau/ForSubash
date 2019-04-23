if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    from CRABClient.UserUtilities import config, getUsernameFromSiteDB
    config = config()

    #config.General.workArea = 'Prabhat_PbPb2018_LowpT_Dec01_chNN_cent05'
    config.General.workArea = 'Ana_QAplots_PbPb2018data_Cent3035_Dec01_NewBin'
    config.General.transferOutputs = True
    config.General.transferLogs = False
    config.JobType.pluginName = 'Analysis'
    config.JobType.maxMemoryMB = 4000
    config.JobType.psetName = '../cfg/chargedepptcorr_base_cfg.py'
    config.Data.unitsPerJob = 10 #40 is good
    config.Data.totalUnits = -1
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'LumiBased'
    #config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
    config.Data.outLFNDirBase = '/store/user/prabhat/'
    config.Data.publication = False
    config.Site.storageSite = 'T2_IN_TIFR'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    ###############################
    #    Standard analysis        #
    ###############################
    
    ##### Central events 0-10% ####
    ##config.Data.unitsPerJob = 46
 
    config.General.requestName = 'PbPb2015_pixelReReco_chgdepcorr_std_central_v1'
    config.JobType.psetName = '../cfg/chargedepptcorr_central_cfg.py'
    config.Data.inputDataset = '/HIMinimumBias14/HIRun2018A-PromptReco-v1/AOD'
    config.Data.inputDataset = '/HIMinimumBias3/HIRun2018A-PromptReco-v1/AOD'
    #config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-326618_HI_PromptReco_Collisions18_JSON.txt'
    #config.Data.outputDatasetTag = 'Prabhat_PbPb2018_cent05_lowpT_Dec01_chNN_v1'
    config.Data.outputDatasetTag = 'Ana_QAplots_PbPb2018_Dec01_newBin_v1'
    submit(config)

    



    

