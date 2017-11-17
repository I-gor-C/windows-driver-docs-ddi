---
UID: NS.fcb._SRV_OPEN~r1
title: SRV_OPEN
author: windows-driver-content
description: 
ms.assetid: 9927485a-6a74-4cf8-bceb-4c6ed56ad672
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SRV_OPEN, SRV_OPEN, *PSRV_OPEN
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

# SRV_OPEN structure

## -description



## -struct-fields

### -field union __unnamed_union_0bd5_9			
 	
### -field union __unnamed_union_0bd5_11			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field __volatile LONG BufferingToken			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field LIST_ENTRY FobxList			
 	
### -field PFOBX InternalFobx			
 	
### -field NTSTATUS OpenStatus			
 	
### -field MRX_NORMAL_NODE_HEADER spacer			
 	
### -field PFCB Fcb			
 	
### -field PV_NET_ROOT VNetRoot			
 	
### -field LIST_ENTRY SrvOpenKeyList			
 	
### -field ULONG SequenceNumber			
 	
## -remarks

## -see-also