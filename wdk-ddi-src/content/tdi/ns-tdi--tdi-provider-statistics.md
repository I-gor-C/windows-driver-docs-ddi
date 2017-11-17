---
UID: NS.tdi._TDI_PROVIDER_STATISTICS
title: TDI_PROVIDER_STATISTICS
author: windows-driver-content
description: 
ms.assetid: ba85d317-32b4-40b3-931f-90cdfd6c6573
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: TDI_PROVIDER_STATISTICS, TDI_PROVIDER_STATISTICS, *PTDI_PROVIDER_STATISTICS
req.header: tdi.h
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

# TDI_PROVIDER_STATISTICS structure

## -description



## -struct-fields

### -field ULONG Version			
 	
### -field ULONG OpenConnections			
 	
### -field ULONG ConnectionsAfterNoRetry			
 	
### -field ULONG ConnectionsAfterRetry			
 	
### -field ULONG LocalDisconnects			
 	
### -field ULONG RemoteDisconnects			
 	
### -field ULONG LinkFailures			
 	
### -field ULONG AdapterFailures			
 	
### -field ULONG SessionTimeouts			
 	
### -field ULONG CancelledConnections			
 	
### -field ULONG RemoteResourceFailures			
 	
### -field ULONG LocalResourceFailures			
 	
### -field ULONG NotFoundFailures			
 	
### -field ULONG NoListenFailures			
 	
### -field ULONG DatagramsSent			
 	
### -field LARGE_INTEGER DatagramBytesSent			
 	
### -field ULONG DatagramsReceived			
 	
### -field LARGE_INTEGER DatagramBytesReceived			
 	
### -field ULONG PacketsSent			
 	
### -field ULONG PacketsReceived			
 	
### -field ULONG DataFramesSent			
 	
### -field LARGE_INTEGER DataFrameBytesSent			
 	
### -field ULONG DataFramesReceived			
 	
### -field LARGE_INTEGER DataFrameBytesReceived			
 	
### -field ULONG DataFramesResent			
 	
### -field LARGE_INTEGER DataFrameBytesResent			
 	
### -field ULONG DataFramesRejected			
 	
### -field LARGE_INTEGER DataFrameBytesRejected			
 	
### -field ULONG ResponseTimerExpirations			
 	
### -field ULONG AckTimerExpirations			
 	
### -field ULONG MaximumSendWindow			
 	
### -field ULONG AverageSendWindow			
 	
### -field ULONG PiggybackAckQueued			
 	
### -field ULONG PiggybackAckTimeouts			
 	
### -field LARGE_INTEGER WastedPacketSpace			
 	
### -field ULONG WastedSpacePackets			
 	
### -field ULONG NumberOfResources			
 	
### -field TDI_PROVIDER_RESOURCE_STATS [1] ResourceStats			
 	
## -remarks

## -see-also