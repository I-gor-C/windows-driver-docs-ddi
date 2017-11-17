---
UID: NS.ntifs._KAPC_STATE
title: KAPC_STATE
author: windows-driver-content
description: 
ms.assetid: 94b18ab4-48e3-4905-ad83-a065e8c21347
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: KAPC_STATE, KAPC_STATE, *PKAPC_STATE, *PRKAPC_STATE
req.header: ntifs.h
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

# KAPC_STATE structure

## -description



## -struct-fields

### -field struct _KPROCESS			
 	
### -field _KPROCESS * Process			
 	
### -field union __unnamed_union_0c30_80			
 	
### -field LIST_ENTRY [MaximumMode] ApcListHead			
 	
### -field BOOLEAN KernelApcPending			
 	
### -field BOOLEAN UserApcPending			
 	
### -field BOOLEAN  : 1 KernelApcInProgress			
 	
### -field BOOLEAN  : 1 SpecialApcInProgress			
 	
### -field UCHAR InProgressFlags			
 	
## -remarks

## -see-also