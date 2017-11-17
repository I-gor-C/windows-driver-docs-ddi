---
UID: NC.d3d12umddi.PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025
title: PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025
author: windows-driver-content
description: 
ms.assetid: 4cf4ccf9-41c3-4248-9e7e-732b66e01d62
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

# PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025 Pfnd3d12ddiCreatedepthstencilstate0025; 

// Definition

VOID Pfnd3d12ddiCreatedepthstencilstate0025 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDI_DEPTH_STENCIL_DESC_0025 *
	 D3D12DDI_HDEPTHSTENCILSTATE
)
{...}

PFND3D12DDI_CREATEDEPTHSTENCILSTATE_0025 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 
### -param D3D12DDI_HDEPTHSTENCILSTATE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also