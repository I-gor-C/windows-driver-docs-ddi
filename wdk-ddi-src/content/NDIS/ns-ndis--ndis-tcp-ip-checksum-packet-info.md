---
UID: NS.ndis._NDIS_TCP_IP_CHECKSUM_PACKET_INFO
title: NDIS_TCP_IP_CHECKSUM_PACKET_INFO
author: windows-driver-content
description: 
ms.assetid: 506825a8-1390-4bcd-96d0-dc8eaaff6e8a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_TCP_IP_CHECKSUM_PACKET_INFO, NDIS_TCP_IP_CHECKSUM_PACKET_INFO, *PNDIS_TCP_IP_CHECKSUM_PACKET_INFO
req.header: ndis.h
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

# NDIS_TCP_IP_CHECKSUM_PACKET_INFO structure

## -description



## -struct-fields

### -field union __unnamed_union_0c0c_8			
 	
### -field ULONG  : 1 NdisPacketChecksumV4			
 	
### -field ULONG  : 1 NdisPacketChecksumV6			
 	
### -field ULONG  : 1 NdisPacketTcpChecksum			
 	
### -field ULONG  : 1 NdisPacketUdpChecksum			
 	
### -field ULONG  : 1 NdisPacketIpChecksum			
 	
### -field ULONG  : 1 NdisPacketTcpChecksumFailed			
 	
### -field ULONG  : 1 NdisPacketUdpChecksumFailed			
 	
### -field ULONG  : 1 NdisPacketIpChecksumFailed			
 	
### -field ULONG  : 1 NdisPacketTcpChecksumSucceeded			
 	
### -field ULONG  : 1 NdisPacketUdpChecksumSucceeded			
 	
### -field ULONG  : 1 NdisPacketIpChecksumSucceeded			
 	
### -field ULONG  : 1 NdisPacketLoopback			
 	
### -field ULONG Value			
 	
## -remarks

## -see-also