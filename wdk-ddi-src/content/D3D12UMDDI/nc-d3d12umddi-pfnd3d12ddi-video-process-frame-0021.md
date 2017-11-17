---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_PROCESS_FRAME_0021
title: PFND3D12DDI_VIDEO_PROCESS_FRAME_0021
author: windows-driver-content
description: 
ms.assetid: b928b526-2b32-4380-8813-3d374c290f0f
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

# PFND3D12DDI_VIDEO_PROCESS_FRAME_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_VIDEO_PROCESS_FRAME_0021 Pfnd3d12ddiVideoProcessFrame0021; 

// Definition

VOID Pfnd3d12ddiVideoProcessFrame0021 
(
	D3D12DDI_HCOMMANDLIST hDrvCommandList
	D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
	UINT64 SubmissionID
	 const D3D12DDIARG_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_0020 *pOutputParameters
	 const D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0020 *pInputStreamParameters
	UINT NumInputStreams
)
{...}

PFND3D12DDI_VIDEO_PROCESS_FRAME_0021 


```

## -parameters

### -param hDrvCommandList: 
### -param hDrvVideoProcessor: 
### -param SubmissionID: 
### -param *pOutputParameters: 
### -param *pInputStreamParameters: 
### -param NumInputStreams: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also