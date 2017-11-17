---
UID: NS.fcb._SRV_CALL~r1
title: SRV_CALL
author: windows-driver-content
description: 
ms.assetid: df122f1e-6514-42c9-86d4-b487db5fbf90
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SRV_CALL, SRV_CALL, *PSRV_CALL
req.header: fcb.h
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

# SRV_CALL structure

## -description



## -struct-fields

### -field union __unnamed_union_0bd5_1			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field RX_PREFIX_ENTRY PrefixEntry			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field ULONG SerialNumberForEnum			
 	
### -field __volatile LONG NumberOfCloseDelayedFiles			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field PURGE_SYNCHRONIZATION_CONTEXT PurgeSyncronizationContext			
 	
### -field RX_BUFFERING_MANAGER BufferingManager			
 	
### -field MRX_NORMAL_NODE_HEADER spacer			
 	
## -remarks

## -see-also