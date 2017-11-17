---
UID: NS.netringbuffer._NET_RING_BUFFER
title: NET_RING_BUFFER
author: windows-driver-content
description: 
ms.assetid: 36e2de48-0723-4ecc-b91b-18402227c89e
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: NET_RING_BUFFER, NET_RING_BUFFER, *PNET_RING_BUFFER
req.header: netringbuffer.h
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

# NET_RING_BUFFER structure

## -description



## -struct-fields

### -field UINT16 OSReserved1			
 	
### -field UINT16 ElementStride			
 	
### -field UINT32 NumberOfElements			
 	
### -field UINT32 ElementIndexMask			
 	
### -field UINT32 BeginIndex			
 	
### -field UINT32 NextIndex			
 	
### -field UINT32 EndIndex			
 	
### -field VOID * [2] NetAdapterScratch			
 	
### -field VOID * [3] OSReserved2			
 	
### -field BYTE [ANYSIZE_ARRAY] Buffer			
 	
## -remarks

## -see-also