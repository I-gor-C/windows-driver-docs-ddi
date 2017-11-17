---
UID: NC.d3d12umddi.PFND3D12DDI_CREATEVIDEODECODER_0021
title: PFND3D12DDI_CREATEVIDEODECODER_0021
author: windows-driver-content
description: 
ms.assetid: ad1fab66-7ab0-4e02-a818-f0fab2c09c6b
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

# PFND3D12DDI_CREATEVIDEODECODER_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATEVIDEODECODER_0021 Pfnd3d12ddiCreatevideodecoder0021; 

// Definition

HRESULT Pfnd3d12ddiCreatevideodecoder0021 
(
	D3D12DDI_HDEVICE hDrvDevice
	CONST D3D12DDIARG_CREATE_VIDEO_DECODER_0021 *pArgs
	D3D12DDI_HVIDEODECODER_0020 hDrvVideoDecoder
)
{...}

PFND3D12DDI_CREATEVIDEODECODER_0021 


```

## -parameters

### -param hDrvDevice: 
### -param *pArgs: 
### -param hDrvVideoDecoder: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also