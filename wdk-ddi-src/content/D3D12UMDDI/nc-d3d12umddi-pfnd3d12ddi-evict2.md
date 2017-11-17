---
UID: NC.d3d12umddi.PFND3D12DDI_EVICT2
title: PFND3D12DDI_EVICT2
author: windows-driver-content
description: 
ms.assetid: b2324af7-3b4b-4ec4-b65d-2ac2e670d397
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

# PFND3D12DDI_EVICT2 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_EVICT2 Pfnd3d12ddiEvict2; 

// Definition

HRESULT Pfnd3d12ddiEvict2 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_EVICT *
)
{...}

PFND3D12DDI_EVICT2 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also