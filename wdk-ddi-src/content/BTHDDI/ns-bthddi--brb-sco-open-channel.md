---
UID: NS.bthddi._BRB_SCO_OPEN_CHANNEL
title: BRB_SCO_OPEN_CHANNEL
author: windows-driver-content
description: 
ms.assetid: 974e887b-37d8-4bd5-99e5-5000099ac6dd
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: BRB_SCO_OPEN_CHANNEL, 
req.header: bthddi.h
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

# BRB_SCO_OPEN_CHANNEL structure

## -description



## -struct-fields

### -field BRB_HEADER Hdr			
 	
### -field BTH_ADDR BtAddress			
 	
### -field ULONG TransmitBandwidth			
 	
### -field ULONG ReceiveBandwidth			
 	
### -field USHORT MaxLatency			
 	
### -field USHORT PacketType			
 	
### -field USHORT ContentFormat			
 	
### -field USHORT Reserved			
 	
### -field SCO_RETRANSMISSION_EFFORT RetransmissionEffort			
 	
### -field ULONG ChannelFlags			
 	
### -field ULONG CallbackFlags			
 	
### -field PFNSCO_INDICATION_CALLBACK Callback			
 	
### -field PVOID CallbackContext			
 	
### -field PVOID ReferenceObject			
 	
### -field SCO_CHANNEL_HANDLE ChannelHandle			
 	
### -field UCHAR Response			
 	
## -remarks

## -see-also