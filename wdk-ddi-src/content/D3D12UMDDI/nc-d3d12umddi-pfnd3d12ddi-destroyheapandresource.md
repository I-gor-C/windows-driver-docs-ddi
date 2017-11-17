---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYHEAPANDRESOURCE
title: PFND3D12DDI_DESTROYHEAPANDRESOURCE
author: windows-driver-content
description: 
ms.assetid: 6a15019c-2725-4093-84a8-816c5cfbc19a
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

# PFND3D12DDI_DESTROYHEAPANDRESOURCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYHEAPANDRESOURCE Pfnd3d12ddiDestroyheapandresource; 

// Definition

VOID Pfnd3d12ddiDestroyheapandresource 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HHEAP
	 D3D12DDI_HRESOURCE
)
{...}

PFND3D12DDI_DESTROYHEAPANDRESOURCE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HHEAP: 
### -param D3D12DDI_HRESOURCE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also