import FWCore.ParameterSet.Config as cms

defaultCPDC = cms.EDAnalyzer('ChargeDepAndPtCorr', #Analyzer named: Correspond to the class name in 'plugin' fold
#defaultCPDC = cms.EDFilter('ChargeDepAndPtCorr',
                             #Track collection
                             #tracks    = cms.InputTag('hiConformalPixelTracks'),
                             #trackSrc  = cms.InputTag("genParticles"), #for Gen. particles only
                             #tracks  = cms.InputTag("genParticles"), #for Gen. particles only
                             tracks    = cms.InputTag('generalTracks'), 
                             #Vertex collection
                             vertex    = cms.InputTag('offlinePrimaryVertices'),
                             #Calorimeter tower collection
                             caloTower = cms.InputTag('towerMaker'),
                             #Centrality
                             centralitySrc    = cms.InputTag("hiCentrality"),
                             centralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
                             #Event classifier # 0 == centrality, 1 == n_trk^offline
                             evtclassifier = cms.untracked.int32(0), 
                             centmin = cms.untracked.int32(0), 
                             centmax = cms.untracked.int32(100), 
                             noffmin = cms.untracked.int32(0), 
                             noffmax = cms.untracked.int32(10000), 
                             
                             #Efficiency/Fake correction
                             #cweight = cms.untracked.bool(True),
                             cweight = cms.untracked.bool(False), 
                             #fname   = cms.untracked.InputTag("EffCorrectionsPixel_TT_pt_0_10_v2.root"),
                             fname   = cms.untracked.InputTag("EffCorrectionsPixelPbPb_nominal_v2.root"),
                             effCorrBinMin = cms.untracked.vint32(0,5,10,30,50),
                             effCorrBinMax = cms.untracked.vint32(5,10,30,50,100),

                             #Phiweight new
                             cweight2 = cms.untracked.bool(False), #Checking with phiweights correction
                             fname2   = cms.untracked.InputTag("EtaPhiWeights.root"),
                             phiCorrBinMin = cms.untracked.vint32(0,5,10,15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85),
                             phiCorrBinMax = cms.untracked.vint32(5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90),

                             #Vertex selection
                             nTrkAssoToVtx = cms.untracked.uint32(2),
                             selectVtxByMult = cms.untracked.bool(False),
                             zminVtx = cms.untracked.double(-15.0), #-15 original
                             zmaxVtx = cms.untracked.double(15.0),  #15 original
                             rhomaxVtx = cms.untracked.double(0.2),
                             #Track selection
                             dzdzerror = cms.untracked.double(2.0), #2018 Twiki
                             d0dz0rror = cms.untracked.double(2.0), #
                             
                             #---------------------for pp----------
                             
                             #-------------------------------------
                             
                             pTerrorpT = cms.untracked.double(0.05), #
                             pTminTrk_trg = cms.untracked.vdouble(0.3),
                             pTmaxTrk_trg = cms.untracked.vdouble(2.0), #3.0 original
                             pTminTrk_ass = cms.untracked.vdouble(0.3),
                             pTmaxTrk_ass = cms.untracked.vdouble(2.0),
                             etaminTrk_trg = cms.untracked.double(-2.4), #-2.4
                             etamaxTrk_trg = cms.untracked.double(2.4),  #2.4
                             etaminTrk_ass = cms.untracked.double(-2.4),
                             etamaxTrk_ass = cms.untracked.double(2.4),
                             isHI = cms.untracked.bool(False),
                             isPix = cms.untracked.bool(False), #True Originally (pixel tracking)
                             pTmax_pix = cms.untracked.double(3.0), #2.4 original
                             nhitsmin_pix = cms.untracked.int32(3), #3 original
                             nhitsmax_pix = cms.untracked.int32(6),
                             chi2nmax_pix = cms.untracked.double(1000.0),#9 nominal
                             
                             dzdzerror_pix = cms.untracked.double(40.0), #6 nominal
                             d0d0error_pix = cms.untracked.double(10.0), #6 nominal
                             
                             nhitsmin = cms.untracked.int32(11),
                             algo = cms.untracked.vint32(4,5,6,7),
                             chi2nmax = cms.untracked.double(0.15),
                             #Histogram binning
                             nEtaBins = cms.untracked.int32(32), #32 original
                             nPhiBins = cms.untracked.int32(32), #32 original
                             #Mixing factor
                             bkgFactor = cms.untracked.uint32(10)
                             #bkgFactor = cms.untracked.uint32(6)
                             )
