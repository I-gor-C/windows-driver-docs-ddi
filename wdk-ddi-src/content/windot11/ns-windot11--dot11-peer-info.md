---
UID: NS.windot11._DOT11_PEER_INFO
title: DOT11_PEER_INFO
author: windows-driver-content
description: 
ms.assetid: 2918fb54-4aed-4511-9dce-9b98f5cc68cc
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DOT11_PEER_INFO, 
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

# DOT11_PEER_INFO structure

## -description



## -struct-fields

### -field DOT11_MAC_ADDRESS MacAddress			
 	
### -field USHORT usCapabilityInformation			
 	
### -field DOT11_AUTH_ALGORITHM AuthAlgo			
 	
### -field DOT11_CIPHER_ALGORITHM UnicastCipherAlgo			
 	
### -field DOT11_CIPHER_ALGORITHM MulticastCipherAlgo			
 	
### -field BOOLEAN bWpsEnabled			
 	
### -field USHORT usListenInterval			
 	
### -field UCHAR [MAX_NUM_SUPPORTED_RATES_V2] ucSupportedRates			
 	
### -field USHORT usAssociationID			
 	
### -field DOT11_ASSOCIATION_STATE AssociationState			
 	
### -field DOT11_POWER_MODE PowerMode			
 	
### -field LARGE_INTEGER liAssociationUpTime			
 	
### -field DOT11_PEER_STATISTICS Statistics			
 	
## -remarks

## -see-also