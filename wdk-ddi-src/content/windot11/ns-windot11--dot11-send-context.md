---
UID: NS.windot11._DOT11_SEND_CONTEXT
title: DOT11_SEND_CONTEXT
author: windows-driver-content
description: 
ms.assetid: b2a14c15-d847-426a-920a-d15d251bd016
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_SEND_CONTEXT, DOT11_SEND_CONTEXT, *PDOT11_SEND_CONTEXT
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

# DOT11_SEND_CONTEXT structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field PVOID pvReserved			
 	
### -field ULONG uFlags			
 	
### -field ULONG uPSLifetime			
 	
### -field ULONG uDelayedSleepValue			
 	
### -field UCHAR [8] ucTXDataRates			
 	
### -field BOOLEAN bIndicateAssociatedACKs			
 	
### -field BOOLEAN bIndicateTXStatus			
 	
### -field UCHAR ucPriority			
 	
### -field BOOLEAN bDontFragment			
 	
### -field ULONG dwExtendedStatus			
 	
### -field HANDLE hIntegrityOffload			
 	
### -field HANDLE hWEPOffload			
 	
### -field UCHAR ucWPAMSDUPriority			
 	
### -field UCHAR ucNumOfRWsOnPeer			
 	
### -field USHORT usAID			
 	
### -field PDOT11_PER_MSDU_COUNTERS pDot11PerMSDUCounters			
 	
## -remarks

## -see-also