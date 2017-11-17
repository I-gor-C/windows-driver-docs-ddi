---
UID: NS.fcb._NET_ROOT~r1
title: NET_ROOT
author: windows-driver-content
description: 
ms.assetid: a0db3a51-ad74-485e-9285-e3ddb9f2cf21
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NET_ROOT, NET_ROOT, *PNET_ROOT
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

# NET_ROOT structure

## -description



## -struct-fields

### -field union __unnamed_union_0bd5_3			
 	
### -field BOOLEAN UpperFinalizationDone			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
### -field PURGE_SYNCHRONIZATION_CONTEXT PurgeSyncronizationContext			
 	
### -field PV_NET_ROOT DefaultVNetRoot			
 	
### -field LIST_ENTRY VirtualNetRoots			
 	
### -field ULONG NumberOfVirtualNetRoots			
 	
### -field ULONG SerialNumberForEnum			
 	
### -field RX_PREFIX_ENTRY PrefixEntry			
 	
### -field RX_FCB_TABLE FcbTable			
 	
### -field MRX_NORMAL_NODE_HEADER spacer			
 	
### -field PSRV_CALL SrvCall			
 	
## -remarks

## -see-also