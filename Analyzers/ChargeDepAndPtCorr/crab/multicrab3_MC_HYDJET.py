if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    from CRABClient.UserUtilities import config, getUsernameFromSiteDB
    config = config()

    config.General.workArea = 'ChargeDepPtCorr_PbPb_pixelReReco_MCreco_etaphiweights_Jun16'
    config.General.transferOutputs = True
    config.General.transferLogs = False
    config.JobType.pluginName = 'Analysis'
    config.JobType.maxMemoryMB = 2500
    config.JobType.psetName = '../cfg/chargedepptcorr_base_cfg.py'
    config.Data.unitsPerJob = 10 #For MC Jobs
    config.Data.totalUnits = -1
    config.Data.inputDBS = 'global'
    #config.Data.splitting = 'LumiBased'
    config.Data.splitting = 'FileBased'
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

    config.General.requestName = 'PbPb2015_pixelReReco_chgdepcorr_std_central_v1'
    config.JobType.psetName = '../cfg/chargedepptcorr_central_cfg.py'
    config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v13_75X_mcRun2_HeavyIon_v13-v1/AODSIM'
    config.Data.outputDatasetTag = 'Historgram_chgepcorr_PbPb2015_pixelReReco_std_central_MCreco_Jun16'
    submit(config)

    ##### Midcentral events 10-30% ####
   # config.General.requestName = 'PbPb2015_pixelReReco_chgdepcorr_std_midcentral_v1'
   # config.JobType.psetName = '../cfg/chargedepptcorr_midcentral_cfg.py'
   # config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v13_75X_mcRun2_HeavyIon_v13-v1/AODSIM'
   # config.Data.outputDatasetTag = 'Historgram_chgepcorr_PbPb2015_pixelReReco_std_midcentral_Jun06_noPhiwgt_MCgen_Phi_Jun15_onlyPhi_v1'
   # submit(config)

    ##### Midperipheral events 30-50% ####
    #config.General.requestName = 'PbPb2015_pixelReReco_chgdepcorr_std_midperipheral_v1'
    #config.JobType.psetName = '../cfg/chargedepptcorr_midperipheral_cfg.py'
    #config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v13_75X_mcRun2_HeavyIon_v13-v1/AODSIM' 
    #config.Data.outputDatasetTag = 'Historgram_chgepcorr_PbPb2015_pixelReReco_std_midperipheral_Jun06_noPhiwgt_MCgen_Phi_Jun15_onlyPhi_v1'
    #submit(config)

    ##### Peripheral events 50-100% ####
   # config.General.requestName = 'PbPb2015_pixelReReco_chgdepcorr_std_peripheral_v1'
   # config.JobType.psetName = '../cfg/chargedepptcorr_peripheral_cfg.py'
   # config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV_750/HINPbPbWinter16DR-NoPU_75X_mcRun2_HeavyIon_v13_75X_mcRun2_HeavyIon_v13-v1/AODSIM'
   # config.Data.outputDatasetTag = 'Historgram_chgepcorr_PbPb2015_pixelReReco_std_peripheral_Jun06_noPhiwgt_MCgen_Phi_Jun15_onlyPhi_v1'
   # submit(config)
