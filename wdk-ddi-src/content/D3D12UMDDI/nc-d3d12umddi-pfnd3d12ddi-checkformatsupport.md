---
UID: NC.d3d12umddi.PFND3D12DDI_CHECKFORMATSUPPORT
title: PFND3D12DDI_CHECKFORMATSUPPORT
author: windows-driver-content
description: 
ms.assetid: 72ad57d7-1a1b-4281-b1f2-b5d96eb8b367
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

# PFND3D12DDI_CHECKFORMATSUPPORT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CHECKFORMATSUPPORT Pfnd3d12ddiCheckformatsupport; 

// Definition

VOID Pfnd3d12ddiCheckformatsupport 
(
	 D3D12DDI_HDEVICE
	 DXGI_FORMAT
	UINT *
)
{...}

PFND3D12DDI_CHECKFORMATSUPPORT 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param DXGI_FORMAT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also