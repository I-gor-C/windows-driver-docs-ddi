---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_DECODE_FRAME_0021
title: PFND3D12DDI_VIDEO_DECODE_FRAME_0021
author: windows-driver-content
description: 
ms.assetid: 2ed3dca5-53d5-42f2-923e-acb287faa9f0
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

# PFND3D12DDI_VIDEO_DECODE_FRAME_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_VIDEO_DECODE_FRAME_0021 Pfnd3d12ddiVideoDecodeFrame0021; 

// Definition

VOID Pfnd3d12ddiVideoDecodeFrame0021 
(
	D3D12DDI_HCOMMANDLIST hDrvCommandList
	D3D12DDI_HVIDEODECODER_0020 hDrvDecoder
	UINT64 SubmissionID
	 const D3D12DDI_VIDEO_DECODE_OUTPUT_STREAM_ARGUMENTS_0021 *pOutputStreamParameters
	 const D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0020 *pInputStreamParameters
)
{...}

PFND3D12DDI_VIDEO_DECODE_FRAME_0021 


```

## -parameters

### -param hDrvCommandList: 
### -param hDrvDecoder: 
### -param SubmissionID: 
### -param *pOutputStreamParameters: 
### -param *pInputStreamParameters: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also