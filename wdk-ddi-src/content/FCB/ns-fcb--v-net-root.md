---
UID: NS.fcb._V_NET_ROOT
title: V_NET_ROOT
author: windows-driver-content
description: 
ms.assetid: 4c61701e-43ba-4186-bfcd-ccb188a4e4c3
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: V_NET_ROOT, V_NET_ROOT, *PV_NET_ROOT
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

# V_NET_ROOT structure

## -description



## -struct-fields

### -field BOOLEAN UpperFinalizationDone			
 	
### -field BOOLEAN ConnectionFinalizationDone			
 	
### -field RX_BLOCK_CONDITION Condition			
 	
### -field __volatile LONG AdditionalReferenceForDeleteFsctlTaken			
 	
### -field RX_PREFIX_ENTRY PrefixEntry			
 	
### -field UNICODE_STRING NamePrefix			
 	
### -field ULONG PrefixOffsetInBytes			
 	
### -field LIST_ENTRY NetRootListEntry			
 	
### -field ULONG SerialNumberForEnum			
 	
### -field LIST_ENTRY TransitionWaitList			
 	
### -field LIST_ENTRY ScavengerFinalizationList			
 	
## -remarks

## -see-also