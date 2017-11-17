---
UID: NS.windot11._DOT11_SEND_EXTENSION_INFO
title: DOT11_SEND_EXTENSION_INFO
author: windows-driver-content
description: 
ms.assetid: d8865e41-b898-4283-820b-49ce352631ed
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_SEND_EXTENSION_INFO, DOT11_SEND_EXTENSION_INFO, *PDOT11_SEND_EXTENSION_INFO
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

# DOT11_SEND_EXTENSION_INFO structure

## -description



## -struct-fields

### -field ULONG uVersion			
 	
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
 	
### -field USHORT usNumberOfFragments			
 	
### -field DOT11_FRAGMENT_DESCRIPTOR [1] Dot11FragmentDescriptors			
 	
## -remarks

## -see-also