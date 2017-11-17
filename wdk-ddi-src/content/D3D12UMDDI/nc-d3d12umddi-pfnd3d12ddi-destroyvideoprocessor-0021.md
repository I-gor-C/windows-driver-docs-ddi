---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021
title: PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021
author: windows-driver-content
description: 
ms.assetid: ea950ea8-3ab2-4e6c-be36-1541c1950991
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

# PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021 Pfnd3d12ddiDestroyvideoprocessor0021; 

// Definition

VOID Pfnd3d12ddiDestroyvideoprocessor0021 
(
	D3D12DDI_HDEVICE hDrvDevice
	D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
)
{...}

PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021 


```

## -parameters

### -param hDrvDevice: 
### -param hDrvVideoProcessor: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also