---
UID: NS.d3dukmdt.D3DDDI_UPDATEALLOCPROPERTY
title: D3DDDI_UPDATEALLOCPROPERTY
author: windows-driver-content
description: 
ms.assetid: a0496351-18a8-4076-88e1-1a35b690f21a
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: D3DDDI_UPDATEALLOCPROPERTY, D3DDDI_UPDATEALLOCPROPERTY
req.header: d3dukmdt.h
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

# D3DDDI_UPDATEALLOCPROPERTY structure

## -description



## -struct-fields

### -field union __unnamed_union_0ad4_58			
 	
### -field D3DKMT_HANDLE hPagingQueue			
 	
### -field D3DKMT_HANDLE hAllocation			
 	
### -field UINT SupportedSegmentSet			
 	
### -field D3DDDI_SEGMENTPREFERENCE PreferredSegment			
 	
### -field D3DDDI_UPDATEALLOCPROPERTY_FLAGS Flags			
 	
### -field UINT64 PagingFenceValue			
 	
### -field UINT  : 1 SetAccessedPhysically			
 	
### -field UINT  : 1 SetSupportedSegmentSet			
 	
### -field UINT  : 1 SetPreferredSegment			
 	
### -field UINT  : 29 Reserved			
 	
### -field UINT PropertyMaskValue			
 	
## -remarks

## -see-also