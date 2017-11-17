---
UID: NS.scavengr._RDBSS_SCAVENGER
title: RDBSS_SCAVENGER
author: windows-driver-content
description: 
ms.assetid: 18a33be4-fd62-498d-845e-b31e5dd8eea4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: RDBSS_SCAVENGER, RDBSS_SCAVENGER, *PRDBSS_SCAVENGER
req.header: scavengr.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# RDBSS_SCAVENGER structure

## -description



## -struct-fields

### -field RDBSS_SCAVENGER_STATE State			
 	
### -field LONG MaximumNumberOfDormantFiles			
 	
### -field __volatile LONG NumberOfDormantFiles			
 	
### -field LARGE_INTEGER TimeLimit			
 	
### -field ULONG SrvCallsToBeFinalized			
 	
### -field ULONG NetRootsToBeFinalized			
 	
### -field ULONG VNetRootsToBeFinalized			
 	
### -field ULONG FcbsToBeFinalized			
 	
### -field ULONG SrvOpensToBeFinalized			
 	
### -field ULONG FobxsToBeFinalized			
 	
### -field LIST_ENTRY SrvCallFinalizationList			
 	
### -field LIST_ENTRY NetRootFinalizationList			
 	
### -field LIST_ENTRY VNetRootFinalizationList			
 	
### -field LIST_ENTRY FcbFinalizationList			
 	
### -field LIST_ENTRY SrvOpenFinalizationList			
 	
### -field LIST_ENTRY FobxFinalizationList			
 	
### -field LIST_ENTRY ClosePendingFobxsList			
 	
### -field RX_WORK_ITEM WorkItem			
 	
### -field KEVENT SyncEvent			
 	
### -field KEVENT ScavengeEvent			
 	
### -field PETHREAD CurrentScavengerThread			
 	
### -field PNET_ROOT CurrentNetRootForClosePendingProcessing			
 	
### -field PFCB CurrentFcbForClosePendingProcessing			
 	
### -field KEVENT ClosePendingProcessingSyncEvent			
 	
## -remarks

## -see-also