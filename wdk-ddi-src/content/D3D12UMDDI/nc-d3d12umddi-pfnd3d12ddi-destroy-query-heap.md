---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROY_QUERY_HEAP
title: PFND3D12DDI_DESTROY_QUERY_HEAP
author: windows-driver-content
description: 
ms.assetid: 55aba8ed-32f3-414e-8154-cab2d29cf4bd
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

# PFND3D12DDI_DESTROY_QUERY_HEAP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROY_QUERY_HEAP Pfnd3d12ddiDestroyQueryHeap; 

// Definition

VOID Pfnd3d12ddiDestroyQueryHeap 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HQUERYHEAP
)
{...}

PFND3D12DDI_DESTROY_QUERY_HEAP 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HQUERYHEAP: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also