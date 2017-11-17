---
UID: NC.d3dkmddi.DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES
title: DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES
author: windows-driver-content
description: 
ms.assetid: 9f233012-7406-4cee-bfdc-bb333cb0e3b4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
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

# DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES DxgkcbUnblockuefiframebufferranges; 

// Definition

NTSTATUS DxgkcbUnblockuefiframebufferranges 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGK_SEGMENTMEMORYSTATE pSegmentMemoryState
)
{...}

DXGKCB_UNBLOCKUEFIFRAMEBUFFERRANGES 


```

## -parameters

### -param hAdapter: 
### -param pSegmentMemoryState: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also