import FWCore.ParameterSet.Config as cms

from Analyzers.ChargeDepAndPtCorr.chargedepptcorr_cfi import *

#### Standard analysis for pixel Rereco PbPb 2015 ####

#### centrality 0-5% ####


CPDCSUBASH = defaultCPDC.clone()
CPDCSUBASH.noffmin = cms.untracked.int32(85)
CPDCSUBASH.noffmax = cms.untracked.int32(100)


#pT diff file
#CPDCptdiff = defaultCPDC.clone()
#CPDCptdiff.pTminTrk_trg = cms.untracked.int32(0.1,0.2,0.3,0.4,0.5,1.0,2.0)
#CPDCptdiff.pTminTrk_trg = cms.untracked.int32(0.2,0.3,0.4,0.5,1.0,2.0,3.0)
