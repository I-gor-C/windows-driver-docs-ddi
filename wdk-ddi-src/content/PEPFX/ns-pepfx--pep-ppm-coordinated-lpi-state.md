---
UID: NS.pepfx._PEP_PPM_COORDINATED_LPI_STATE
title: PEP_PPM_COORDINATED_LPI_STATE
author: windows-driver-content
description: 
ms.assetid: 9ceb20c3-0580-4fce-ae3d-f5bb6499dd3c
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PEP_PPM_COORDINATED_LPI_STATE, PEP_PPM_COORDINATED_LPI_STATE, *PPEP_PPM_COORDINATED_LPI_STATE
req.header: pepfx.h
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
 	
### -field __unnamed_union_0c3c_20 __unnamed_union_0c3c_20			
 	
### -field union ArchContextFlags			
 	
### -field __unnamed_union_0c3c_22 __unnamed_union_0c3c_22			
 	
### -field union EntryMethod			
 	
### -field __unnamed_union_0c3c_24 __unnamed_union_0c3c_24			
 	
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