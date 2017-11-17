---
UID: NC.d3d12umddi.PFND3D12DDI_GETPAGEABLESIZE_0020
title: PFND3D12DDI_GETPAGEABLESIZE_0020
author: windows-driver-content
description: 
ms.assetid: 54eafb98-5714-4cbf-bbfe-8c0a8b2e40c4
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

# PFND3D12DDI_GETPAGEABLESIZE_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GETPAGEABLESIZE_0020 Pfnd3d12ddiGetpageablesize0020; 

// Definition

UINT64 Pfnd3d12ddiGetpageablesize0020 
(
	D3D12DDI_HDEVICE hDrvDevice
	CONST D3D12DDIARG_GET_PAGEABLE_SIZE_0020 *pArgs
)
{...}

PFND3D12DDI_GETPAGEABLESIZE_0020 


```

## -parameters

### -param hDrvDevice: 
### -param *pArgs: 



## -returns

Returns UINT64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also