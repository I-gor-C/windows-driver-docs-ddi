---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020
title: PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020
author: windows-driver-content
description: 
ms.assetid: bc769222-c510-4ded-8701-f198b2a4e034
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

# PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020 Pfnd3d12ddiVideoGetDecodeFormatCount0020; 

// Definition

UINT Pfnd3d12ddiVideoGetDecodeFormatCount0020 
(
	 D3D12DDI_HDEVICE
	UINT NodeIndex
	CONST D3D12DDI_VIDEO_DECODE_CONFIGURATION_0020 *
)
{...}

PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param NodeIndex: 
### -param *: 



## -returns

Returns UINT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also