---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032
title: PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032
author: windows-driver-content
description: 
ms.assetid: 7e4b6a40-1cde-4836-9d53-02b8dc4adb85
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

# PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032 Pfnd3d12ddiCalcprivatevideodecoderheapsize0032; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatevideodecoderheapsize0032 
(
	D3D12DDI_HDEVICE hDrvDevice
	CONST D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032 *pArgs
)
{...}

PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032 


```

## -parameters

### -param hDrvDevice: 
### -param *pArgs: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also