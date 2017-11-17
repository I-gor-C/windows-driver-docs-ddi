---
UID: NS.windot11._DOT11_RECV_CONTEXT
title: DOT11_RECV_CONTEXT
author: windows-driver-content
description: 
ms.assetid: 80256767-1191-40bf-9e04-da060b33bfef
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_RECV_CONTEXT, DOT11_RECV_CONTEXT, *PDOT11_RECV_CONTEXT
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

# DOT11_RECV_CONTEXT structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field PVOID pvReserved			
 	
### -field DOT11_PHY_TYPE dot11PhyType			
 	
### -field ULONG uChCenterFrequency			
 	
### -field LONG lRSSI			
 	
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
 	
## -remarks

## -see-also