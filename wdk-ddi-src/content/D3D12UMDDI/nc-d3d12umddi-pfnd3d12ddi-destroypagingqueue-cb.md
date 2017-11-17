---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYPAGINGQUEUE_CB
title: PFND3D12DDI_DESTROYPAGINGQUEUE_CB
author: windows-driver-content
description: 
ms.assetid: f8839d69-fc71-44bf-8ce6-9b5657eb74f6
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

# PFND3D12DDI_DESTROYPAGINGQUEUE_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYPAGINGQUEUE_CB Pfnd3d12ddiDestroypagingqueueCb; 

// Definition

HRESULT Pfnd3d12ddiDestroypagingqueueCb 
(
	D3D12DDI_HRTCOMMANDQUEUE hRTCommandQueue
	 const D3DDDI_DESTROYPAGINGQUEUE *
)
{...}

PFND3D12DDI_DESTROYPAGINGQUEUE_CB 


```

## -parameters

### -param hRTCommandQueue: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also