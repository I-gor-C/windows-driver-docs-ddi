---
UID: NC.d3d12umddi.PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003
title: PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003
author: windows-driver-content
description: 
ms.assetid: 2976f4e4-3882-4ad0-934b-c377ef08ddd4
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

# PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003 Pfnd3d12ddiClearDepthStencilView0003; 

// Definition

VOID Pfnd3d12ddiClearDepthStencilView0003 
(
	 D3D12DDI_HCOMMANDLIST
	D3D12DDI_CPU_DESCRIPTOR_HANDLE ViewCPUHandle
	 UINT
	 FLOAT
	 UINT8
	UINT NumRects
	CONST D3D12DDI_RECT *pRects
)
{...}

PFND3D12DDI_CLEAR_DEPTH_STENCIL_VIEW_0003 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param ViewCPUHandle: 
### -param UINT: 
### -param FLOAT: 
### -param UINT8: 
### -param NumRects: 
### -param *pRects: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also