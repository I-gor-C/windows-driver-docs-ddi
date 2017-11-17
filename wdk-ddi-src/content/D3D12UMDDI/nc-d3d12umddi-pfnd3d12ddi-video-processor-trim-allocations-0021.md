---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021
title: PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021
author: windows-driver-content
description: 
ms.assetid: d7d2eaa5-5e2a-4077-b603-60f98ed373bf
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

# PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021 Pfnd3d12ddiVideoProcessorTrimAllocations0021; 

// Definition

UINT64 Pfnd3d12ddiVideoProcessorTrimAllocations0021 
(
	D3D12DDI_HDEVICE hdrvDevice
	D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
	UINT64 SubmissionID
)
{...}

PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021 


```

## -parameters

### -param hdrvDevice: 
### -param hDrvVideoProcessor: 
### -param SubmissionID: 



## -returns

Returns UINT64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also