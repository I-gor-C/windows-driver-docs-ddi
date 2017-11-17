---
UID: NS.fcb._SRV_OPEN
title: SRV_OPEN
author: windows-driver-content
description: 
ms.assetid: 5b433d7b-7db5-46aa-8443-ee00ca2e9b6a
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

### -field union __unnamed_union_0bd5_8			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field __volatile LONG BufferingToken			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field LIST_ENTRY FobxList			
 	
### -field PFOBX InternalFobx			
 	
### -field NTSTATUS OpenStatus			
 	
### -field LIST_ENTRY SrvOpenKeyList			
 	
### -field ULONG SequenceNumber			
 	
## -remarks

## -see-also