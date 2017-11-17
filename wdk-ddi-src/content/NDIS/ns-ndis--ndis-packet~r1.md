---
UID: NS.ndis._NDIS_PACKET~r1
title: NDIS_PACKET
author: windows-driver-content
description: 
ms.assetid: 736c1eec-909f-4247-aff7-c0dbf477584d
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NDIS_PACKET, NDIS_PACKET, *PNDIS_PACKET, **PPNDIS_PACKET
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

# NDIS_PACKET structure

## -description



## -struct-fields

### -field union __unnamed_union_0c0c_4			
 	
### -field NDIS_PACKET_PRIVATE Private			
 	
### -field ULONG_PTR [2] Reserved			
 	
### -field UCHAR [1] ProtocolReserved			
 	
### -field UCHAR [2 * sizeof(PVOID)] MiniportReserved			
 	
### -field UCHAR [2 * sizeof(PVOID)] WrapperReserved			
 	
### -field UCHAR [3 * sizeof(PVOID)] MiniportReservedEx			
 	
### -field UCHAR [sizeof(PVOID)] WrapperReservedEx			
 	
### -field UCHAR [4 * sizeof(PVOID)] MacReserved			
 	
## -remarks

## -see-also