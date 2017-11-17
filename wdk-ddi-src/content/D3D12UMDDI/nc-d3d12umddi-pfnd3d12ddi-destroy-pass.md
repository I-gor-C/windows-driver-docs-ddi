---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROY_PASS
title: PFND3D12DDI_DESTROY_PASS
author: windows-driver-content
description: 
ms.assetid: 8a19af64-1f80-4137-b2fd-cf59b485fab1
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

# PFND3D12DDI_DESTROY_PASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROY_PASS Pfnd3d12ddiDestroyPass; 

// Definition

VOID Pfnd3d12ddiDestroyPass 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HPASS
)
{...}

PFND3D12DDI_DESTROY_PASS 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HPASS: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also