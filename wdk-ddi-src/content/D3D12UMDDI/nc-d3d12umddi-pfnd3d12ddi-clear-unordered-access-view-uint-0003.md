---
UID: NC.d3d12umddi.PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003
title: PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003
author: windows-driver-content
description: 
ms.assetid: c58c8b47-e65c-4116-8ece-6f2b5c7f8367
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003 Pfnd3d12ddiClearUnorderedAccessViewUint0003; 

// Definition

VOID Pfnd3d12ddiClearUnorderedAccessViewUint0003 
(
	 D3D12DDI_HCOMMANDLIST
	D3D12DDI_GPU_DESCRIPTOR_HANDLE ViewGPUHandleInCurrentHeap
	D3D12DDI_CPU_DESCRIPTOR_HANDLE ViewCPUHandle
	D3D12DDI_HRESOURCE hDrvResource
	CONST UINT[4]
	UINT NumRects
	CONST D3D12DDI_RECT *pRects
)
{...}

PFND3D12DDI_CLEAR_UNORDERED_ACCESS_VIEW_UINT_0003 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param ViewGPUHandleInCurrentHeap: 
### -param ViewCPUHandle: 
### -param hDrvResource: 
### -param UINT[4]: 
### -param NumRects: 
### -param *pRects: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also