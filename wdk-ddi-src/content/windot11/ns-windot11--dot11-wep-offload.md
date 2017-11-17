---
UID: NS.windot11._DOT11_WEP_OFFLOAD
title: DOT11_WEP_OFFLOAD
author: windows-driver-content
description: 
ms.assetid: 7339d3d9-4048-4487-8bff-e0017f440e86
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_WEP_OFFLOAD, DOT11_WEP_OFFLOAD, *PDOT11_WEP_OFFLOAD
req.header: windot11.h
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

# DOT11_WEP_OFFLOAD structure

## -description



## -struct-fields

### -field ULONG uReserved			
 	
### -field HANDLE hOffloadContext			
 	
### -field HANDLE hOffload			
 	
### -field DOT11_OFFLOAD_TYPE dot11OffloadType			
 	
### -field ULONG dwAlgorithm			
 	
### -field BOOLEAN bRowIsOutbound			
 	
### -field BOOLEAN bUseDefault			
 	
### -field ULONG uFlags			
 	
### -field UCHAR [6] ucMacAddress			
 	
### -field ULONG uNumOfRWsOnPeer			
 	
### -field ULONG uNumOfRWsOnMe			
 	
### -field DOT11_IV48_COUNTER [16] dot11IV48Counters			
 	
### -field USHORT [16] usDot11RWBitMaps			
 	
### -field USHORT usKeyLength			
 	
### -field UCHAR [1] ucKey			
 	
## -remarks

## -see-also