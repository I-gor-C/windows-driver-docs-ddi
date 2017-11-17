---
UID: NS.ntddndis._NDIS_QOS_OFFLOAD_CAPABILITIES
title: NDIS_QOS_OFFLOAD_CAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 7161364e-5b49-442e-ae81-9d4b10cb3a56
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_QOS_OFFLOAD_CAPABILITIES, NDIS_QOS_OFFLOAD_CAPABILITIES, *PNDIS_QOS_OFFLOAD_CAPABILITIES
req.header: ntddndis.h
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

# NDIS_QOS_OFFLOAD_CAPABILITIES structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field ULONG Flags			
 	
### -field ULONG SupportedSqTypes			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TransmitCapSupported			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TransmitReservationSupported			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] ReceiveCapSupported			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TransmitGftCapSupported			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] ReceiveGftCapSupported			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TcSupportedTable			
 	
### -field ULONG NumStandardSqsSupported			
 	
### -field ULONG NumGftSqsSupported			
 	
### -field ULONG ReservationGranularitySupported			
 	
### -field ULONG MaxNumSqInputs			
 	
## -remarks

## -see-also