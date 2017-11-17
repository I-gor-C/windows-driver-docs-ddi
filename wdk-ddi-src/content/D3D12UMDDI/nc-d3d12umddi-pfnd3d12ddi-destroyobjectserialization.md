---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYOBJECTSERIALIZATION
title: PFND3D12DDI_DESTROYOBJECTSERIALIZATION
author: windows-driver-content
description: 
ms.assetid: fff3327a-50df-4b0c-95b2-d8ad9f628d19
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

# PFND3D12DDI_DESTROYOBJECTSERIALIZATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYOBJECTSERIALIZATION Pfnd3d12ddiDestroyobjectserialization; 

// Definition

VOID Pfnd3d12ddiDestroyobjectserialization 
(
	D3D12DDI_HDEVICE hDevice
	SIZE_T BlobSize
	CONST UINT *pBlob
)
{...}

PFND3D12DDI_DESTROYOBJECTSERIALIZATION 


```

## -parameters

### -param hDevice: 
### -param BlobSize: 
### -param *pBlob: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also