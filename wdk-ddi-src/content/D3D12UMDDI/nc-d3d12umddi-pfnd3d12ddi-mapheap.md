---
UID: NC.d3d12umddi.PFND3D12DDI_MAPHEAP
title: PFND3D12DDI_MAPHEAP
author: windows-driver-content
description: 
ms.assetid: 8b4e8212-ac58-4ff6-9750-d944a1c9578d
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

# PFND3D12DDI_MAPHEAP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_MAPHEAP Pfnd3d12ddiMapheap; 

// Definition

HRESULT Pfnd3d12ddiMapheap 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HHEAP
	VOID **
)
{...}

PFND3D12DDI_MAPHEAP 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HHEAP: 
### -param **: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also