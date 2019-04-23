import FWCore.ParameterSet.Config as cms

#Trigger Selection
### Comment out for the timing being assuming running on secondary dataset with trigger bit selected already
import HLTrigger.HLTfilters.hltHighLevel_cfi
hltSelect = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
hltSelect.HLTPaths = ["HLT_FullTrack_Multiplicity155_v*","HLT_FullTrack_Multiplicity130_v*","HLT_FullTrack_Multiplicity100_v*","HLT_FullTrack_Multiplicity85_v*"]
hltSelect.andOr = cms.bool(True)
hltSelect.throw = cms.bool(False)
