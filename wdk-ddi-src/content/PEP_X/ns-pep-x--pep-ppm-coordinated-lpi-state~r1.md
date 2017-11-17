---
UID: NS.pep_x._PEP_PPM_COORDINATED_LPI_STATE~r1
title: PEP_PPM_COORDINATED_LPI_STATE
author: windows-driver-content
description: 
ms.assetid: 3d0adf4b-d42f-497a-a27b-a815aa0bc6b6
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PEP_PPM_COORDINATED_LPI_STATE, PEP_PPM_COORDINATED_LPI_STATE, *PPEP_PPM_COORDINATED_LPI_STATE
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

# PEP_PPM_COORDINATED_LPI_STATE structure

## -description



## -struct-fields

### -field union Flags			
 	
### -field __unnamed_union_0c3d_30 __unnamed_union_0c3d_30			
 	
### -field union ArchContextFlags			
 	
### -field __unnamed_union_0c3d_32 __unnamed_union_0c3d_32			
 	
### -field union EntryMethod			
 	
### -field __unnamed_union_0c3d_34 __unnamed_union_0c3d_34			
 	
### -field ULONG MinResidency			
 	
### -field ULONG WakeupLatency			
 	
### -field ULONG ResidencyCounterFrequency			
 	
### -field BOOLEAN IntegerEntryMethod			
 	
### -field PEP_PPM_LPI_REGISTER ResidencyCounter			
 	
### -field PEP_PPM_LPI_REGISTER UsageCounter			
 	
### -field PWSTR StateName			
 	
### -field ULONG DependencyCount			
 	
### -field PPEP_PPM_LPI_COORDINATED_DEPENDENCY Dependencies			
 	
### -field ULONG  : 1 Enabled			
 	
### -field ULONG  : 31 Reserved			
 	
### -field ULONG AsUlong			
 	
### -field ULONG  : 1 CoreContextLost			
 	
### -field ULONG  : 1 TraceContextLost			
 	
### -field ULONG  : 1 GICR			
 	
### -field ULONG  : 1 GICD			
 	
### -field ULONG  : 28 Reserved			
 	
### -field ULONG AsUlong			
 	
### -field PEP_PPM_LPI_REGISTER AsRegister			
 	
### -field ULONG64 AsInteger			
 	
## -remarks

## -see-also