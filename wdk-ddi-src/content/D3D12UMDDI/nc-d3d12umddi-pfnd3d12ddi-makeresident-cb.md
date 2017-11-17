---
UID: NC.d3d12umddi.PFND3D12DDI_MAKERESIDENT_CB
title: PFND3D12DDI_MAKERESIDENT_CB
author: windows-driver-content
description: 
ms.assetid: 2bee4a43-f4f0-4f50-bb96-3bdb73803cf2
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

# PFND3D12DDI_MAKERESIDENT_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_MAKERESIDENT_CB Pfnd3d12ddiMakeresidentCb; 

// Definition

HRESULT Pfnd3d12ddiMakeresidentCb 
(
	D3D12DDI_HRTDEVICE hRTDevice
	D3D12DDI_HRTPAGINGQUEUE hRTPagingQueue
	D3DDDI_MAKERESIDENT *
)
{...}

PFND3D12DDI_MAKERESIDENT_CB 


```

## -parameters

### -param hRTDevice: 
### -param hRTPagingQueue: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also