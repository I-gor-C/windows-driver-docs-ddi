---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP
title: PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP
author: windows-driver-content
description: 
ms.assetid: 7d15cf21-584b-4d87-9ce5-e5856b6a34e8
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

# PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP Pfnd3d12ddiDestroyDescriptorHeap; 

// Definition

VOID Pfnd3d12ddiDestroyDescriptorHeap 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HDESCRIPTORHEAP
)
{...}

PFND3D12DDI_DESTROY_DESCRIPTOR_HEAP 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HDESCRIPTORHEAP: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also