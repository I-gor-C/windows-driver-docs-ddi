---
UID: NC.d3d12umddi.PFND3D12DDI_SET_ROOT_BUFFER_VIEW
title: PFND3D12DDI_SET_ROOT_BUFFER_VIEW
author: windows-driver-content
description: 
ms.assetid: dc093a8d-7983-43bd-9aa1-f757af0972c3
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

# PFND3D12DDI_SET_ROOT_BUFFER_VIEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SET_ROOT_BUFFER_VIEW Pfnd3d12ddiSetRootBufferView; 

// Definition

VOID Pfnd3d12ddiSetRootBufferView 
(
	 D3D12DDI_HCOMMANDLIST
	UINT RootParameterIndex
	D3D12DDI_GPU_VIRTUAL_ADDRESS BufferLocation
)
{...}

PFND3D12DDI_SET_ROOT_BUFFER_VIEW 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param RootParameterIndex: 
### -param BufferLocation: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also