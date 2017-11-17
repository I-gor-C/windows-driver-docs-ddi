---
UID: NC.d3d12umddi.PFND3D12DDI_CREATEVIDEOPROCESSOR_0032
title: PFND3D12DDI_CREATEVIDEOPROCESSOR_0032
author: windows-driver-content
description: 
ms.assetid: 00692dc1-dc4b-4374-9444-33ef0da2ef6f
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

# PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 Pfnd3d12ddiCreatevideoprocessor0032; 

// Definition

HRESULT Pfnd3d12ddiCreatevideoprocessor0032 
(
	D3D12DDI_HDEVICE hDrvDevice
	CONST D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032 *pArgs
	D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
)
{...}

PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 


```

## -parameters

### -param hDrvDevice: 
### -param *pArgs: 
### -param hDrvVideoProcessor: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also