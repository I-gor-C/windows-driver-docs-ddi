---
UID: NS.pep_x._PEP_PPM_PROCESSOR_LPI_STATE~r1
title: PEP_PPM_PROCESSOR_LPI_STATE
author: windows-driver-content
description: 
ms.assetid: 9ed61579-7ea2-47a0-9ab3-7b424d3b5d8e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PEP_PPM_PROCESSOR_LPI_STATE, PEP_PPM_PROCESSOR_LPI_STATE, *PPEP_PPM_PROCESSOR_LPI_STATE
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

# PEP_PPM_PROCESSOR_LPI_STATE structure

## -description



## -struct-fields

### -field union Flags			
 	
### -field __unnamed_union_0c3d_25 __unnamed_union_0c3d_25			
 	
### -field union ArchContextFlags			
 	
### -field __unnamed_union_0c3d_27 __unnamed_union_0c3d_27			
 	
### -field ULONG MinResidency			
 	
### -field ULONG WakeupLatency			
 	
### -field ULONG ResidencyCounterFrequency			
 	
### -field PEP_PPM_LPI_REGISTER EntryMethod			
 	
### -field PEP_PPM_LPI_REGISTER ResidencyCounter			
 	
### -field PEP_PPM_LPI_REGISTER UsageCounter			
 	
### -field PWSTR StateName			
 	
### -field ULONG  : 1 Enabled			
 	
### -field ULONG  : 31 Reserved			
 	
### -field ULONG AsUlong			
 	
### -field ULONG  : 1 CoreContextLost			
 	
### -field ULONG  : 1 TraceContextLost			
 	
### -field ULONG  : 1 GICR			
 	
### -field ULONG  : 1 GICD			
 	
### -field ULONG  : 28 Reserved			
 	
### -field ULONG AsUlong			
 	
## -remarks

## -see-also