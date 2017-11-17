---
UID: NS.netpacket._NET_PACKET_ADVANCED_OFFLOAD
title: NET_PACKET_ADVANCED_OFFLOAD
author: windows-driver-content
description: 
ms.assetid: 0a1cbe6b-ab9f-4a9a-8cdf-91f420ab23fa
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NET_PACKET_ADVANCED_OFFLOAD, NET_PACKET_ADVANCED_OFFLOAD
req.header: netpacket.h
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

# NET_PACKET_ADVANCED_OFFLOAD structure

## -description



## -struct-fields

### -field UINT16  : 1 InsertVlanHeader			
 	
### -field UINT16  : 1 InsertNestedVlanHeader			
 	
### -field UINT16  : 4 InsertEncapsulationHeader			
 	
### -field UINT16  : 10 Reserved1			
 	
### -field NET_PACKET_LAYOUT EncapsulatedLayout			
 	
### -field NET_PACKET_CHECKSUM EncapsulatedChecksum			
 	
### -field NET_PACKET_8021Q_HEADER VlanHeader			
 	
### -field NET_PACKET_8021Q_HEADER NestedVlanHeader			
 	
### -field UINT32  : 20 TcpMss			
 	
### -field UINT32  : 12 Reserved2			
 	
### -field UINT32  : 24 VirtualSubnetId			
 	
### -field UINT32  : 8 Reserved3			
 	
## -remarks

## -see-also