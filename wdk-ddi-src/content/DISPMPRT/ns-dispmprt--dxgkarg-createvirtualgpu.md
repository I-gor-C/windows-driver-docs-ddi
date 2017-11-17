---
UID: NS.dispmprt._DXGKARG_CREATEVIRTUALGPU
title: DXGKARG_CREATEVIRTUALGPU
author: windows-driver-content
description: 
ms.assetid: 674fea82-7ff1-47df-9465-633b236fa95f
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: DXGKARG_CREATEVIRTUALGPU, DXGKARG_CREATEVIRTUALGPU, *PDXGKARG_CREATEVIRTUALGPU
req.header: dispmprt.h
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

# DXGKARG_CREATEVIRTUALGPU structure

## -description



## -struct-fields

### -field ULONG PartitionId			
 	
### -field DXGK_VIRTUALGPUPROFILE Profile			
 	
### -field CLSID UserModeVirtualDeviceProvider			
 	
### -field LUID VirtualGpuLuid			
 	
### -field ULONG NumMemorySegments			
 	
### -field DXGK_VIRTUALGPUSEGMENTINFO [DXGK_MAX_VIRTUAL_GPU_ALLOCATIONS] SegmentInfo			
 	
### -field ULONG NumEngines			
 	
### -field DXGK_VIRTUALGPUENGINEINFO [DXGK_MAX_ASYMETRICAL_PROCESSING_NODES] EngineInfo			
 	
## -remarks

## -see-also