---
UID : NA:extsfns
ms.assetid : 65a44f62-6646-38b2-b962-e5ad09608ad4
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# extsfns.h header



extsfns.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IDebugFAEntryTags](nn-extsfns-idebugfaentrytags.md) | When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins. |
| [IDebugFailureAnalysis2](nn-extsfns-idebugfailureanalysis2.md) | When the !analyze debugger command runs, the analysis engine can load and run extension analysis plug-ins. |





## Structures
| Title | Description |
| ---- |:---- |
| [_FA_ENTRY](ns-extsfns-_fa_entry.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). Each FA entry is represented by an FA_ENTRY structure. For more information, see Failure Analysis Entries, Tags, and Data Types. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_DEBUG_FAILURE_TYPE](ne-extsfns-_debug_failure_type.md) | The values in the DEBUG_FAILURE_TYPE enumeration indicate the type of a failure. |
| [_DEBUG_FLR_PARAM_TYPE](ne-extsfns-_debug_flr_param_type.md) | The values of DEBUG_FLR_PARAM_TYPE enumeration are tags that indicate the kind of information that is stored in failure analysis entry. |
| [_FA_ENTRY_TYPE](ne-extsfns-_fa_entry_type.md) | A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries). |
| [_FA_EXTENSION_PLUGIN_PHASE](ne-extsfns-_fa_extension_plugin_phase.md) | A value in the FA_EXTENSION_PLUGIN_PHASE enumeration is passed to the _EFN_Analyze function to specify which phase of the analysis is currently in progress. |