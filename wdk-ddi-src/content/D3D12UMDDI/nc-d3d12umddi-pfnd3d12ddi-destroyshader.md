---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYSHADER
title: PFND3D12DDI_DESTROYSHADER
author: windows-driver-content
description: 
ms.assetid: 075d72e7-6ec6-48f2-9d16-54cd0f0b17a6
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

# PFND3D12DDI_DESTROYSHADER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYSHADER Pfnd3d12ddiDestroyshader; 

// Definition

VOID Pfnd3d12ddiDestroyshader 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HSHADER
)
{...}

PFND3D12DDI_DESTROYSHADER 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HSHADER: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also