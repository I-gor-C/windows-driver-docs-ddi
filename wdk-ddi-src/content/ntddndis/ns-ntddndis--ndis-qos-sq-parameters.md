---
UID: NS.ntddndis._NDIS_QOS_SQ_PARAMETERS
title: NDIS_QOS_SQ_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 56c959d2-2025-474c-8295-12bb38c13678
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_QOS_SQ_PARAMETERS, NDIS_QOS_SQ_PARAMETERS, *PNDIS_QOS_SQ_PARAMETERS
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

# NDIS_QOS_SQ_PARAMETERS structure

## -description



## -struct-fields

### -field NDIS_OBJECT_HEADER Header			
 	
### -field ULONG Flags			
 	
### -field NDIS_QOS_SQ_ID SqId			
 	
### -field NDIS_QOS_SQ_TYPE SqType			
 	
### -field BOOLEAN [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TcEnabledTable			
 	
### -field ULONG [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TcTransmitBandwidthCapTable			
 	
### -field ULONG [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TcTransmitBandwidthReservationTable			
 	
### -field ULONG [NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES] TcReceiveBandwidthCapTable			
 	
## -remarks

## -see-also