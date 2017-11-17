---
UID: NC.d3d12umddi.PFND3D12DDI_EVICT_CB
title: PFND3D12DDI_EVICT_CB
author: windows-driver-content
description: 
ms.assetid: fcb13111-4f7e-4351-a47f-c01a9591d16a
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

# PFND3D12DDI_EVICT_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_EVICT_CB Pfnd3d12ddiEvictCb; 

// Definition

HRESULT Pfnd3d12ddiEvictCb 
(
	D3D12DDI_HRTDEVICE hRTDevice
	 const D3DDDICB_EVICT *
)
{...}

PFND3D12DDI_EVICT_CB 


```

## -parameters

### -param hRTDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also