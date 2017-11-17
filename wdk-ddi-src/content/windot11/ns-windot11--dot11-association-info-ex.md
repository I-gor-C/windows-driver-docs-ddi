---
UID: NS.windot11._DOT11_ASSOCIATION_INFO_EX
title: DOT11_ASSOCIATION_INFO_EX
author: windows-driver-content
description: 
ms.assetid: c58251c1-ed2e-49e4-82fb-d2de0642f020
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_ASSOCIATION_INFO_EX, DOT11_ASSOCIATION_INFO_EX, *PDOT11_ASSOCIATION_INFO_EX
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

# DOT11_ASSOCIATION_INFO_EX structure

## -description



## -struct-fields

### -field DOT11_MAC_ADDRESS PeerMacAddress			
 	
### -field DOT11_MAC_ADDRESS BSSID			
 	
### -field USHORT usCapabilityInformation			
 	
### -field USHORT usListenInterval			
 	
### -field UCHAR [MAX_NUM_SUPPORTED_RATES_V2] ucPeerSupportedRates			
 	
### -field USHORT usAssociationID			
 	
### -field DOT11_ASSOCIATION_STATE dot11AssociationState			
 	
### -field DOT11_POWER_MODE dot11PowerMode			
 	
### -field LARGE_INTEGER liAssociationUpTime			
 	
### -field ULONGLONG ullNumOfTxPacketSuccesses			
 	
### -field ULONGLONG ullNumOfTxPacketFailures			
 	
### -field ULONGLONG ullNumOfRxPacketSuccesses			
 	
### -field ULONGLONG ullNumOfRxPacketFailures			
 	
## -remarks

## -see-also