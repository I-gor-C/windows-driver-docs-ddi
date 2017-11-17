---
UID: NS.poclass._PCC_HEADER
title: PCC_HEADER
author: windows-driver-content
description: 
ms.assetid: ab8dec28-84bf-44b7-85a8-e6136eeb7c87
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: PCC_HEADER, PCC_HEADER, *PPCC_HEADER
req.header: poclass.h
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

# PCC_HEADER structure

## -description



## -struct-fields

### -field union SupportedFeatures			
 	
### -field __unnamed_union_0af1_5 __unnamed_union_0af1_5			
 	
### -field union Command			
 	
### -field __unnamed_union_0af1_7 __unnamed_union_0af1_7			
 	
### -field union Status			
 	
### -field __unnamed_union_0af1_9 __unnamed_union_0af1_9			
 	
### -field ULONG Signature			
 	
### -field USHORT HeaderLength			
 	
### -field UCHAR MajorVersion			
 	
### -field UCHAR MinorVersion			
 	
### -field ULONG Latency			
 	
### -field ULONG MinimumCommandInterval			
 	
### -field ULONG MaximumCommandInterval			
 	
### -field ULONG NominalFrequency			
 	
### -field ULONG MinimumFrequency			
 	
### -field ULONG MinimumUnthrottledFrequency			
 	
### -field ULONG  : 1 SciDoorbell			
 	
### -field ULONG  : 31 Reserved			
 	
### -field ULONG AsULong			
 	
### -field USHORT  : 8 CommandCode			
 	
### -field USHORT  : 7 ReservedZ			
 	
### -field USHORT  : 1 SciDoorbell			
 	
### -field USHORT AsUShort			
 	
### -field USHORT  : 1 CommandComplete			
 	
### -field USHORT  : 1 SciReceived			
 	
### -field USHORT  : 1 Error			
 	
### -field USHORT  : 13 Reserved			
 	
### -field USHORT AsUShort			
 	
## -remarks

## -see-also