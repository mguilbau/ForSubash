import FWCore.ParameterSet.Config as cms

process = cms.Process("ChargeDepAndPtCorr")
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')                                                               
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("HeavyIonsAnalysis.Configuration.hfCoincFilter_cff")

# __________________ General _________________

# Configure the logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    #input = cms.untracked.int32(-1) 
    input = cms.untracked.int32(3000) 
)

# __________________ I/O files _________________

# Define the input file to run on in interactive mode
#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(
#        'root://cms-xrd-global.cern.ch//store/hidata/HIRun2015/HIMinimumBias2/AOD/25Aug2016-v1/90000/34CD034C-ED6F-E611-A55F-44A842124E15.root'
#    )
#)

#----- Testing one One file -------------------
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

        '/store/data/Run2018C/HighMultiplicityEOF1/AOD/PromptReco-v2/000/319/488/00000/FEBCFC7A-9C87-E811-8510-02163E012E44.root'
        #'/store/hidata/HIRun2018A/HIMinimumBias2/AOD/PromptReco-v1/000/326/886/00000/EC263AEE-A375-BF49-9E4A-78E55F6B4A49.root'
        #'file:/eos/cms/store/hidata/HIRun2018A/HIMinimumBias13/AOD/PromptReco-v1/000/326/623/00000/5EC2FCC1-2B5D-9445-B39C-54B0632A29EB.root' 
        #' /store/data/Run2018D/MinimumBias/AOD/PromptReco-v2/000/325/227/00000/1F470AE8-CF09-714B-8775-EFE8811664F3.root'
        )
)
#----------------------------------------------

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring(
#        'root://cms-xrd-global.cern.ch//store/himc/HINPbPbWinter16DR/Hydjet_Quenched_MinBias_5020GeV_750/AODSIM/NoPU_75X_mcRun2_HeavyIon_v13_75X_mcRun2_HeavyIon_v13-v1/80000/001E4607-5BBA-E611-9A99-0CC47A7E6A2C.root'
#    )
#)

# Define output file name
import os
process.TFileService = cms.Service("TFileService",
     #fileName = cms.string(os.getenv('CMSSW_BASE') + '/src/Analyzers/ChargeDepAndPtCorr/test/chargeptdepcorr.root')
     fileName = cms.string('chargeptdepcorr_central.root')
)


# __________________ Detector conditions _________________

# Configure the Global Tag
# Global tag contains information about detector geometry, calibration, alignement, ...
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')


# __________________ Event selection _________________
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)                                                    
#process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)                                                                  
#process.pBeamScrapingFilter = cms.Path(process.beamScrapingFilter)                                                                    
#process.collisionEventSelectionAOD = cms.Path(process.collisionEventSelectionAOD)                                                     
#process.collisionEventSelectionAODv2 = cms.Path(process.collisionEventSelectionAODv2)                                                 

process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
#process.phfCoincFilter1Th3 = cms.Path(process.hfCoincFilterTh3)                                                                       
#process.phfCoincFilter2Th3 = cms.Path(process.hfCoincFilter2Th3)                                                                      
#process.phfCoincFilter3Th3 = cms.Path(process.hfCoincFilter3Th3)                                                                      
#process.phfCoincFilter4Th3 = cms.Path(process.hfCoincFilter4Th3)                                                                      
#process.phfCoincFilter5Th3 = cms.Path(process.hfCoincFilter5Th3)                                                                      
#process.phfCoincFilter1Th4 = cms.Path(process.hfCoincFilterTh4)                                                                       
#process.phfCoincFilter2Th4 = cms.Path(process.hfCoincFilter2Th4)                                                                      

process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")
process.hltMB = process.hltHighLevel.clone()
process.hltMB.HLTPaths = [
 #              "HLT_Fulltrack_Multiplicity85_*1160192",
#               "HLT_FullTrackMultiplicity100_*811925"
                  "HLT_FullTracks_Multiplicity100_v*",
                   "HLT_FullTracks_Multiplicity85_v*"
]



process.eventSelections = cms.Sequence(
        process.clusterCompatibilityFilter
        + process.primaryVertexFilter
        + process.hfCoincFilter2Th4
)

# trigger selection                                                                                                                    
#process.load("HLTrigger.HLTfilters.hltHighLevel_cfi")                                                                                 
#process.hltHIL1MinimumBiasHF_OR_SinglePixelTrack = process.hltHighLevel.clone()                                                       
#process.hltHIL1MinimumBiasHF_OR_SinglePixelTrack.HLTPaths = ["HLT_HIL1MinimumBiasHF_OR_SinglePixelTrack_part*"]                       
#process.hltHIL1MinimumBiasHF_OR_SinglePixelTrack.andOr = cms.bool(True)                                                               
#process.hltHIL1MinimumBiasHF_OR_SinglePixelTrack.throw = cms.bool(False)                                                              
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltSelect = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltSelect.HLTPaths = [
    #"HLT_HIMinimumBias_*",
    "HLT_FullTracks_Multiplicity100_v*",
    "HLT_FullTracks_Multiplicity85_v*"

 ]
process.hltSelect.andOr = cms.bool(True)
process.hltSelect.throw = cms.bool(False)
###                                                                                                                                    

#GlobalTak                                                                                                                             

#Centrality                                                                                                                            

#process.ChargeDepAndPtCorr.centralityBinSrc = cms.InputTag("centralityBin","HFtowers")

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')
#process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag                                                                         

#print('\n\033[31m~*~ USING CENTRALITY TABLE FOR PbPb 2018 ~*~\033[0m\n')
#process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
#process.GlobalTag.toGet.extend([
 #   cms.PSet(record = cms.string("HeavyIonRcd"),
  #      tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"),
  #      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
  #      label = cms.untracked.string("HFtowers")
  #      ),
  #  ])


# __________________ Analyse Sequence _________________

# Load you analyzer with initial configuration
process.load("Analyzers.ChargeDepAndPtCorr.chargedepptcorr_cff")
process.defaultAnalysis   = process.CPDCSUBASH.clone()
process.p = cms.Path(process.hltSelect *             # Requier HF coincidence with 3 GeV  
                     process.eventSelections *        # Clean up on vertices
                     #process.centralityBin * # Clean up on pileup
                     process.clusterCompatibilityFilter * # Clean up on pileup   
                     process.defaultAnalysis)
                     
                     

