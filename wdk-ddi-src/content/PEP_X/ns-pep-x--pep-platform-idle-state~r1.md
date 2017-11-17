---
UID: NS.pep_x._PEP_PLATFORM_IDLE_STATE~r1
title: PEP_PLATFORM_IDLE_STATE
author: windows-driver-content
description: 
ms.assetid: 3e1c1674-a1c4-4c04-a4ce-cffd90a158a7
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PEP_PLATFORM_IDLE_STATE, PEP_PLATFORM_IDLE_STATE, *PPEP_PLATFORM_IDLE_STATE
req.header: pep_x.h
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

# PEP_PLATFORM_IDLE_STATE structure

## -description



## -struct-fields

### -field union __unnamed_union_0c3d_18			
 	
### -field UCHAR InitiatingState			
 	
### -field ULONG Latency			
 	
### -field ULONG BreakEvenDuration			
 	
### -field ULONG DependencyArrayUsed			
 	
### -field ULONG DependencyArrayCount			
 	
### -field PEP_PROCESSOR_IDLE_DEPENDENCY [ANYSIZE_ARRAY] DependencyArray			
 	
### -field POHANDLE InitiatingProcessor			
 	
### -field PVOID DeviceContext			
 	
## -remarks

## -see-also