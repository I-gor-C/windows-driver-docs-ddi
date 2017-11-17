---
UID: NS.windot11._DOT11_RECV_EXTENSION_INFO
title: DOT11_RECV_EXTENSION_INFO
author: windows-driver-content
description: 
ms.assetid: 258ae48c-fe7a-4da5-be51-54bd0255c895
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_RECV_EXTENSION_INFO, DOT11_RECV_EXTENSION_INFO, *PDOT11_RECV_EXTENSION_INFO
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

# DOT11_RECV_EXTENSION_INFO structure

## -description



## -struct-fields

### -field ULONG uVersion			
 	
### -field PVOID pvReserved			
 	
### -field DOT11_PHY_TYPE dot11PhyType			
 	
### -field ULONG uChCenterFrequency			
 	
### -field LONG lRSSI			
 	
### -field LONG lRSSIMin			
 	
### -field LONG lRSSIMax			
 	
### -field ULONG uRSSI			
 	
### -field UCHAR ucPriority			
 	
### -field UCHAR ucDataRate			
 	
### -field UCHAR [6] ucPeerMacAddress			
 	
### -field ULONG dwExtendedStatus			
 	
### -field HANDLE hWEPOffloadContext			
 	
### -field HANDLE hAuthOffloadContext			
 	
### -field USHORT usWEPAppliedMask			
 	
### -field USHORT usWPAMSDUPriority			
 	
### -field DOT11_IV48_COUNTER dot11LowestIV48Counter			
 	
### -field USHORT usDot11LeftRWBitMap			
 	
### -field DOT11_IV48_COUNTER dot11HighestIV48Counter			
 	
### -field USHORT usDot11RightRWBitMap			
 	
### -field USHORT usNumberOfMPDUsReceived			
 	
### -field USHORT usNumberOfFragments			
 	
### -field PVOID [1] pNdisPackets			
 	
## -remarks

## -see-also